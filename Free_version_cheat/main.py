from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog, QComboBox
from PyQt5.QtGui import QFontDatabase

import os
import shutil
from random import choice
from string import ascii_uppercase
import matplotlib.colors as colors
import os
from cheats import *
from bhop import *
from onebytewallhack import *
from rcs import *
from no_flash import *
from onebyteradar import *
from onebyte_money import *
from trigger_bot import *



# имена фейк файлов для защиты от VAC
rnd_text_name_file1_cheatx_free = ''.join(choice(ascii_uppercase) for e in range(30))
rnd_text_name_file2_cheatx_free = ''.join(choice(ascii_uppercase) for s in range(30))
# текст в фейк файлах
rnd_text_file1_cheatx_free = ''.join(choice(ascii_uppercase) for f in range(3000))
rnd_text_file2_cheatx_free = ''.join(choice(ascii_uppercase) for o in range(3000))


# settings file name




def cheat_files():
    appdata_p = os.environ['AppData']
    folder = '%s\\CheatX' % (appdata_p)
    check_folder = os.path.isdir(folder)
    if check_folder == True:
        print(check_folder)
        shutil.rmtree('%s\\CheatX' % (appdata_p), ignore_errors=True)
        os.mkdir('%s\\CheatX' % (appdata_p))
        os.mkdir('%s\\CheatX\\cheatx-free' % (appdata_p))
        os.mkdir('%s\\CheatX\\cheatx-free\\settings' % (appdata_p))
        # bunnyhop
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\b' % (appdata_p))
        # esp
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\e' % (appdata_p))
        # onebyte_wh
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\w' % (appdata_p))
        # rcs
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\r' % (appdata_p))
        # no flash
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\n' % (appdata_p))
        # onebyte_radar
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\br' % (appdata_p))
        # onebyte_money
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\mn' % (appdata_p))
        # trigger_bot
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\t' % (appdata_p))


        file1_av = open('%s\\CheatX\\cheatx-free\\%s' % (appdata_p, rnd_text_name_file1_cheatx_free), 'w')
        file1_av.write(rnd_text_file1_cheatx_free)
        file1_av.close()
        file2_av = open('%s\\CheatX\\cheatx-free\\settings\\%s' % (appdata_p, rnd_text_name_file2_cheatx_free), 'w')
        file2_av.write(rnd_text_file2_cheatx_free)
        file2_av.close()
    elif check_folder == False:
        os.mkdir('%s\\CheatX' % (appdata_p))
        os.mkdir('%s\\CheatX\\cheatx-free' % (appdata_p))
        os.mkdir('%s\\CheatX\\cheatx-free\\settings' % (appdata_p))
        # bunnyhop
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\b' % (appdata_p))
        # esp
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\e' % (appdata_p))
        # onebyte_wh
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\w' % (appdata_p))
        # rcs
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\r' % (appdata_p))
        # no flash
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\n' % (appdata_p))
        # onebyte_radar
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\br' % (appdata_p))
        # onebyte_money
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\mn' % (appdata_p))
        # trigger_bot
        os.mkdir('%s\\CheatX\\cheatx-free\\settings\\t' % (appdata_p))


        file1_av = open('%s\\CheatX\\cheatx-free\\%s' % (appdata_p, rnd_text_name_file1_cheatx_free), 'w')
        file1_av.write(rnd_text_file1_cheatx_free)
        file1_av.close()
        file2_av = open('%s\\CheatX\\cheatx-free\\settings\\%s' % (appdata_p, rnd_text_name_file2_cheatx_free), 'w')
        file2_av.write(rnd_text_file2_cheatx_free)
        file2_av.close()

    else:
        BrokenPipeError


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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
        self.pushButton_5.setGeometry(QtCore.QRect(0, 70, 164, 33))
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
)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(164, 70, 164, 33))
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
)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(328, 70, 164, 33))
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
)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setGeometry(QtCore.QRect(492, 70, 164, 33))
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
)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(266, 19, 126, 42))
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
        self.label_5.setGeometry(QtCore.QRect(43, 211, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #fafaea;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(43, 290, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #fafaea;")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(451, 208, 30, 30))
        self.pushButton.setStyleSheet("border-radius: 15px;\n"
"background: url(C:/Users/stvin/PycharmProjects/PyQt_Cheat/ba.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(519, 205, 107, 34))
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
        self.pushButton_3.setGeometry(QtCore.QRect(519, 284, 107, 34))
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
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 70, 164, 33))
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
)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(164, 70, 164, 33))
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
)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(328, 70, 164, 33))
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
)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_12.setGeometry(QtCore.QRect(492, 70, 164, 33))
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
)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(266, 19, 126, 42))
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
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(266, 19, 126, 42))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #FF5D02;\n"
"")
        self.label_3.setObjectName("label_3")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 70, 164, 33))
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
)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_14.setGeometry(QtCore.QRect(164, 70, 164, 33))
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
)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_15.setGeometry(QtCore.QRect(328, 70, 164, 33))
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
)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_16.setGeometry(QtCore.QRect(492, 70, 164, 33))
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
)
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
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(266, 19, 126, 42))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #FF5D02;\n"
"")
        self.label_4.setObjectName("label_4")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_17.setGeometry(QtCore.QRect(0, 70, 164, 33))
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
)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_18.setGeometry(QtCore.QRect(164, 70, 164, 33))
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
)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_19.setGeometry(QtCore.QRect(328, 70, 164, 33))
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
)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_20.setGeometry(QtCore.QRect(492, 70, 164, 33))
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
)
        self.pushButton_20.setObjectName("pushButton_20")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(41, 162, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #fafaea;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(41, 235, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #fafaea;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(41, 302, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #fafaea;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(41, 369, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: #fafaea;")
        self.label_13.setObjectName("label_13")
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_22.setGeometry(QtCore.QRect(519, 162, 107, 34))
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
        self.pushButton_23.setGeometry(QtCore.QRect(519, 230, 107, 34))
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
        self.pushButton_24.setGeometry(QtCore.QRect(519, 298, 107, 34))
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
        self.pushButton_25.setGeometry(QtCore.QRect(519, 367, 107, 34))
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
        self.tabWidget.addTab(self.tab_4, "")
        self.comboBox = QtWidgets.QComboBox(self.tab_4)
        self.comboBox.setGeometry(QtCore.QRect(440, 168, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CheatX - Free"))
        self.pushButton_5.setText(_translate("MainWindow", "ESP"))
        self.pushButton_6.setText(_translate("MainWindow", "RCS"))
        self.pushButton_7.setText(_translate("MainWindow", "BHOP"))
        self.pushButton_8.setText(_translate("MainWindow", "Other"))
        self.label_2.setText(_translate("MainWindow", "CheatX"))
        self.label_5.setText(_translate("MainWindow", "Esp - обводка врагов"))
        self.label_6.setText(_translate("MainWindow", "OneByteWallHack"))
        self.pushButton_2.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.pushButton_3.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "esp"))
        self.pushButton_9.setText(_translate("MainWindow", "ESP"))
        self.pushButton_10.setText(_translate("MainWindow", "RCS"))
        self.pushButton_11.setText(_translate("MainWindow", "BHOP"))
        self.pushButton_12.setText(_translate("MainWindow", "Other"))
        self.label.setText(_translate("MainWindow", "CheatX"))
        self.label_7.setText(_translate("MainWindow", "RCS - полный контроль отдачи всех"))
        self.label_8.setText(_translate("MainWindow", "автоматических оружий. "))
        self.pushButton_4.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "rcs"))
        self.label_3.setText(_translate("MainWindow", "CheatX"))
        self.pushButton_13.setText(_translate("MainWindow", "ESP"))
        self.pushButton_14.setText(_translate("MainWindow", "RCS"))
        self.pushButton_15.setText(_translate("MainWindow", "BHOP"))
        self.pushButton_16.setText(_translate("MainWindow", "Other"))
        self.label_9.setText(_translate("MainWindow", "BHOP  - Автоматическая распрыжка"))
        self.pushButton_21.setText(_translate("MainWindow", "ВКЛЮЧИТЬ"))
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
        self.comboBox.setItemText(0, _translate("MainWindow", "shift"))
        self.comboBox.setItemText(1, _translate("MainWindow", "alt"))
        self.comboBox.setItemText(2, _translate("MainWindow", "CapsLock"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "other"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.move_tab_1)
        self.pushButton_6.clicked.connect(self.move_tab_2)
        self.pushButton_7.clicked.connect(self.move_tab_3)
        self.pushButton_8.clicked.connect(self.move_tab_4)
        self.pushButton_9.clicked.connect(self.move_tab_1)
        self.pushButton_10.clicked.connect(self.move_tab_2)
        self.pushButton_11.clicked.connect(self.move_tab_3)
        self.pushButton_12.clicked.connect(self.move_tab_4)
        self.pushButton_13.clicked.connect(self.move_tab_1)
        self.pushButton_14.clicked.connect(self.move_tab_2)
        self.pushButton_15.clicked.connect(self.move_tab_3)
        self.pushButton_16.clicked.connect(self.move_tab_4)
        self.pushButton_17.clicked.connect(self.move_tab_1)
        self.pushButton_18.clicked.connect(self.move_tab_2)
        self.pushButton_19.clicked.connect(self.move_tab_3)
        self.pushButton_20.clicked.connect(self.move_tab_4)

        self.pushButton.clicked.connect(color_choose)
        self.pushButton_2.clicked.connect(self.esp_s)
        self.pushButton_21.clicked.connect(self.BHOP)
        self.pushButton_3.clicked.connect(self.obh)
        self.pushButton_4.clicked.connect(self.rcs_s)
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
    def BHOP(self):
        if self.checkBox.isChecked():
                appdata_p = os.environ['AppData']
                file = '%s\\CheatX\\cheatx-free\\settings\\b\\tr.cfg' % (appdata_p)
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
                file = '%s\\CheatX\\cheatx-free\\settings\\b\\tr.cfg' % (appdata_p)
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

    def esp_s(self):
        file = '%s\\CheatX\\cheatx-free\\settings\\e\\tr.cfg' % (appdata_p)
        check_1 = os.path.isfile(file)
        if check_1 == True:
            self.pushButton_2.setText("ВКЛЮЧИТЬ")
            os.remove(file)
        elif check_1 == False:
            open(file, 'w')
            self.pushButton_2.setText("ВЫКЛЮЧИТЬ")
            start_esp()
    def obh(self):
        file = '%s\\CheatX\\cheatx-free\\settings\\w\\tr.cfg' % (appdata_p)
        check_1 = os.path.isfile(file)
        if check_1 == True:
            self.pushButton_3.setText("ВКЛЮЧИТЬ")
            os.remove(file)
            obwh()
        elif check_1 == False:
            open(file, 'w')
            self.pushButton_3.setText("ВЫКЛЮЧИТЬ")
            obwh()
    def rcs_s(self):
        file = '%s\\CheatX\\cheatx-free\\settings\\r\\tr.cfg' % (appdata_p)
        check_1 = os.path.isfile(file)
        if check_1 == True:
            self.pushButton_4.setText("ВКЛЮЧИТЬ")
            os.remove(file)
        elif check_1 == False:
            open(file, 'w')
            self.pushButton_4.setText("ВЫКЛЮЧИТЬ")
            start_rcs()

    def no_f(self):
        file = '%s\\CheatX\\cheatx-free\\settings\\n\\tr.cfg' % (appdata_p)
        check_1 = os.path.isfile(file)
        if check_1 == True:
            self.pushButton_23.setText("ВКЛЮЧИТЬ")
            os.remove(file)
            start_no_flash()
        elif check_1 == False:
            open(file, 'w')
            self.pushButton_23.setText("ВЫКЛЮЧИТЬ")
            start_no_flash()

    def obr_s(self):
        file = '%s\\CheatX\\cheatx-free\\settings\\br\\tr.cfg' % (appdata_p)
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
        file = '%s\\CheatX\\cheatx-free\\settings\\mn\\tr.cfg' % (appdata_p)
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
        trig_key = open('%s\\CheatX\\cheatx-free\\settings\\t_k.cfg' % (appdata_p), 'w')
        trig_key.write(key)
        trig_key.close()

        file = '%s\\CheatX\\cheatx-free\\settings\\t\\tr.cfg' % (appdata_p)
        check_1 = os.path.isfile(file)
        if check_1 == True:
            self.pushButton_22.setText("ВКЛЮЧИТЬ")
            os.remove(file)
            start_trigger()
        elif check_1 == False:
            open(file, 'w')
            self.pushButton_22.setText("ВЫКЛЮЧИТЬ")
            start_trigger()




if __name__ == "__main__":
    import sys
    cheat_files()
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

