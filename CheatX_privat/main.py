from PyQt5 import QtCore, QtGui, QtWidgets
import os
from time import sleep
import shutil
from random import *
from string import ascii_uppercase
from espbox import *
from esp_hp import *
from sc import *
from bhop import *
from no_flash import *
from onebyteradar import *
from onebyte_money import *
from trigger_bot import *
from onebytewallhack import *
from PyQt5.QtWidgets import QColorDialog, QComboBox
from wmi import WMI
import socket


# имена фейк файлов для защиты от VAC
rnd_text_name_file1_cheatx_free = ''.join(choice(ascii_uppercase) for e in range(30))
rnd_text_name_file2_cheatx_free = ''.join(choice(ascii_uppercase) for s in range(30))
# текст в фейк файлах
rnd_text_file1_cheatx_free = ''.join(choice(ascii_uppercase) for f in range(3000))
rnd_text_file2_cheatx_free = ''.join(choice(ascii_uppercase) for o in range(3000))


appdata_p = os.environ['AppData']

def cheat_files():
    appdata_p = os.environ['AppData']
    folder = '%s\\CheatX' % (appdata_p)
    check_folder = os.path.isdir(folder)
    if check_folder == True:
        shutil.rmtree('%s\\CheatX\\cheatx-private' % (appdata_p), ignore_errors=True)
        os.mkdir('%s\\CheatX\\cheatx-private' % (appdata_p))
        os.mkdir('%s\\CheatX\\cheatx-private\\settings' % (appdata_p))
        # bunnyhop
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\b' % (appdata_p))
        # esp
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\e' % (appdata_p))
        # onebyte_wh
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\w' % (appdata_p))
        # rcs
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\r' % (appdata_p))
        # no flash
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\n' % (appdata_p))
        # onebyte_radar
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\br' % (appdata_p))
        # onebyte_money
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\mn' % (appdata_p))
        # trigger_bot
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\t' % (appdata_p))
        # sc
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\sc' % (appdata_p))


        # esp_box
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\eb' % (appdata_p))
        #esp_name
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\nm' % (appdata_p))
        #esp_line
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\l' % (appdata_p))
        #esp_hp
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\eh' % (appdata_p))

        file1_av = open('%s\\CheatX\\cheatx-private\\%s' % (appdata_p, rnd_text_name_file1_cheatx_free), 'w')
        file1_av.write(rnd_text_file1_cheatx_free)
        file1_av.close()
        file2_av = open('%s\\CheatX\\cheatx-private\\settings\\%s' % (appdata_p, rnd_text_name_file2_cheatx_free), 'w')
        file2_av.write(rnd_text_file2_cheatx_free)
        file2_av.close()
    elif check_folder == False:
        os.mkdir('%s\\CheatX' % (appdata_p))
        os.mkdir('%s\\CheatX\\cheatx-private' % (appdata_p))
        os.mkdir('%s\\CheatX\\cheatx-private\\settings' % (appdata_p))
        # bunnyhop
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\b' % (appdata_p))
        # esp
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\e' % (appdata_p))
        # onebyte_wh
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\w' % (appdata_p))
        # rcs
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\r' % (appdata_p))
        # no flash
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\n' % (appdata_p))
        # onebyte_radar
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\br' % (appdata_p))
        # onebyte_money
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\mn' % (appdata_p))
        # trigger_bot
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\t' % (appdata_p))

        #esp_box
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\eb' % (appdata_p))
        #esp_name
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\nm' % (appdata_p))
        #esp_line
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\l' % (appdata_p))
        #esp_hp
        os.mkdir('%s\\CheatX\\cheatx-private\\settings\\eh' % (appdata_p))

        file1_av = open('%s\\CheatX\\cheatx-private\\%s' % (appdata_p, rnd_text_name_file1_cheatx_free), 'w')
        file1_av.write(rnd_text_file1_cheatx_free)
        file1_av.close()
        file2_av = open('%s\\CheatX\\cheatx-private\\settings\\%s' % (appdata_p, rnd_text_name_file2_cheatx_free), 'w')
        file2_av.write(rnd_text_file2_cheatx_free)
        file2_av.close()

    else:
        BrokenPipeError



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('C:/Users/stvin/Documents/x.gif'))
        MainWindow.resize(654, 444)
        MainWindow.setStyleSheet("background: #4A4141;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-3, -22, 1102, 679))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"    color: #F5D2A9;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #653E32;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #653E32;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}\n"
"#ff4646")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(260, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setGeometry(QtCore.QRect(520, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(266, 20, 126, 42))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #FF5D02;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(43, 160, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #fafaea;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(43, 229, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #fafaea;")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(451, 208, 30, 30))
        self.pushButton.setStyleSheet("border-radius: 15px;\n"
"background: url(C:/Users/stvin/PycharmProjects/PyQt_Cheat/ba.gif);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(519, 159, 107, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: #B03939;\n"
"    color: #f5e2cb;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #be502f;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff4646;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(519, 226, 107, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: #B03939;\n"
"    color: #f5e2cb;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #be502f;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff4646;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_26 = QtWidgets.QPushButton(self.tab)
        self.pushButton_26.setGeometry(QtCore.QRect(130, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_26.setObjectName("pushButton_26")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(43, 298, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: #fafaea;")
        self.label_14.setObjectName("label_14")
        self.pushButton_27 = QtWidgets.QPushButton(self.tab)
        self.pushButton_27.setGeometry(QtCore.QRect(519, 295, 107, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton{\n"
"    background-color: #B03939;\n"
"    color: #f5e2cb;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #be502f;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff4646;\n"
"}")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.tab)
        self.pushButton_28.setGeometry(QtCore.QRect(519, 364, 107, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("QPushButton{\n"
"    background-color: #B03939;\n"
"    color: #f5e2cb;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #be502f;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff4646;\n"
"}")
        self.pushButton_28.setObjectName("pushButton_28")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(43, 367, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: #fafaea;")
        self.label_15.setObjectName("label_15")
        #self.pushButton_30 = QtWidgets.QPushButton(self.tab)
        #self.pushButton_30.setGeometry(QtCore.QRect(461, 227, 30, 30))
        #self.pushButton_30.setStyleSheet("border-radius: 15px;\n"
#"background: url(C:/Users/stvin/PycharmProjects/PyQt_Cheat/ba.png);")
        #self.pushButton_30.setText("")
        #self.pushButton_30.setObjectName("pushButton_30")
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setKerning(True)
        self.tab_5.setFont(font)
        self.tab_5.setAccessibleName("")
        self.tab_5.setObjectName("tab_5")
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setGeometry(QtCore.QRect(59, 253, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: #fafaea;")
        self.label_16.setObjectName("label_16")
        self.pushButton_31 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_31.setGeometry(QtCore.QRect(471, 250, 107, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("QPushButton{\n"
"    background-color: #B03939;\n"
"    color: #f5e2cb;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #be502f;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff4646;\n"
"}")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_32.setGeometry(QtCore.QRect(0, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_33.setGeometry(QtCore.QRect(130, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #653E32;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}\n"
"#ff4646")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_34.setGeometry(QtCore.QRect(260, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_35.setGeometry(QtCore.QRect(390, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_36.setGeometry(QtCore.QRect(520, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_36.setObjectName("pushButton_36")
        self.label_17 = QtWidgets.QLabel(self.tab_5)
        self.label_17.setGeometry(QtCore.QRect(266, 20, 126, 42))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: #FF5D02;\n"
"")
        self.label_17.setObjectName("label_17")
        self.verticalSlider = QtWidgets.QSlider(self.tab_5)
        self.verticalSlider.setGeometry(QtCore.QRect(611, 189, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(260, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #653E32;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}\n"
"#ff4646")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(390, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_12.setGeometry(QtCore.QRect(520, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(266, 20, 126, 42))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #FF5D02;")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(38, 230, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #fafaea;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(87, 253, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #fafaea;")
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(491, 237, 107, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color: #B03939;\n"
"    color: #f5e2cb;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #be502f;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff4646;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_75 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_75.setGeometry(QtCore.QRect(130, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_75.setFont(font)
        self.pushButton_75.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_75.setObjectName("pushButton_75")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(266, 20, 126, 42))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #FF5D02;\n"
"")
        self.label_3.setObjectName("label_3")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_14.setGeometry(QtCore.QRect(260, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_15.setGeometry(QtCore.QRect(390, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setAutoFillBackground(False)
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #653E32;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}\n"
"#ff4646")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_16.setGeometry(QtCore.QRect(520, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(24, 244, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #fafaea;")
        self.label_9.setObjectName("label_9")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_21.setGeometry(QtCore.QRect(491, 243, 107, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("QPushButton{\n"
"    background-color: #B03939;\n"
"    color: #f5e2cb;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #be502f;\n"
"}\n"
"QPushButton:pressed{\n"    
"    background-color: #ff4646;\n"
"}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox.setGeometry(QtCore.QRect(620, 250, 70, 17))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_114 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_114.setGeometry(QtCore.QRect(130, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_114.setFont(font)
        self.pushButton_114.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_114.setObjectName("pushButton_114")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(266, 20, 126, 42))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #FF5D02;\n"
"")
        self.label_4.setObjectName("label_4")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_17.setGeometry(QtCore.QRect(0, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_18.setGeometry(QtCore.QRect(260, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_19.setGeometry(QtCore.QRect(390, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_20.setGeometry(QtCore.QRect(520, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #653E32;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}\n"
"#ff4646")
        self.pushButton_20.setObjectName("pushButton_20")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(41, 128, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #fafaea;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(41, 196, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #fafaea;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(41, 261, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #fafaea;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(41, 323, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: #fafaea;")
        self.label_13.setObjectName("label_13")
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_22.setGeometry(QtCore.QRect(519, 128, 107, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("QPushButton{\n"
"    background-color: #B03939;\n"
"    color: #f5e2cb;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #be502f;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff4646;\n"
"}")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_23.setGeometry(QtCore.QRect(519, 192, 107, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("QPushButton{\n"
"    background-color: #B03939;\n"
"    color: #f5e2cb;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #be502f;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff4646;\n"
"}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_24.setGeometry(QtCore.QRect(519, 256, 107, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("QPushButton{\n"
"    background-color: #B03939;\n"
"    color: #f5e2cb;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #be502f;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff4646;\n"
"}")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_25.setGeometry(QtCore.QRect(519, 320, 107, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("QPushButton{\n"
"    background-color: #B03939;\n"
"    color: #f5e2cb;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #be502f;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff4646;\n"
"}")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_37 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_37.setGeometry(QtCore.QRect(519, 384, 107, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setStyleSheet("QPushButton{\n"
"    background-color: #B03939;\n"
"    color: #f5e2cb;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #be502f;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff4646;\n"
"}")
        self.pushButton_37.setObjectName("pushButton_37")
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(40, 387, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: #fafaea;")
        self.label_18.setObjectName("label_18")
        self.pushButton_115 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_115.setGeometry(QtCore.QRect(130, 70, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_115.setFont(font)
        self.pushButton_115.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #453C3C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #312828;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(148, 40, 40);\n"
"}")
        self.pushButton_115.setObjectName("pushButton_115")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.comboBox = QtWidgets.QComboBox(self.tab_4)
        self.comboBox.setGeometry(QtCore.QRect(440, 135, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CheatX - Private"))
        self.pushButton_5.setText(_translate("MainWindow", "ESP"))
        self.pushButton_6.setText(_translate("MainWindow", "RCS"))
        self.pushButton_7.setText(_translate("MainWindow", "BHOP"))
        self.pushButton_8.setText(_translate("MainWindow", "Other"))
        self.label_2.setText(_translate("MainWindow", "CheatX"))
        self.label_5.setText(_translate("MainWindow", "Дистанция до врага"))
        self.label_6.setText(_translate("MainWindow", "Esp BOX -  Обводка врагов в квадраты"))
        self.pushButton_2.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.pushButton_3.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.pushButton_26.setText(_translate("MainWindow", "SC"))
        self.label_14.setText(_translate("MainWindow", "Name - виден ник противника"))
        self.pushButton_27.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.pushButton_28.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.label_15.setText(_translate("MainWindow", "Esp HP - видно здоровье врагов"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "esp"))
        self.label_16.setText(_translate("MainWindow", "Shot Control - контроль выстрелов"))
        self.pushButton_31.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.pushButton_32.setText(_translate("MainWindow", "ESP"))
        self.pushButton_33.setText(_translate("MainWindow", "SC"))
        self.pushButton_34.setText(_translate("MainWindow", "RCS"))
        self.pushButton_35.setText(_translate("MainWindow", "BHOP"))
        self.pushButton_36.setText(_translate("MainWindow", "Other"))
        self.label_17.setText(_translate("MainWindow", "CheatX"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "SC"))
        self.pushButton_9.setText(_translate("MainWindow", "ESP"))
        self.pushButton_10.setText(_translate("MainWindow", "RCS"))
        self.pushButton_11.setText(_translate("MainWindow", "BHOP"))
        self.pushButton_12.setText(_translate("MainWindow", "Other"))
        self.label.setText(_translate("MainWindow", "CheatX"))
        self.label_7.setText(_translate("MainWindow", "RCS - полный контроль отдачи всех"))
        self.label_8.setText(_translate("MainWindow", "автоматических оружий. "))
        self.pushButton_4.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.pushButton_75.setText(_translate("MainWindow", "SC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "rcs"))
        self.label_3.setText(_translate("MainWindow", "CheatX"))
        self.pushButton_13.setText(_translate("MainWindow", "ESP"))
        self.pushButton_14.setText(_translate("MainWindow", "RCS"))
        self.pushButton_15.setText(_translate("MainWindow", "BHOP"))
        self.pushButton_16.setText(_translate("MainWindow", "Other"))
        self.label_9.setText(_translate("MainWindow", "BHOP  - Автоматическая распрыжка"))
        self.pushButton_21.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.pushButton_114.setText(_translate("MainWindow", "SC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "bhop"))
        self.label_4.setText(_translate("MainWindow", "CheatX"))
        self.pushButton_17.setText(_translate("MainWindow", "ESP"))
        self.pushButton_18.setText(_translate("MainWindow", "RCS"))
        self.pushButton_19.setText(_translate("MainWindow", "BHOP"))
        self.pushButton_20.setText(_translate("MainWindow", "Other"))
        self.label_10.setText(_translate("MainWindow", "TriggerBot - автоматическая стрельба"))
        self.label_11.setText(_translate("MainWindow", "No Flash - флешки не ослепляют"))
        self.label_12.setText(_translate("MainWindow", "MoneyEnemy - видны деньги противника"))
        self.label_13.setText(_translate("MainWindow", "RadarHack - противники видны на радаре"))
        self.pushButton_22.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.pushButton_23.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.pushButton_24.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.pushButton_25.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.pushButton_37.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.label_18.setText(_translate("MainWindow", "OneByteWallHack "))
        self.pushButton_115.setText(_translate("MainWindow", "SC"))
        self.comboBox.setItemText(0, _translate("MainWindow", "shift"))
        self.comboBox.setItemText(1, _translate("MainWindow", "alt"))
        self.comboBox.setItemText(2, _translate("MainWindow", "CapsLock"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "other"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #esp
        self.pushButton_5.clicked.connect(self.move_tab_1)
        self.pushButton_26.clicked.connect(self.move_tab_2)
        self.pushButton_6.clicked.connect(self.move_tab_3)
        self.pushButton_7.clicked.connect(self.move_tab_4)
        self.pushButton_8.clicked.connect(self.move_tab_5)
        self.pushButton_5.clicked.connect(self.move_tab_1)
        # sc
        self.pushButton_32.clicked.connect(self.move_tab_1)
        self.pushButton_33.clicked.connect(self.move_tab_2)
        self.pushButton_34.clicked.connect(self.move_tab_3)
        self.pushButton_35.clicked.connect(self.move_tab_4)
        self.pushButton_36.clicked.connect(self.move_tab_5)
        self.pushButton_32.clicked.connect(self.move_tab_1)
        # rcs
        self.pushButton_9.clicked.connect(self.move_tab_1)
        self.pushButton_75.clicked.connect(self.move_tab_2)
        self.pushButton_10.clicked.connect(self.move_tab_3)
        self.pushButton_11.clicked.connect(self.move_tab_4)
        self.pushButton_12.clicked.connect(self.move_tab_5)
        # bhop
        self.pushButton_13.clicked.connect(self.move_tab_1)
        self.pushButton_114.clicked.connect(self.move_tab_2)
        self.pushButton_14.clicked.connect(self.move_tab_3)
        self.pushButton_15.clicked.connect(self.move_tab_4)
        self.pushButton_15.clicked.connect(self.move_tab_5)
        self.pushButton_16.clicked.connect(self.move_tab_5)
        # other
        self.pushButton_17.clicked.connect(self.move_tab_1)
        self.pushButton_115.clicked.connect(self.move_tab_2)
        self.pushButton_18.clicked.connect(self.move_tab_3)
        self.pushButton_19.clicked.connect(self.move_tab_4)
        self.pushButton_20.clicked.connect(self.move_tab_5)
        # settings
        self.pushButton_3.clicked.connect(self.esp_box)
        self.pushButton_28.clicked.connect(self.esp_hpp)
        self.pushButton_27.clicked.connect(self.esp_nm)
        self.verticalSlider.setValue(0)
        self.pushButton_31.clicked.connect(self.scs)
        # color choose
        #self.pushButton_30.clicked.connect(color_choose)
        # line
        self.pushButton_2.clicked.connect(self.lines)
        # bhop
        self.pushButton_21.clicked.connect(self.BHOP)

        self.pushButton_37.clicked.connect(self.obh)
        self.pushButton_23.clicked.connect(self.no_f)
        self.pushButton_25.clicked.connect(self.obr_s)
        self.pushButton_24.clicked.connect(self.enemy_money)
        self.pushButton_22.clicked.connect(self.trigger_b)



    # binds_tab
    @QtCore.pyqtSlot()
    def move_tab_1(self):
        self.tabWidget.setCurrentIndex(0)
    @QtCore.pyqtSlot()
    def move_tab_2(self):
        self.tabWidget.setCurrentIndex(1)

    @QtCore.pyqtSlot()
    def move_tab_3(self):
        self.tabWidget.setCurrentIndex(2)

    @QtCore.pyqtSlot()
    def move_tab_4(self):
        self.tabWidget.setCurrentIndex(3)

    @QtCore.pyqtSlot()
    def move_tab_5(self):
        self.tabWidget.setCurrentIndex(4)


    def BHOP(self):
        if self.checkBox.isChecked():
                appdata_p = os.environ['AppData']
                file = '%s\\CheatX\\cheatx-private\\settings\\b\\tr.cfg' % (appdata_p)
                check_1 = os.path.isfile(file)
                print(check_1)
                if check_1 == True:
                    self.pushButton_21.setText("ВКЛЮЧИТЬ")
                    os.remove(file)
                elif check_1 == False:
                    open(file, 'w')
                    self.pushButton_21.setText("ВЫКЛЮЧИТЬ")
                    start_bhop_checked()

                print("is checked")


        elif not self.checkBox.isChecked():
                print("not checked")

                appdata_p = os.environ['AppData']
                file = '%s\\CheatX\\cheatx-private\\settings\\b\\tr.cfg' % (appdata_p)
                check_1 = os.path.isfile(file)
                print(check_1)
                if check_1 == True:
                    self.pushButton_21.setText("ВКЛЮЧИТЬ")
                    os.remove(file)
                elif check_1 == False:
                    start_bhop_not_checked()
                    open(file, 'w')
                    self.pushButton_21.setText("ВЫКЛЮЧИТЬ")


                print("is checked")

    def esp_box(self):
        file = '%s\\CheatX\\cheatx-private\\settings\\eb\\tr.cfg' % (appdata_p)
        check_1 = os.path.isfile(file)
        file_eh = '%s\\CheatX\\cheatx-private\\settings\\eh\\tr.cfg' % (appdata_p)
        check_2_eh = os.path.isfile(file_eh)
        if check_2_eh == True:
            if check_1 == True:
                self.pushButton_3.setText("ВКЛЮЧИТЬ")
                os.remove(file)
            elif check_1 == False:
                open(file, 'w')
                self.pushButton_3.setText("ВЫКЛЮЧИТЬ")
        elif check_2_eh == False:
            if check_1 == True:
                self.pushButton_3.setText("ВКЛЮЧИТЬ")
                os.remove(file)
            elif check_1 == False:
                open(file, 'w')
                self.pushButton_3.setText("ВЫКЛЮЧИТЬ")
                esp_box1()
    def esp_hpp(self):
        file = '%s\\CheatX\\cheatx-private\\settings\\eh\\tr.cfg' % (appdata_p)
        file_eb = '%s\\CheatX\\cheatx-private\\settings\\eb\\tr.cfg' % (appdata_p)
        check_2_eb = os.path.isfile(file_eb)
        check_1 = os.path.isfile(file)
        if check_2_eb == True:
            if check_1 == True:
                self.pushButton_28.setText("ВКЛЮЧИТЬ")
                os.remove(file)
            elif check_1 == False:
                open(file, 'w')
                self.pushButton_28.setText("ВЫКЛЮЧИТЬ")
        elif check_2_eb == False:
            if check_1 == True:
                self.pushButton_28.setText("ВКЛЮЧИТЬ")
                os.remove(file)
            elif check_1 == False:
                open(file, 'w')
                self.pushButton_28.setText("ВЫКЛЮЧИТЬ")
                esp_box1()

    def esp_nm(self):
        file = '%s\\CheatX\\cheatx-private\\settings\\nm\\tr.cfg' % (appdata_p)
        file_eb = '%s\\CheatX\\cheatx-private\\settings\\eb\\tr.cfg' % (appdata_p)
        file_eh = '%s\\CheatX\\cheatx-private\\settings\\eh\\tr.cfg' % (appdata_p)
        check_2_eh = os.path.isfile(file_eh)
        check_2_eb = os.path.isfile(file_eb)
        check_1 = os.path.isfile(file)
        if check_2_eb == True or check_2_eh == True:
            if check_1 == True:
                self.pushButton_27.setText("ВКЛЮЧИТЬ")
                os.remove(file)
            elif check_1 == False:
                open(file, 'w')
                self.pushButton_27.setText("ВЫКЛЮЧИТЬ")
        elif check_2_eb == False and check_2_eh == True:
            if check_1 == True:
                self.pushButton_27.setText("ВКЛЮЧИТЬ")
                os.remove(file)
            elif check_1 == False:
                open(file, 'w')
                self.pushButton_27.setText("ВЫКЛЮЧИТЬ")
                esp_box1()
    def scs(self):
        file = '%s\\CheatX\\cheatx-private\\settings\\sc\\tr.cfg' % (appdata_p)
        value_slider = self.verticalSlider.value()
        value_slider = str(value_slider)
        file_v = '%s\\CheatX\\cheatx-private\\settings\\sc\\v.cfg' % (appdata_p)
        check_1 = os.path.isfile(file)
        check_v = os.path.isfile(file_v)
        if check_v == True:
            os.remove(file_v)
            fil = open(file_v, 'w')
            fil.write(value_slider)
        elif check_v == False:
            fil = open(file_v, 'w')
            fil.write(value_slider)
        if check_1 == True:
            self.pushButton_31.setText("ВКЛЮЧИТЬ")
            os.remove(file)
            start_sc()
        elif check_1 == False:
            open(file, 'w')
            self.pushButton_31.setText("ВЫКЛЮЧИТЬ")
            start_sc()

    def lines(self):
        file = '%s\\CheatX\\cheatx-private\\settings\\l\\tr.cfg' % (appdata_p)
        file_eb = '%s\\CheatX\\cheatx-private\\settings\\eb\\tr.cfg' % (appdata_p)
        file_eh = '%s\\CheatX\\cheatx-private\\settings\\eh\\tr.cfg' % (appdata_p)
        check_2_eb = os.path.isfile(file_eb)
        check_2_eh = os.path.isfile(file_eh)
        check_1 = os.path.isfile(file)
        if check_2_eb == True or check_2_eh == True:
            if check_1 == True:
                self.pushButton_2.setText("ВКЛЮЧИТЬ")
                os.remove(file)
            elif check_1 == False:
                open(file, 'w')
                self.pushButton_2.setText("ВЫКЛЮЧИТЬ")
        elif check_2_eb == False and check_2_eh == False:
            if check_1 == True:
                self.pushButton_2.setText("ВКЛЮЧИТЬ")
                os.remove(file)
            elif check_1 == False:
                open(file, 'w')
                self.pushButton_2.setText("ВЫКЛЮЧИТЬ")
                esp_box1()

    def obh(self):
        file = '%s\\CheatX\\cheatx-private\\settings\\w\\tr.cfg' % (appdata_p)
        check_1 = os.path.isfile(file)
        if check_1 == True:
            self.pushButton_37.setText("ВКЛЮЧИТЬ")
            os.remove(file)
            obwh()
        elif check_1 == False:
            open(file, 'w')
            self.pushButton_37.setText("ВЫКЛЮЧИТЬ")
            obwh()

    def no_f(self):
        file = '%s\\CheatX\\cheatx-private\\settings\\n\\tr.cfg' % (appdata_p)
        check_1 = os.path.isfile(file)
        if check_1 == True:
            self.pushButton_23.setText("ВКЛЮЧИТЬ")
            os.remove(file)
            main()
        elif check_1 == False:
            open(file, 'w')
            self.pushButton_23.setText("ВЫКЛЮЧИТЬ")
            main()

    def obr_s(self):
        file = '%s\\CheatX\\cheatx-private\\settings\\br\\tr.cfg' % (appdata_p)
        check_1 = os.path.isfile(file)
        if check_1 == True:
            self.pushButton_25.setText("ВКЛЮЧИТЬ")
            os.remove(file)
            obr()
        elif check_1 == False:
            open(file, 'w')
            self.pushButton_25.setText("ВЫКЛЮЧИТЬ")
            obr()

    def enemy_money(self):
        file = '%s\\CheatX\\cheatx-private\\settings\\mn\\tr.cfg' % (appdata_p)
        check_1 = os.path.isfile(file)
        if check_1 == True:
            self.pushButton_24.setText("ВКЛЮЧИТЬ")
            os.remove(file)
            money_enemys()
        elif check_1 == False:
            open(file, 'w')
            self.pushButton_24.setText("ВЫКЛЮЧИТЬ")
            money_enemys()

    def trigger_b(self):
        key = self.comboBox.currentText()
        print(key)
        trig_key = open('%s\\CheatX\\cheatx-private\\settings\\t_k.cfg' % (appdata_p), 'w')
        trig_key.write(key)
        trig_key.close()

        file = '%s\\CheatX\\cheatx-private\\settings\\t\\tr.cfg' % (appdata_p)
        check_1 = os.path.isfile(file)
        if check_1 == True:
            self.pushButton_22.setText("ВКЛЮЧИТЬ")
            os.remove(file)
            start_trigger()
        elif check_1 == False:
            open(file, 'w')
            self.pushButton_22.setText("ВЫКЛЮЧИТЬ")
            start_trigger()




def authorisation():
    from wmi import WMI
    import socket
    file_auth = '%s\\CheatX\\login.txt' % appdata_p
    check_f = os.path.isfile(file_auth)
    if check_f == True:
        hwid = WMI().Win32_ComputerSystemProduct()[0].UUID
        print(hwid)

        f = open(file_auth, 'r').read()
        read = f.split(' ')
        user_a = read[0]
        password_a = read[1]
        hwid_a = read[2]
        userr = {'user': '%s %s %s' % (user_a, password_a, hwid_a)}
        user = userr['user']
        print(userr["user"])

        rrr = requests.get('https://raw.githubusercontent.com/hohopro35/ch/main/host_ip')
        host_ip = rrr.text
        ip = '192.168.0.61'#host_ip.replace('\n', '')
        rrrr = requests.get('https://raw.githubusercontent.com/hohopro35/ch/main/host_port')
        host_port = rrrr.text
        port = 49847#int(host_port.replace('\n', ''))

        client_sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock2.connect((ip, port))
        client_sock2.send(user.encode('utf8'))
        data2 = client_sock2.recv(1024)
        client_sock2.close()
        if data2.decode('utf8') == "True":
            import sys
            cheat_files()
            app = QtWidgets.QApplication(sys.argv)
            w = MainWindow()
            w.show()
            print("Starting cheat...")
            sys.exit(app.exec_())
        print(data2.decode('utf8'))

    elif check_f == False:
        link_install = requests.get('https://raw.githubusercontent.com/hohopro35/ch/main/unstall_donwload_link')
        link = link_install.text
        p = link.replace('\n', '')
        r = requests.get(p, allow_redirects=True)
        filename = p.split('/')[-1]
        open(filename, "wb").write(r.content)
        while True:
            chhh = os.path.isfile(filename)
            print(chhh)
            if chhh == True:
                break
            sleep(1)
            print(1)
        os.system('start %s' % filename)
        exit(1)



if __name__ == "__main__":
    authorisation()
    import sys

    cheat_files()
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
