#import Total as t
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QDialog,QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
import Background
global fileName
class App(QWidget):
    def __init__(self):
        super(App,self).__init__()
        loadUi('Ui1.ui',self)
        self.setWindowTitle('Transcribe')
        self.Browse.clicked.connect(self.getfile)
        self.transcribe.clicked.connect(self.tb)
        self.Download.clicked.connect(self.db)
        
        
    def getfile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Video Files (*.mp4);;AudioFiles(*.mp3)", options=options)
        self.browsefile.setText(fileName)
        self.fileName=fileName
    def tb(self):
        s='.mp4'
        print(self.fileName)
        if (self.fileName.endswith(s)):
             t.converter(self.fileName)
        elif(self.fileName.endswith('.wav')):
             t.splitter(self.fileName)
             
    def db(self):
         self.s=loadUi('op.ui')
         self.s.show() 
        
        #t.download()

app = QApplication(sys.argv)
ex = App()
ex.show()
sys.exit(app.exec_())


getfile()
