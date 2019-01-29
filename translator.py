from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from tkinter import filedialog
from imageReader import Reader
from googletrans import Translator



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 870)
        self.filePath = ''
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectImage = QtWidgets.QPushButton(self.centralwidget)
        self.selectImage.setGeometry(QtCore.QRect(80, 60, 161, 51))
        self.selectImage.setObjectName("selectImage")
        self.Translate = QtWidgets.QPushButton(self.centralwidget)
        self.Translate.setGeometry(QtCore.QRect(520, 60, 171, 51))
        self.Translate.setObjectName("Translate")
        self.originalText = QtWidgets.QTextEdit(self.centralwidget)
        self.originalText.setGeometry(QtCore.QRect(80, 160, 321, 541))
        self.originalText.setObjectName("originalText")
        self.translatedText = QtWidgets.QTextEdit(self.centralwidget)
        self.translatedText.setGeometry(QtCore.QRect(520, 160, 351, 541))
        self.translatedText.setObjectName("translatedText")
        self.translatedText.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.selectImage.clicked.connect(self.selectImageClicked)
        self.Translate.clicked.connect(self.translateClicked)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectImage.setText(_translate("MainWindow", "Select Image"))
        self.Translate.setText(_translate("MainWindow", "Translate"))

    def extractTextImage(self):
        
        reader = Reader()
        reader.setFilePath(self.filePath)
        text = reader.getText()
        return text

    def translate(self, text):
        trans = Translator()
        translated = trans.translate(text, dest = 'tr')
        return translated.text
        



    def selectImageClicked(self):
        file_path = filedialog.askopenfilename()
        self.filePath = file_path
        print(self.filePath)
        text = self.extractTextImage()
        self.originalText.setPlainText(text)

    def translateClicked(self):
        
        text = self.originalText.toPlainText()
        
        translated = self.translate(text)
        print(translated)
        self.translatedText.setPlainText(translated)

    
      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

