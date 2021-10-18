# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PageSelector = QtWidgets.QStackedWidget(self.centralwidget)
        self.PageSelector.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.PageSelector.setObjectName("PageSelector")
        self.MainMenu_pg = QtWidgets.QWidget()
        self.MainMenu_pg.setObjectName("MainMenu_pg")
        self.frame = QtWidgets.QFrame(self.MainMenu_pg)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(25, 46, 122)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(330, 160, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    background-color: rgb(85, 255, 127)\n"
"}\n"
"\n"
"QPushButton: active {\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.PageSelector.addWidget(self.MainMenu_pg)
        self.Map_pg = QtWidgets.QWidget()
        self.Map_pg.setMouseTracking(False)
        self.Map_pg.setTabletTracking(False)
        self.Map_pg.setObjectName("Map_pg")
        self.MapScrollArea = QtWidgets.QScrollArea(self.Map_pg)
        self.MapScrollArea.setGeometry(QtCore.QRect(10, 40, 781, 291))
        self.MapScrollArea.setMouseTracking(False)
        self.MapScrollArea.setTabletTracking(False)
        self.MapScrollArea.setAcceptDrops(False)
        self.MapScrollArea.setWidgetResizable(False)
        self.MapScrollArea.setObjectName("MapScrollArea")
        self.scrollAreaWidgetCHANGE_GEO_SIZE = QtWidgets.QWidget()
        self.scrollAreaWidgetCHANGE_GEO_SIZE.setGeometry(QtCore.QRect(0, 0, 5000, 1659))
        self.scrollAreaWidgetCHANGE_GEO_SIZE.setObjectName("scrollAreaWidgetCHANGE_GEO_SIZE")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.scrollAreaWidgetCHANGE_GEO_SIZE)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 5011, 1661))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.GridFormatting = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.GridFormatting.setContentsMargins(0, 0, 0, 0)
        self.GridFormatting.setObjectName("GridFormatting")
        self.BackgroundFrame = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.BackgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackgroundFrame.setObjectName("BackgroundFrame")
        self.GridFormatting.addWidget(self.BackgroundFrame, 0, 0, 1, 1)
        self.MapScrollArea.setWidget(self.scrollAreaWidgetCHANGE_GEO_SIZE)
        self.mapButtons_Group = QtWidgets.QGroupBox(self.Map_pg)
        self.mapButtons_Group.setGeometry(QtCore.QRect(10, 340, 781, 131))
        self.mapButtons_Group.setObjectName("mapButtons_Group")
        self.mapResearch_Button = QtWidgets.QPushButton(self.mapButtons_Group)
        self.mapResearch_Button.setGeometry(QtCore.QRect(120, 20, 101, 41))
        self.mapResearch_Button.setStyleSheet("pushButton2 {\n"
"  display: inline-block;\n"
"  -webkit-box-sizing: content-box;\n"
"  -moz-box-sizing: content-box;\n"
"  box-sizing: content-box;\n"
"  cursor: pointer;\n"
"  padding: 10px 20px;\n"
"  border: 1px solid #018dc4;\n"
"  -webkit-border-radius: 3px;\n"
"  border-radius: 3px;\n"
"  font: normal 16px/normal Tahoma, Geneva, sans-serif;\n"
"  color: rgba(255,255,255,0.9);\n"
"  -o-text-overflow: clip;\n"
"  text-overflow: clip;\n"
"  background: #0199d9;\n"
"  -webkit-box-shadow: 2px 2px 2px 0 rgba(0,0,0,0.2) ;\n"
"  box-shadow: 2px 2px 2px 0 rgba(0,0,0,0.2) ;\n"
"  text-shadow: -1px -1px 0 rgba(15,73,168,0.66) ;\n"
"  -webkit-transition: all 300ms cubic-bezier(0.42, 0, 0.58, 1);\n"
"  -moz-transition: all 300ms cubic-bezier(0.42, 0, 0.58, 1);\n"
"  -o-transition: all 300ms cubic-bezier(0.42, 0, 0.58, 1);\n"
"  transition: all 300ms cubic-bezier(0.42, 0, 0.58, 1);\n"
"}")
        self.mapResearch_Button.setObjectName("mapResearch_Button")
        self.mapEngineering_Button = QtWidgets.QPushButton(self.mapButtons_Group)
        self.mapEngineering_Button.setGeometry(QtCore.QRect(120, 70, 101, 51))
        self.mapEngineering_Button.setObjectName("mapEngineering_Button")
        self.mapEconomy_Button = QtWidgets.QPushButton(self.mapButtons_Group)
        self.mapEconomy_Button.setGeometry(QtCore.QRect(230, 20, 101, 101))
        self.mapEconomy_Button.setObjectName("mapEconomy_Button")
        self.mapArmy_Button = QtWidgets.QPushButton(self.mapButtons_Group)
        self.mapArmy_Button.setGeometry(QtCore.QRect(10, 20, 101, 101))
        self.mapArmy_Button.setObjectName("mapArmy_Button")
        self.mapEndTurn_Button = QtWidgets.QPushButton(self.mapButtons_Group)
        self.mapEndTurn_Button.setGeometry(QtCore.QRect(340, 20, 101, 101))
        self.mapEndTurn_Button.setObjectName("mapEndTurn_Button")
        self.credits_Label = QtWidgets.QLabel(self.Map_pg)
        self.credits_Label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.credits_Label.setObjectName("credits_Label")
        self.PageSelector.addWidget(self.Map_pg)
        self.Planet_pg = QtWidgets.QWidget()
        self.Planet_pg.setObjectName("Planet_pg")
        self.planetName_Label = QtWidgets.QLabel(self.Planet_pg)
        self.planetName_Label.setGeometry(QtCore.QRect(310, 10, 181, 51))
        self.planetName_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.planetName_Label.setObjectName("planetName_Label")
        self.backPlanet_Button = QtWidgets.QPushButton(self.Planet_pg)
        self.backPlanet_Button.setGeometry(QtCore.QRect(30, 20, 41, 41))
        self.backPlanet_Button.setText("")
        self.backPlanet_Button.setObjectName("backPlanet_Button")
        self.pushButton_2 = QtWidgets.QPushButton(self.Planet_pg)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 390, 81, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Planet_pg)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 390, 81, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Planet_pg)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 390, 81, 81))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groundPlanet_Button = QtWidgets.QPushButton(self.Planet_pg)
        self.groundPlanet_Button.setGeometry(QtCore.QRect(330, 390, 81, 81))
        self.groundPlanet_Button.setObjectName("groundPlanet_Button")
        self.PageSelector.addWidget(self.Planet_pg)
        self.PlanetGround_pg = QtWidgets.QWidget()
        self.PlanetGround_pg.setObjectName("PlanetGround_pg")
        self.garrisonGround_List = QtWidgets.QListWidget(self.PlanetGround_pg)
        self.garrisonGround_List.setGeometry(QtCore.QRect(7, 70, 381, 241))
        self.garrisonGround_List.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.garrisonGround_List.setObjectName("garrisonGround_List")
        self.outboundGround_List = QtWidgets.QListWidget(self.PlanetGround_pg)
        self.outboundGround_List.setGeometry(QtCore.QRect(10, 350, 381, 121))
        self.outboundGround_List.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.outboundGround_List.setObjectName("outboundGround_List")
        self.enemyGround_List = QtWidgets.QListWidget(self.PlanetGround_pg)
        self.enemyGround_List.setGeometry(QtCore.QRect(410, 70, 371, 261))
        self.enemyGround_List.setObjectName("enemyGround_List")
        self.backGround_Button = QtWidgets.QPushButton(self.PlanetGround_pg)
        self.backGround_Button.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.backGround_Button.setText("")
        self.backGround_Button.setObjectName("backGround_Button")
        self.outboundGround_Button = QtWidgets.QPushButton(self.PlanetGround_pg)
        self.outboundGround_Button.setGeometry(QtCore.QRect(10, 310, 381, 21))
        self.outboundGround_Button.setObjectName("outboundGround_Button")
        self.garrisonGround_Button = QtWidgets.QPushButton(self.PlanetGround_pg)
        self.garrisonGround_Button.setGeometry(QtCore.QRect(10, 330, 381, 21))
        self.garrisonGround_Button.setObjectName("garrisonGround_Button")
        self.PageSelector.addWidget(self.PlanetGround_pg)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.PageSelector.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.mapButtons_Group.setTitle(_translate("MainWindow", "Options"))
        self.mapResearch_Button.setText(_translate("MainWindow", "Research"))
        self.mapEngineering_Button.setText(_translate("MainWindow", "Engineering"))
        self.mapEconomy_Button.setText(_translate("MainWindow", "Economy"))
        self.mapArmy_Button.setText(_translate("MainWindow", "Army"))
        self.mapEndTurn_Button.setText(_translate("MainWindow", "End Turn"))
        self.credits_Label.setText(_translate("MainWindow", "Credits: "))
        self.planetName_Label.setText(_translate("MainWindow", "Planet Name Here"))
        self.pushButton_2.setText(_translate("MainWindow", "Move"))
        self.pushButton_3.setText(_translate("MainWindow", "Train"))
        self.pushButton_4.setText(_translate("MainWindow", "Space"))
        self.groundPlanet_Button.setText(_translate("MainWindow", "Ground"))
        self.outboundGround_Button.setText(_translate("MainWindow", "Move Outbound"))
        self.garrisonGround_Button.setText(_translate("MainWindow", "Move to Garrison"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

