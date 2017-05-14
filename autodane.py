#!/usr/bin/python

from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication

from splash.dbconnecting import DBConnecting
from initialoptions.choosefootprint import ChooseFootprint
from main.mainwindow import MainWindow

import sys
import os
import psycopg2
import ConfigParser
import thread
import datetime

def main():
    app = QApplication(sys.argv)
    # app.setStyle("cleanlooks")
    # plastique
    # cde
    # motif
    # sgi
    # windows
    # cleanlooks
    # mac

    wndDBConnecting = DBConnecting()
    wndChooseFootprint = ChooseFootprint()
    wndMainWindow = MainWindow()

    conf = ConfigParser.ConfigParser()
    conf.read("settings.ini")

    showSplash = False
    runApp = True

    try:
        psycopg2.connect(host=conf.get('postgres',  'host'), user=conf.get('postgres',  'user'), password=conf.get('postgres',  'pass'), dbname=conf.get('postgres',  'db'))
        showSplash = False
    except:
        showSplash = True

    if showSplash is True:
        runApp = wndDBConnecting.exec_()

    if runApp:
        db = psycopg2.connect(host=conf.get('postgres',  'host'), user=conf.get('postgres',  'user'), password=conf.get('postgres',  'pass'), dbname=conf.get('postgres',  'db'))
        db.autocommit = True

        cursor = db.cursor()
        cursor.execute(
            "select footprint_name from footprints order by footprint_name")

        footprints_list = [""]
        for row in cursor.fetchall():
            footprints_list.append(row[0])

        cursor.close()

        wndChooseFootprint.setFootprints(footprints_list)
        wndChooseFootprint.db = db
        wndChooseFootprint.updateUI()

        if wndChooseFootprint.exec_():
            cursor = db.cursor()
            cursor.execute(
                "update task_list set in_progress = false where in_progress = true")
            cursor.close()

            cursor = db.cursor()
            cursor.execute("select createFootprint(%s);",  (str(
                wndChooseFootprint.txtFootprintName.text()), ))
            footprint_id = cursor.fetchone()[0]
            cursor.close()

            wndMainWindow.setWindowTitle("autodane : {0}".format(
                wndChooseFootprint.txtFootprintName.text()))

            wndMainWindow.db = db
            wndMainWindow.footprint_id = footprint_id

            # wndMainWindow.on_btnUpdateSummary_clicked()
            # wndMainWindow.on_btnUpdateHosts_clicked()
            # wndMainWindow.on_btnUpdateDomains_clicked()
            # wndMainWindow.on_btnUpdateCreds_clicked()
            # wndMainWindow.on_btnUpdateTaskList_clicked()
            # wndMainWindow.on_btnUpdateTaskLogs_clicked()
            # wndMainWindow.updateWebsites()

            # wndMainWindow.show()

            for item in wndChooseFootprint.txtExclude.toPlainText().split("\n"):
                if item != "":
                    cursor = db.cursor()
                    cursor.execute("select addScopeItem(%s, %s, %s)",
                                   (footprint_id,  3,  str(item), ))
                    cursor.close()

            cursor = db.cursor()
            cursor.execute(
                "select item_value from scope where footprint_id = %s and item_type = 3", (footprint_id, ))
            os.popen('echo "" > temp/exclude_list')
            for row in cursor.fetchall():
                os.popen("echo {0} >> temp/exclude_list".format(row[0]))
            cursor.close()

            # TODO: call these in a thread, so they can take as long as they
            # need to
            for item in wndChooseFootprint.txtKnownHosts.toPlainText().split("\n"):
                if item != "":
                    cursor = db.cursor()
                    cursor.execute("select addScopeItem(%s, %s, %s)",
                                   (footprint_id,  1,  str(item), ))
                    cursor.close()

            for item in wndChooseFootprint.txtKnownDCs.toPlainText().split("\n"):
                if item != "":
                    cursor = db.cursor()
                    cursor.execute(
                        "select addHost(%s, %s::varchar, ''::varchar, true)", (footprint_id,  str(item), ))
                    cursor.close()

            for item in wndChooseFootprint.txtKnownRanges.toPlainText().split("\n"):
                if item != "":
                    octs = item.split(".")
                    if octs[3] == "0/24":
                        # print "add range: {0}".format(item)
                        cursor = db.cursor()
                        cursor.execute(
                            "select addScopeItem(%s, %s, %s)", (footprint_id,  2,  str(item), ))
                        cursor.close()
                    elif item.split(".")[3] == "0/16":
                        for oct2 in range(0, 256):
                            cursor = db.cursor()
                            cursor.execute("select addScopeItem(%s, %s, %s)", (
                                footprint_id,  2,  "{0}.{1}.{2}.0/24".format(octs[0],  octs[1], oct2), ))
                            cursor.close()
                    else:
                        cursor = db.cursor()
                        cursor.execute(
                            "select addScopeItem(%s, %s, %s)", (footprint_id,  2,  str(item), ))
                        cursor.close()
                    # elif item.split(".")[3] == "0/8":
                    #     for oct1 in range(0, 256):
                    #         for oct2 in range(0, 256):
                    # print "{0}.{1}.{2}.0/24".format(octs[0],  oct1, oct2)

            for row in xrange(0, wndChooseFootprint.tblDomainCreds.rowCount()):
                domain = wndChooseFootprint.tblDomainCreds.item(row, 0).text()
                username = wndChooseFootprint.tblDomainCreds.item(
                    row, 1).text()
                password = wndChooseFootprint.tblDomainCreds.item(
                    row, 2).text()
                lm_hash = wndChooseFootprint.tblDomainCreds.item(row, 3).text()
                ntlm_hash = wndChooseFootprint.tblDomainCreds.item(
                    row, 4).text()
                valid = (wndChooseFootprint.tblDomainCreds.item(
                    row, 5).text() == "True")
                cursor = db.cursor()
                cursor.execute("select addDomainCreds(%s, %s, %s, %s, %s, %s, %s)",  (footprint_id, 0, str(
                    domain), str(username), str(password), str(lm_hash), str(ntlm_hash), ))
                cursor.close()

                if valid is True:
                    cursor = db.cursor()
                    cursor.execute("update domain_credentials set verified = true, valid = true where footprint_id = %s and domain = %s and username = %s", (
                        footprint_id, str(domain), str(username), ))
                    cursor.close()

            #print "on_btnUpdateSummary_clicked             " + str(datetime.datetime.now())
            wndMainWindow.on_btnUpdateSummary_clicked()

            #print "on_btnUpdateHosts_clicked               " + str(datetime.datetime.now())
            wndMainWindow.on_btnUpdateHosts_clicked()

            #print "on_btnRefreshVulnerabilitiesTab_clicked " + str(datetime.datetime.now())
            wndMainWindow.on_btnRefreshVulnerabilitiesTab_clicked()

            #print "on_btnUpdateDomains_clicked             " + str(datetime.datetime.now())
            wndMainWindow.on_btnUpdateDomains_clicked()

            #print "on_btnUpdateCreds_clicked               " + str(datetime.datetime.now())
            wndMainWindow.on_btnUpdateCreds_clicked()

            #print "on_btnUpdateTaskList_clicked            " + str(datetime.datetime.now())
            wndMainWindow.on_btnUpdateTaskList_clicked()

            #print "setupFilterCombos                       " + str(datetime.datetime.now())
            wndMainWindow.setupFilterCombos()

            #print "on_btnSearchLogs_clicked                " + str(datetime.datetime.now())
            # wndMainWindow.on_btnSearchLogs_clicked()

            #print "updateWebsites                          " + str(datetime.datetime.now())
            wndMainWindow.updateWebsites()

            wndMainWindow.show()

            if wndChooseFootprint.sldTestDepth.value() > 0:
                for i in wndChooseFootprint.enumerationPlugins:
                    if wndChooseFootprint.enumerationPlugins[i][3] is True:
                        cursor = db.cursor()
                        # TODO add logic to check whether these tasks have been done before adding them
                        # otherwise the same thing will be run each time the
                        # app is opened
                        cursor.execute("insert into task_list (footprint_id, task_descriptions_id, item_identifier) values (%s, %s, 0)", (
                            footprint_id, wndChooseFootprint.enumerationPlugins[i][0], ))
                        cursor.close()

                nmap_timing = wndChooseFootprint.cmbNmapTiming.currentText()
                network_interface = wndChooseFootprint.cmbNetworkInterface.currentText()
                thread_counts = {}
                thread_counts['all'] = wndChooseFootprint.sedAllTasks.value()
                thread_counts['footprinting'] = wndChooseFootprint.sedFootprinting.value()
                thread_counts['exploits'] = wndChooseFootprint.sedExploits.value()
                thread_counts['pivoting'] = wndChooseFootprint.sedPivoting.value()
                thread_counts['pivoting_msf'] = wndChooseFootprint.sedPivotingMsf.value()
                thread_counts['domain_enumeration'] = wndChooseFootprint.sedDomainEnumeration.value()

                thread.start_new_thread(wndMainWindow.startWork, (wndChooseFootprint.sldTestDepth.value(), nmap_timing, network_interface, thread_counts))
        else:
            quit()
    else:
        quit()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
