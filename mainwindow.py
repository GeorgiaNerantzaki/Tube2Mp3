# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

import yt_dlp
import sys
import webbrowser


    
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    
    @Slot()
    def download_song(self):
        #parse the links from the textbrowser
        input_text=self.textEdit.toPlainText()
        #split multiple links in commas
        urls = [url.strip() for url in input_text.split(',') if url.strip()]
        self.textBrowser.setText("Downloading..")
        try:
            ydl_opts = {
                'format': 'm4a/bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'm4a',
                }]
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                for index,url in enumerate(urls):
                 ydl.download([url])  # Use the URL
            #this text will show when the download is complete
            self.textBrowser.append("Download complete... In " + self.browser + "\n")
            self.progressBar.setProperty("value", 100)
        except Exception as e:
            self.textBrowser.setText(f"ERROR: {str(e)}")
        finally:
            self.progressBar.setProperty("value", 0)
    


    @Slot()
    #paypal donation function
    def paypal_donation(self):
        url="https://www.paypal.com/gr/home"
        webbrowser.open(url)
    
    def send_signal(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 0, 391, 71))
        self.label.setPixmap(QPixmap(u"tube2mp3.gif"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 80, 101, 71))
        self.label_2.setMaximumSize(QSize(121, 71))
        self.label_2.setPixmap(QPixmap(u"icon.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 170, 351, 20))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(80, 200, 631, 286))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.textBrowser = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"background-color: rgb(61, 61, 61);")

        self.verticalLayout.addWidget(self.textBrowser)

        self.progressBar = QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.pushButton.clicked.connect(self.download_song)
        self.pushButton.clicked.connect(self.send_signal)
        self.pushButton.clicked.connect(self.the_button_was_toggled)
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.pushButton_2.clicked.connect(self.paypal_donation)
        self.verticalLayout.addWidget(self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Add a single or multiple links seperated by commas", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Paypal donation", None))
    # retranslateUi

