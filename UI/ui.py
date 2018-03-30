<<<<<<< HEAD
from PyQt5 import QtCore, QtGui, QtWidgets
import Background

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")    
        Form.resize(720, 550)
        Form.setMinimumSize(QtCore.QSize(720, 550))
        Form.setMaximumSize(QtCore.QSize(720, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Res/logotitle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setAttribute(QtCore.Qt.WA_StyledBackground)
        Form.setStyleSheet("background-image: url(:/newPrefix/Background.png);"
"font: 25 8pt \"Microsoft YaHei Light\";")
        self.Logo = QtWidgets.QGraphicsView(Form)
        self.Logo.setEnabled(True)
        self.Logo.setGeometry(QtCore.QRect(310, 100, 120, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setMinimumSize(QtCore.QSize(50, 50))
        self.Logo.setMaximumSize(QtCore.QSize(120, 120))
        self.Logo.setStyleSheet("background-image: url(:/logo/logo.png);border:none;")
        self.Logo.setObjectName("Logo")
        self.Youtube = QtWidgets.QLineEdit(Form)
        self.Youtube.setGeometry(QtCore.QRect(20, 310, 581, 20))
        self.Youtube.setStyleSheet("background:none;background-color:transparent;\n"
"border: 2px solid gray;\n"
" border-radius: 10px;")
        self.Youtube.setObjectName("Youtube")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 350, 31, 21))
        self.label.setStyleSheet("background:none;\n"
"font: 14pt \"Yu Gothic UI Semilight\";\n"
"border-radius:5px;\n"
"border-color:rgb(0,0);")
        self.label.setObjectName("label")
        self.browsefile = QtWidgets.QLineEdit(Form)
        self.browsefile.setGeometry(QtCore.QRect(90, 400, 391, 20))
        self.browsefile.setStyleSheet("background:none;\n"
"background-color:transparent;\n"
"border: 2px solid gray;\n"
" border-radius: 10px;")
        self.browsefile.setObjectName("browsefile")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(230, 230, 341, 51))
        self.label_2.setStyleSheet("background:none;\n"
"font: 25 36pt \"Yu Gothic UI Light\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.Download = QtWidgets.QPushButton(Form)
        self.Download.setGeometry(QtCore.QRect(610, 310, 75, 23))
        self.Download.setStyleSheet("#Download{\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"}\n"
"#Download:pressed{\n"
"border-color: rgb(255, 255, 255);\n"
"}")
        self.Download.setObjectName("Download")
        self.transcribe = QtWidgets.QPushButton(Form)
        self.transcribe.setGeometry(QtCore.QRect(570, 400, 75, 23))
        self.transcribe.setStyleSheet("#transcribe{\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"}\n"
"#transcribe:pressed{\n"
"border-color: rgb(255, 255, 255);\n"
"}")
        self.transcribe.setObjectName("transcribe")
        self.Browse = QtWidgets.QPushButton(Form)
        self.Browse.setGeometry(QtCore.QRect(490, 400, 75, 23))
        self.Browse.setStyleSheet("#Browse{\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"}\n"
"#Browse:pressed{\n"
"border-color: rgb(255, 255, 255);\n"
"}")
        self.Browse.setObjectName("Browse")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "NEFARIANS"))
        self.Youtube.setText(_translate("Form", "     Enter Youtube URL"))
        self.label.setText(_translate("Form", "or"))
        self.browsefile.setText(_translate("Form", "     Enter File Location"))
        self.label_2.setText(_translate("Form", "TRANSCRIBD"))
        self.Download.setText(_translate("Form", "Download"))
        self.transcribe.setText(_translate("Form", "Transcribe"))
        self.Browse.setText(_translate("Form", "Browse"))

=======
from PyQt5 import QtCore, QtGui, QtWidgets
import Background

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")    
        Form.resize(720, 550)
        Form.setMinimumSize(QtCore.QSize(720, 550))
        Form.setMaximumSize(QtCore.QSize(720, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Res/logotitle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setAttribute(QtCore.Qt.WA_StyledBackground)
        Form.setStyleSheet("background-image: url(:/newPrefix/Background.png);"
"font: 25 8pt \"Microsoft YaHei Light\";")
        self.Logo = QtWidgets.QGraphicsView(Form)
        self.Logo.setEnabled(True)
        self.Logo.setGeometry(QtCore.QRect(310, 100, 120, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setMinimumSize(QtCore.QSize(50, 50))
        self.Logo.setMaximumSize(QtCore.QSize(120, 120))
        self.Logo.setStyleSheet("background-image: url(:/logo/logo.png);border:none;")
        self.Logo.setObjectName("Logo")
        self.Youtube = QtWidgets.QLineEdit(Form)
        self.Youtube.setGeometry(QtCore.QRect(20, 310, 581, 20))
        self.Youtube.setStyleSheet("background:none;background-color:transparent;\n"
"border: 2px solid gray;\n"
" border-radius: 10px;")
        self.Youtube.setObjectName("Youtube")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 350, 31, 21))
        self.label.setStyleSheet("background:none;\n"
"font: 14pt \"Yu Gothic UI Semilight\";\n"
"border-radius:5px;\n"
"border-color:rgb(0,0);")
        self.label.setObjectName("label")
        self.browsefile = QtWidgets.QLineEdit(Form)
        self.browsefile.setGeometry(QtCore.QRect(90, 400, 391, 20))
        self.browsefile.setStyleSheet("background:none;\n"
"background-color:transparent;\n"
"border: 2px solid gray;\n"
" border-radius: 10px;")
        self.browsefile.setObjectName("browsefile")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(230, 230, 341, 51))
        self.label_2.setStyleSheet("background:none;\n"
"font: 25 36pt \"Yu Gothic UI Light\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.Download = QtWidgets.QPushButton(Form)
        self.Download.setGeometry(QtCore.QRect(610, 310, 75, 23))
        self.Download.setStyleSheet("#Download{\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"}\n"
"#Download:pressed{\n"
"border-color: rgb(255, 255, 255);\n"
"}")
        self.Download.setObjectName("Download")
        self.transcribe = QtWidgets.QPushButton(Form)
        self.transcribe.setGeometry(QtCore.QRect(570, 400, 75, 23))
        self.transcribe.setStyleSheet("#transcribe{\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"}\n"
"#transcribe:pressed{\n"
"border-color: rgb(255, 255, 255);\n"
"}")
        self.transcribe.setObjectName("transcribe")
        self.Browse = QtWidgets.QPushButton(Form)
        self.Browse.setGeometry(QtCore.QRect(490, 400, 75, 23))
        self.Browse.setStyleSheet("#Browse{\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"}\n"
"#Browse:pressed{\n"
"border-color: rgb(255, 255, 255);\n"
"}")
        self.Browse.setObjectName("Browse")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "NEFARIANS"))
        self.Youtube.setText(_translate("Form", "     Enter Youtube URL"))
        self.label.setText(_translate("Form", "or"))
        self.browsefile.setText(_translate("Form", "     Enter File Location"))
        self.label_2.setText(_translate("Form", "TRANSCRIBD"))
        self.Download.setText(_translate("Form", "Download"))
        self.transcribe.setText(_translate("Form", "Transcribe"))
        self.Browse.setText(_translate("Form", "Browse"))

>>>>>>> 1dcb99b2c04475e04f8ef00d33975d2e16a57f2d
