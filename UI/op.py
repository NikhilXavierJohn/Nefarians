<<<<<<< HEAD
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'op.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(649, 485)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-image: url(:/f/Background.png);")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 771, 551))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(-100, 0, 831, 531))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_8.setGeometry(QtCore.QRect(-10, 0, 681, 501))
        self.textBrowser_8.setObjectName("textBrowser_8")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/f/scale-justice-crime-law-ethics-balance-3f7a26cacefd3896-512x512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(-10, 0, 671, 501))
        self.textBrowser_2.setObjectName("textBrowser_2")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("14292-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_5.setGeometry(QtCore.QRect(-10, 0, 671, 501))
        self.textBrowser_5.setObjectName("textBrowser_5")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("136160-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_6.setGeometry(QtCore.QRect(-10, 0, 671, 491))
        self.textBrowser_6.setObjectName("textBrowser_6")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("books-household-graduation-cap-hardback-library-learning-school-knowledge-study-3b7fa653b6592508-512x512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser_7.setGeometry(QtCore.QRect(-10, -10, 671, 511))
        self.textBrowser_7.setObjectName("textBrowser_7")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Public_health_icon_-_Noun_Project_6435.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_5, icon5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("sport.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_6, icon6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.tab_7)
        self.textBrowser_9.setGeometry(QtCore.QRect(-10, -10, 661, 531))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_9.setFont(font)
        self.textBrowser_9.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser_9.setAutoFillBackground(True)
        self.textBrowser_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_9.setObjectName("textBrowser_9")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img_497562.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_7, icon7, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Crime"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Politics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Economy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Education"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Health"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Sports"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "Entertainment"))

import Background
=======
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'op.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(649, 485)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-image: url(:/f/Background.png);")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 771, 551))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(-100, 0, 831, 531))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_8.setGeometry(QtCore.QRect(-10, 0, 681, 501))
        self.textBrowser_8.setObjectName("textBrowser_8")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/f/scale-justice-crime-law-ethics-balance-3f7a26cacefd3896-512x512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(-10, 0, 671, 501))
        self.textBrowser_2.setObjectName("textBrowser_2")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("14292-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_5.setGeometry(QtCore.QRect(-10, 0, 671, 501))
        self.textBrowser_5.setObjectName("textBrowser_5")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("136160-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_6.setGeometry(QtCore.QRect(-10, 0, 671, 491))
        self.textBrowser_6.setObjectName("textBrowser_6")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("books-household-graduation-cap-hardback-library-learning-school-knowledge-study-3b7fa653b6592508-512x512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser_7.setGeometry(QtCore.QRect(-10, -10, 671, 511))
        self.textBrowser_7.setObjectName("textBrowser_7")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Public_health_icon_-_Noun_Project_6435.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_5, icon5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("sport.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_6, icon6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.tab_7)
        self.textBrowser_9.setGeometry(QtCore.QRect(-10, -10, 661, 531))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_9.setFont(font)
        self.textBrowser_9.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser_9.setAutoFillBackground(True)
        self.textBrowser_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_9.setObjectName("textBrowser_9")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img_497562.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_7, icon7, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Crime"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Politics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Economy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Education"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Health"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Sports"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "Entertainment"))

import Background
>>>>>>> 1dcb99b2c04475e04f8ef00d33975d2e16a57f2d
