
from tkinter import filedialog
from pytube import YouTube
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class login(QDialog):
    def __init__(self):
        super(login,self).__init__()
        loadUi("ytd_ui.ui",self)
        
        self.path_btn.clicked.connect(self.opendirectory)
        self.dwnld.clicked.connect(self.download)
        self.resetbtn.clicked.connect(self.reset)
        
        # text = str(combobox1.currentText())
    
    def opendirectory(self):
        global Folder_name
        Folder_name = QtWidgets.QFileDialog.getExistingDirectory(self)
        if(len(Folder_name)<1):
            self.path_label.setText("Please Choose the Folder")
            self.path_label.setStyleSheet("color: rgb(255, 255, 255); font: 87 8pt Segoe UI Black;")

        else:
            self.path_label.setText(Folder_name)
            self.path_label.setStyleSheet("color: rgb(0, 255, 0); font: 87 8pt Segoe UI Black;")


    def download(self):
        choice_quality = self.choice_combo.currentIndex()
        url_set = self.URL_GET.text() 
        if(len(url_set)<1):
            self.url_label.setText("Please paste the URL")
            self.url_label.setStyleSheet("color: rgb(255, 255, 255); font: 87 8pt Segoe UI Black;")
        else:
            yt = YouTube(url_set)
            string_set  = "Downloading" + yt.title
            
            if(choice_quality == 1):
                select = yt.streams.filter(progressive=True,res="720p",file_extension='mp4').first()
                
                self.prog_label.setText(string_set)
                self.prog_label.setStyleSheet("color: rgb(255, 255, 255); font: 87 8pt Segoe UI Black;")
                select.download(Folder_name)
            if(choice_quality == 2):
                select = yt.streams.filter(progressive=True,res="360p",file_extension='mp4').last()
                self.prog_label.setText(string_set)
                self.prog_label.setStyleSheet("color: rgb(255, 255, 255); font: 87 8pt Segoe UI Black;")
                select.download(Folder_name)
            if(choice_quality == 3):
                select = yt.streams.filter(only_audio=True,file_extension='mp3').first()
                self.prog_label.setText(string_set)
                self.prog_label.setStyleSheet("color: rgb(255, 255, 255); font: 87 8pt Segoe UI Black;")
                select.download(Folder_name)

    def reset(self):
        string_set = ""
        self.URL_GET.setText(string_set)
        self.url_label.clear()
        self.path_label.clear()
        self.prog_label.clear()
            




        
            
app = QApplication(sys.argv)
gui = login()
widget = QtWidgets.QStackedWidget()
widget.setFixedHeight(535)
widget.setFixedWidth(514)
widget.addWidget(gui)
widget.show()
sys.exit(app.exec_())

        
        


"""
TO DO: IMPLEMENT THE RESET BUTTON 


"""