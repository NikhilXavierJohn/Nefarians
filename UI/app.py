import sys
sys.path.append('C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/Code')
import Total as t
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QDialog,QFileDialog
from ui import Ui_Form
from PyQt5.uic import loadUi

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
        self.ui.Browse.clicked.connect(self.getfile)
        self.ui.transcribe.clicked.connect(self.tb)
        self.ui.Download.clicked.connect(self.db)
        
        
    def getfile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Video Files (*.mp4);;AudioFiles(*.mp3)", options=options)
        self.ui.browsefile.setText(fileName)
        self.ui.fileName=fileName
    def tb(self):
        s='.mp4'
        print(self.ui.fileName)
        if (self.ui.fileName.endswith(s)):
             t.converter(self.ui.fileName)
        elif(self.ui.fileName.endswith('.wav')):
             t.splitter(self.ui.fileName)
             
    def db(self):
         t.download(self.ui.Download.text())
         self.s=loadUi('op.ui')
         self.s.show() 
        
        

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())