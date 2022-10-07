# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windGXzdF.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QDoubleSpinBox,
                               QFrame, QGroupBox, QHBoxLayout, QLabel,
                               QListWidget, QProgressBar,
                               QPushButton, QSizePolicy, QSlider, QSpacerItem,
                               QSpinBox, QSplitter, QVBoxLayout, QWidget)

from MouseLabel import Label_click_Mouse


class Ui_mainWindow(object):
    """
    """

    def __init__(self):
        self.centralwidget = None
        self.verticalLayout_2 = None
        self.groupBox_18 = None
        self.verticalLayout_6 = None
        self.groupBox = None
        self.horizontalLayout = None
        self.label_4 = None
        self.horizontalSpacer = None
        self.horizontalLayout_5 = None
        self.minButton = None
        self.maxButton = None
        self.closeButton = None
        self.horizontalLayout_7 = None
        self.groupBox_8 = None
        self.verticalLayout_8 = None
        self.groupBox_2 = None
        self.horizontalLayout_35 = None
        self.label_5 = None
        self.label_27 = None
        self.horizontalSpacer_13 = None
        self.horizontalLayout_2 = None
        self.label_3 = None
        self.comboBox = None
        self.horizontalLayout_9 = None
        self.label_10 = None
        self.horizontalLayout_11 = None
        self.groupBox_5 = None
        self.horizontalLayout_8 = None
        self.fileButton = None
        self.cameraButton = None
        self.rtspButton = None
        self.verticalLayout_3 = None
        self.label_2 = None
        self.horizontalLayout_4 = None
        self.iouSpinBox = None
        self.iouSlider = None
        self.verticalLayout = None
        self.label = None
        self.horizontalLayout_3 = None
        self.confSpinBox = None
        self.confSlider = None
        self.verticalLayout_5 = None
        self.horizontalLayout_14 = None
        self.label_8 = None
        self.checkBox = None
        self.horizontalLayout_13 = None
        self.rateSpinBox = None
        self.rateSlider = None
        self.verticalLayout_7 = None
        self.label_11 = None
        self.resultWidget = None
        self.groupBox_201 = None
        self.verticalLayout_4 = None
        self.groupBox_3 = None
        self.horizontalLayout_6 = None
        self.label_6 = None
        self.label_28 = None
        self.horizontalSpacer_14 = None
        self.fps_label = None
        self.splitter = None
        self.out_video = None
        self.horizontalLayout_12 = None
        self.runButton = None
        self.progressBar = None
        self.stopButton = None
        self.groupBox_4 = None
        self.horizontalLayout_10 = None
        self.statistic_label = None

    def setupUi(self, mainWindow):
        """
        """
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1394, 762)
        mainWindow.setMouseTracking(True)
        icon = QIcon()
        icon.addFile(u":/img/icon/\u56fe\u72471.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"#groupBox_18{\n"
                                         "border: 0px solid #42adff;}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_18 = QGroupBox(self.centralwidget)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setStyleSheet(u"#groupBox_18{border-image:url(:/img/icon/\u80cc\u666f.png);\n"
                                       "border: 0px solid #42adff;}")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.groupBox_18)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 45))
        self.groupBox.setMaximumSize(QSize(16777215, 45))
        self.groupBox.setStyleSheet(u"#groupBox{\n"
                                    "\n"
                                    "border: 0px solid #42adff;\n"
                                    "border-left: 0px solid rgba(29, 83, 185, 255);\n"
                                    "border-right: 0px solid rgba(29, 83, 185, 255);\n"
                                    "border-bottom: 1px solid rgba(200, 200, 200,100);\n"
                                    "border-radius:0px;}")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel\n"
                                   "{\n"
                                   "	font-size: 24px;\n"
                                   "	font-family: \"Microsoft YaHei\";\n"
                                   "	font-weight: bold;\n"
                                   " 		border-radius:9px;\n"
                                   "		background:rgba(66, 195, 255, 0);\n"
                                   "color: rgb(218, 218, 218);\n"
                                   "}\n"
                                   "")

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.minButton = QPushButton(self.groupBox)
        self.minButton.setObjectName(u"minButton")
        self.minButton.setMinimumSize(QSize(50, 28))
        self.minButton.setMaximumSize(QSize(50, 28))
        self.minButton.setStyleSheet(u"QPushButton {\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 0px;\n"
                                     "background-color: rgba(223, 223, 223, 0);}\n"
                                     "QPushButton::focus{outline: none;}\n"
                                     "QPushButton::hover {\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 0px;\n"
                                     "background-color: rgba(223, 223, 223, 150);}")
        icon1 = QIcon()
        icon1.addFile(u":/img/icon/\u6700\u5c0f\u5316.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minButton.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.minButton)

        self.maxButton = QPushButton(self.groupBox)
        self.maxButton.setObjectName(u"maxButton")
        self.maxButton.setMinimumSize(QSize(50, 28))
        self.maxButton.setMaximumSize(QSize(50, 28))
        self.maxButton.setStyleSheet(u"QPushButton {\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 0px;\n"
                                     "background-color: rgba(223, 223, 223, 0);}\n"
                                     "QPushButton::focus{outline: none;}\n"
                                     "QPushButton::hover {\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 0px;\n"
                                     "background-color: rgba(223, 223, 223, 150);}")
        icon2 = QIcon()
        icon2.addFile(u":/img/icon/\u6b63\u65b9\u5f62.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/img/icon/\u8fd8\u539f.png", QSize(), QIcon.Active, QIcon.On)
        icon2.addFile(u":/img/icon/\u8fd8\u539f.png", QSize(), QIcon.Selected, QIcon.On)
        self.maxButton.setIcon(icon2)
        self.maxButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.maxButton)

        self.closeButton = QPushButton(self.groupBox)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(50, 28))
        self.closeButton.setMaximumSize(QSize(50, 28))
        self.closeButton.setStyleSheet(u"QPushButton {\n"
                                       "border-style: solid;\n"
                                       "border-width: 0px;\n"
                                       "border-radius: 0px;\n"
                                       "background-color: rgba(223, 223, 223, 0);}\n"
                                       "QPushButton::focus{outline: none;}\n"
                                       "QPushButton::hover {\n"
                                       "border-style: solid;\n"
                                       "border-width: 0px;\n"
                                       "border-radius: 0px;\n"
                                       "background-color: rgba(223, 223, 223, 150);}")
        icon3 = QIcon()
        icon3.addFile(u":/img/icon/\u5173\u95ed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.closeButton)

        self.horizontalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout_6.addWidget(self.groupBox)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_8 = QGroupBox(self.groupBox_18)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(320, 0))
        self.groupBox_8.setMaximumSize(QSize(320, 16777215))
        self.groupBox_8.setStyleSheet(u"#groupBox_8{\n"
                                      "border: 0px solid #42adff;\n"
                                      "background-color:rgba(0, 0, 0, 30);\n"
                                      "border-radius:0px;}\n"
                                      "")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_8.setSpacing(11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_2 = QGroupBox(self.groupBox_8)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 42))
        self.groupBox_2.setMaximumSize(QSize(16777215, 42))
        self.groupBox_2.setStyleSheet(u"#groupBox_2{\n"
                                      "border: 0px solid #42adff;\n"
                                      "border-radius:0px;}")
        self.horizontalLayout_35 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(2, 0, 0, 0)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setStyleSheet(u"QLabel\n"
                                   "{\n"
                                   "	font: 11pt \"\u9ed1\u4f53\";\n"
                                   "	font-size: 22px;\n"
                                   "	font-family: \"Microsoft YaHei\";\n"
                                   "	font-weight: bold;\n"
                                   " 		border-radius:9px;\n"
                                   "		background:rgba(66, 195, 255, 0);\n"
                                   "color: rgb(218, 218, 218);\n"
                                   "\n"
                                   "}\n"
                                   "")

        self.horizontalLayout_35.addWidget(self.label_5)

        self.label_27 = QLabel(self.groupBox_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 0))
        self.label_27.setMaximumSize(QSize(16777215, 40))
        self.label_27.setStyleSheet(u"QLabel{\n"
                                    "	font-family: \"DejaVu Sans Mono\";\n"
                                    "	font-size: 15px;\n"
                                    "	color: #e8e8e8;}")

        self.horizontalLayout_35.addWidget(self.label_27)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_13)

        self.verticalLayout_8.addWidget(self.groupBox_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.groupBox_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 35))
        self.label_3.setMaximumSize(QSize(80, 16777215))
        self.label_3.setStyleSheet(u"QLabel\n"
                                   "{\n"
                                   "	font: 11pt \"\u9ed1\u4f53\";\n"
                                   "	font-size: 18px;\n"
                                   "	font-family: \"Microsoft YaHei\";\n"
                                   "	font-weight: bold;\n"
                                   " 		border-radius:9px;\n"
                                   "		background:rgba(66, 195, 255, 0);\n"
                                   "color: rgb(218, 218, 218);\n"
                                   "}\n"
                                   "")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.comboBox = QComboBox(self.groupBox_8)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 35))
        self.comboBox.setStyleSheet(u"QComboBox QAbstractItemView {\n"
                                    "font-family: \"Microsoft YaHei\";\n"
                                    "font-size: 16px;\n"
                                    "background:rgba(200, 200, 200,150);\n"
                                    "selection-background-color: rgba(200, 200, 200,50);\n"
                                    "color: rgb(218, 218, 218);\n"
                                    "outline:none;\n"
                                    "border:none;}\n"
                                    "QComboBox{\n"
                                    "font-family: \"Microsoft YaHei\";\n"
                                    "font-size: 16px;\n"
                                    "color: rgb(218, 218, 218);\n"
                                    "border-width:0px;\n"
                                    "border-color:white;\n"
                                    "border-style:solid;\n"
                                    "background-color: rgba(200, 200, 200,0);}\n"
                                    "\n"
                                    "QComboBox::drop-down {\n"
                                    "margin-top:8;\n"
                                    "height:20;\n"
                                    "background:rgba(255,255,255,0);\n"
                                    "border-image: url(:/img/icon/\u4e0b\u62c9_\u767d\u8272.png);\n"
                                    "}\n"
                                    "")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.groupBox_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(80, 16777215))
        self.label_10.setStyleSheet(u"QLabel\n"
                                    "{\n"
                                    "	font-size: 18px;\n"
                                    "	font-family: \"Microsoft YaHei\";\n"
                                    "	font-weight: bold;\n"
                                    " 		border-radius:9px;\n"
                                    "		background:rgba(66, 195, 255, 0);\n"
                                    "color: rgb(218, 218, 218);\n"
                                    "}\n"
                                    "")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.groupBox_5 = QGroupBox(self.groupBox_8)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"#groupBox_5{\n"
                                      "background-color: rgba(48,148,243,0);\n"
                                      "border: 0px solid #42adff;\n"
                                      "border-left: 0px solid #d9d9d9;\n"
                                      "border-right: 0px solid rgba(29, 83, 185, 255);\n"
                                      "border-radius:0px;}")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.fileButton = QPushButton(self.groupBox_5)
        self.fileButton.setObjectName(u"fileButton")
        self.fileButton.setMinimumSize(QSize(55, 28))
        self.fileButton.setMaximumSize(QSize(16777215, 28))
        self.fileButton.setStyleSheet(u"QPushButton{font-family: \"Microsoft YaHei\";\n"
                                      "font-size: 14px;\n"
                                      "font-weight: bold;\n"
                                      "color:white;\n"
                                      "text-align: center center;\n"
                                      "padding-left: 5px;\n"
                                      "padding-right: 5px;\n"
                                      "padding-top: 4px;\n"
                                      "padding-bottom: 4px;\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;\n"
                                      "border-color: rgba(255, 255, 255, 255);\n"
                                      "border-radius: 3px;\n"
                                      "background-color: rgba(200, 200, 200,0);}\n"
                                      "\n"
                                      "QPushButton:focus{outline: none;}\n"
                                      "\n"
                                      "QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
                                      "                     font-size: 14px;\n"
                                      "                     font-weight: bold;\n"
                                      "                     color:rgb(200,200,200);\n"
                                      "                     text-align: center center;\n"
                                      "                     padding-left: 5px;\n"
                                      "                     padding-right: 5px;\n"
                                      "                     padding-top: 4px;\n"
                                      "                     padding-bottom: 4px;\n"
                                      "                     border-style: solid;\n"
                                      "                     border-width: 0px;\n"
                                      "                     border-color: rgba(255, 255, 255, 255);\n"
                                      ""
                                      "                     border-radius: 3px;\n"
                                      "                     background-color:  #bf513b;}\n"
                                      "\n"
                                      "QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
                                      "                     font-size: 14px;\n"
                                      "                     font-weight: bold;\n"
                                      "                     color:rgb(200,200,200);\n"
                                      "                     text-align: center center;\n"
                                      "                     padding-left: 5px;\n"
                                      "                     padding-right: 5px;\n"
                                      "                     padding-top: 4px;\n"
                                      "                     padding-bottom: 4px;\n"
                                      "                     border-style: solid;\n"
                                      "                     border-width: 0px;\n"
                                      "                     border-color: rgba(255, 255, 255, 255);\n"
                                      "                     border-radius: 3px;\n"
                                      "                     background-color:  #bf513b;}\n"
                                      "QPushButton::hover {\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;\n"
                                      "border-radius: 0px;\n"
                                      "background-color: rgba(48,148,243,80);}")
        icon4 = QIcon()
        icon4.addFile(u":/img/icon/\u6253\u5f00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fileButton.setIcon(icon4)

        self.horizontalLayout_8.addWidget(self.fileButton)

        self.cameraButton = QPushButton(self.groupBox_5)
        self.cameraButton.setObjectName(u"cameraButton")
        self.cameraButton.setMinimumSize(QSize(55, 28))
        self.cameraButton.setMaximumSize(QSize(16777215, 28))
        self.cameraButton.setStyleSheet(u"QPushButton{font-family: \"Microsoft YaHei\";\n"
                                        "font-size: 14px;\n"
                                        "font-weight: bold;\n"
                                        "color:white;\n"
                                        "text-align: center center;\n"
                                        "padding-left: 5px;\n"
                                        "padding-right: 5px;\n"
                                        "padding-top: 4px;\n"
                                        "padding-bottom: 4px;\n"
                                        "border-style: solid;\n"
                                        "border-width: 0px;\n"
                                        "border-color: rgba(255, 255, 255, 255);\n"
                                        "border-radius: 3px;\n"
                                        "background-color: rgba(48,148,243,0);}\n"
                                        "\n"
                                        "QPushButton:focus{outline: none;}\n"
                                        "\n"
                                        "QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
                                        "                     font-size: 14px;\n"
                                        "                     font-weight: bold;\n"
                                        "                     color:rgb(200,200,200);\n"
                                        "                     text-align: center center;\n"
                                        "                     padding-left: 5px;\n"
                                        "                     padding-right: 5px;\n"
                                        "                     padding-top: 4px;\n"
                                        "                     padding-bottom: 4px;\n"
                                        "                     border-style: solid;\n"
                                        "                     border-width: 0px;\n"
                                        "                     border-color: rgba(255, 255, 255, 255);\n"
                                        "   "
                                        "                  border-radius: 3px;\n"
                                        "                     background-color:  #bf513b;}\n"
                                        "\n"
                                        "QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
                                        "                     font-size: 14px;\n"
                                        "                     font-weight: bold;\n"
                                        "                     color:rgb(200,200,200);\n"
                                        "                     text-align: center center;\n"
                                        "                     padding-left: 5px;\n"
                                        "                     padding-right: 5px;\n"
                                        "                     padding-top: 4px;\n"
                                        "                     padding-bottom: 4px;\n"
                                        "                     border-style: solid;\n"
                                        "                     border-width: 0px;\n"
                                        "                     border-color: rgba(255, 255, 255, 255);\n"
                                        "                     border-radius: 3px;\n"
                                        "                     background-color:  #bf513b;}\n"
                                        "QPushButton::hover {\n"
                                        "border-style: solid;\n"
                                        "border-width: 0px;\n"
                                        "border-radius: 0px;\n"
                                        "background-color: rgba(48,148,243,80);}")
        icon5 = QIcon()
        icon5.addFile(u":/img/icon/\u6444\u50cf\u5934\u5f00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cameraButton.setIcon(icon5)

        self.horizontalLayout_8.addWidget(self.cameraButton)

        self.rtspButton = QPushButton(self.groupBox_5)
        self.rtspButton.setObjectName(u"rtspButton")
        self.rtspButton.setMinimumSize(QSize(55, 28))
        self.rtspButton.setMaximumSize(QSize(16777215, 28))
        self.rtspButton.setStyleSheet(u"QPushButton{font-family: \"Microsoft YaHei\";\n"
                                      "font-size: 14px;\n"
                                      "font-weight: bold;\n"
                                      "color:white;\n"
                                      "text-align: center center;\n"
                                      "padding-left: 5px;\n"
                                      "padding-right: 5px;\n"
                                      "padding-top: 4px;\n"
                                      "padding-bottom: 4px;\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;\n"
                                      "border-color: rgba(255, 255, 255, 255);\n"
                                      "border-radius: 3px;\n"
                                      "background-color: rgba(48,148,243,0);}\n"
                                      "\n"
                                      "QPushButton:focus{outline: none;}\n"
                                      "\n"
                                      "QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
                                      "                     font-size: 14px;\n"
                                      "                     font-weight: bold;\n"
                                      "                     color:rgb(200,200,200);\n"
                                      "                     text-align: center center;\n"
                                      "                     padding-left: 5px;\n"
                                      "                     padding-right: 5px;\n"
                                      "                     padding-top: 4px;\n"
                                      "                     padding-bottom: 4px;\n"
                                      "                     border-style: solid;\n"
                                      "                     border-width: 0px;\n"
                                      "                     border-color: rgba(255, 255, 255, 255);\n"
                                      "   "
                                      "                  border-radius: 3px;\n"
                                      "                     background-color:  #bf513b;}\n"
                                      "\n"
                                      "QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
                                      "                     font-size: 14px;\n"
                                      "                     font-weight: bold;\n"
                                      "                     color:rgb(200,200,200);\n"
                                      "                     text-align: center center;\n"
                                      "                     padding-left: 5px;\n"
                                      "                     padding-right: 5px;\n"
                                      "                     padding-top: 4px;\n"
                                      "                     padding-bottom: 4px;\n"
                                      "                     border-style: solid;\n"
                                      "                     border-width: 0px;\n"
                                      "                     border-color: rgba(255, 255, 255, 255);\n"
                                      "                     border-radius: 3px;\n"
                                      "                     background-color:  #bf513b;}\n"
                                      "QPushButton::hover {\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;\n"
                                      "border-radius: 0px;\n"
                                      "background-color: rgba(48,148,243,80);}")
        icon6 = QIcon()
        icon6.addFile(u":/img/icon/\u5b9e\u65f6\u89c6\u9891\u6d41\u89e3\u6790.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rtspButton.setIcon(icon6)

        self.horizontalLayout_8.addWidget(self.rtspButton)

        self.horizontalLayout_11.addWidget(self.groupBox_5)

        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)

        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.groupBox_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel\n"
                                   "{\n"
                                   "	font-size: 18px;\n"
                                   "	font-family: \"Microsoft YaHei\";\n"
                                   "	font-weight: bold;\n"
                                   " 		border-radius:9px;\n"
                                   "		background:rgba(66, 195, 255, 0);\n"
                                   "color: rgb(218, 218, 218);\n"
                                   "}\n"
                                   "")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.iouSpinBox = QDoubleSpinBox(self.groupBox_8)
        self.iouSpinBox.setObjectName(u"iouSpinBox")
        self.iouSpinBox.setMinimumSize(QSize(50, 0))
        self.iouSpinBox.setMaximumSize(QSize(50, 16777215))
        self.iouSpinBox.setStyleSheet(u"QDoubleSpinBox{\n"
                                      "background:rgba(200, 200, 200,50);\n"
                                      "color:white;\n"
                                      "font-size: 14px;\n"
                                      "font-family: \"Microsoft YaHei UI\";\n"
                                      "border-style: solid;\n"
                                      "border-width: 1px;\n"
                                      "border-color: rgba(200, 200, 200,100);\n"
                                      "border-radius: 3px;}\n"
                                      "\n"
                                      "QDoubleSpinBox::down-button{\n"
                                      "background:rgba(200, 200, 200,0);\n"
                                      "border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
                                      "QDoubleSpinBox::down-button::hover{\n"
                                      "background:rgba(200, 200, 200,100);\n"
                                      "border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
                                      "\n"
                                      "QDoubleSpinBox::up-button{\n"
                                      "background:rgba(200, 200, 200,0);\n"
                                      "border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
                                      "QDoubleSpinBox::up-button::hover{\n"
                                      "background:rgba(200, 200, 200,100);\n"
                                      "border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
                                      "")
        self.iouSpinBox.setMaximum(1.000000000000000)
        self.iouSpinBox.setSingleStep(0.010000000000000)
        self.iouSpinBox.setValue(0.450000000000000)

        self.horizontalLayout_4.addWidget(self.iouSpinBox)

        self.iouSlider = QSlider(self.groupBox_8)
        self.iouSlider.setObjectName(u"iouSlider")
        self.iouSlider.setStyleSheet(u"QSlider{\n"
                                     "border-color: #bcbcbc;\n"
                                     "color:#d9d9d9;\n"
                                     "}\n"
                                     "QSlider::groove:horizontal {                                \n"
                                     "     border: 1px solid #999999;                             \n"
                                     "     height: 3px;                                           \n"
                                     "    margin: 0px 0;                                         \n"
                                     "     left: 5px; right: 5px; \n"
                                     " }\n"
                                     "QSlider::handle:horizontal {                               \n"
                                     "     border: 0px ; \n"
                                     "     border-image: url(:/img/icon/\u5706.png);\n"
                                     "	 width:15px;\n"
                                     "     margin: -7px -7px -7px -7px;                  \n"
                                     "} \n"
                                     "QSlider::add-page:horizontal{\n"
                                     "background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9); \n"
                                     "\n"
                                     "}\n"
                                     "QSlider::sub-page:horizontal{                               \n"
                                     " background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
                                     "}")
        self.iouSlider.setMaximum(100)
        self.iouSlider.setValue(45)
        self.iouSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.iouSlider)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox_8)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel\n"
                                 "{\n"
                                 "	font-size: 18px;\n"
                                 "	font-family: \"Microsoft YaHei\";\n"
                                 "	font-weight: bold;\n"
                                 " 		border-radius:9px;\n"
                                 "		background:rgba(66, 195, 255, 0);\n"
                                 "color: rgb(218, 218, 218);\n"
                                 "}\n"
                                 "")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.confSpinBox = QDoubleSpinBox(self.groupBox_8)
        self.confSpinBox.setObjectName(u"confSpinBox")
        self.confSpinBox.setMinimumSize(QSize(50, 0))
        self.confSpinBox.setMaximumSize(QSize(50, 16777215))
        self.confSpinBox.setFocusPolicy(Qt.ClickFocus)
        self.confSpinBox.setStyleSheet(u"QDoubleSpinBox{\n"
                                       "background:rgba(200, 200, 200,50);\n"
                                       "color:white;\n"
                                       "font-size: 14px;\n"
                                       "font-family: \"Microsoft YaHei UI\";\n"
                                       "border-style: solid;\n"
                                       "border-width: 1px;\n"
                                       "border-color: rgba(200, 200, 200,100);\n"
                                       "border-radius: 3px;}\n"
                                       "\n"
                                       "QDoubleSpinBox::down-button{\n"
                                       "background:rgba(200, 200, 200,0);\n"
                                       "border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
                                       "QDoubleSpinBox::down-button::hover{\n"
                                       "background:rgba(200, 200, 200,100);\n"
                                       "border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
                                       "\n"
                                       "QDoubleSpinBox::up-button{\n"
                                       "background:rgba(200, 200, 200,0);\n"
                                       "border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
                                       "QDoubleSpinBox::up-button::hover{\n"
                                       "background:rgba(200, 200, 200,100);\n"
                                       "border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
                                       "")
        self.confSpinBox.setMaximum(1.000000000000000)
        self.confSpinBox.setSingleStep(0.010000000000000)
        self.confSpinBox.setValue(0.250000000000000)

        self.horizontalLayout_3.addWidget(self.confSpinBox)

        self.confSlider = QSlider(self.groupBox_8)
        self.confSlider.setObjectName(u"confSlider")
        self.confSlider.setStyleSheet(u"QSlider{\n"
                                      "border-color: #bcbcbc;\n"
                                      "color:#d9d9d9;\n"
                                      "}\n"
                                      "QSlider::groove:horizontal {                                \n"
                                      "     border: 1px solid #999999;                             \n"
                                      "     height: 3px;                                           \n"
                                      "    margin: 0px 0;                                         \n"
                                      "     left: 5px; right: 5px; \n"
                                      " }\n"
                                      "QSlider::handle:horizontal {                               \n"
                                      "     border: 0px ; \n"
                                      "     border-image: url(:/img/icon/\u5706.png);\n"
                                      "	 width:15px;\n"
                                      "     margin: -7px -7px -7px -7px;                  \n"
                                      "} \n"
                                      "QSlider::add-page:horizontal{\n"
                                      "background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9); \n"
                                      "\n"
                                      "}\n"
                                      "QSlider::sub-page:horizontal{                               \n"
                                      " background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
                                      "}")
        self.confSlider.setMaximum(100)
        self.confSlider.setValue(25)
        self.confSlider.setOrientation(Qt.Horizontal)
        self.confSlider.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_3.addWidget(self.confSlider)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_8 = QLabel(self.groupBox_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(80, 16777215))
        self.label_8.setStyleSheet(u"QLabel\n"
                                   "{\n"
                                   "	font-size: 18px;\n"
                                   "	font-family: \"Microsoft YaHei\";\n"
                                   "	font-weight: bold;\n"
                                   " 		border-radius:9px;\n"
                                   "		background:rgba(66, 195, 255, 0);\n"
                                   "color: rgb(218, 218, 218);\n"
                                   "}\n"
                                   "")

        self.horizontalLayout_14.addWidget(self.label_8)

        self.checkBox = QCheckBox(self.groupBox_8)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"\n"
                                    "QCheckBox\n"
                                    "{font-size: 16px;\n"
                                    "	font-family: \"Microsoft YaHei\";\n"
                                    "	font-weight: bold;\n"
                                    " 		border-radius:9px;\n"
                                    "		background:rgba(66, 195, 255, 0);\n"
                                    "color: rgb(218, 218, 218);;}\n"
                                    "\n"
                                    "QCheckBox::indicator {\n"
                                    "	width: 20px;\n"
                                    "	height: 20px;\n"
                                    "}\n"
                                    "QCheckBox::indicator:unchecked {\n"
                                    "    image: url(:/img/icon/button-off.png);\n"
                                    "}\n"
                                    "\n"
                                    "QCheckBox::indicator:checked {\n"
                                    "    \n"
                                    "    image: url(:/img/icon/button-on.png);\n"
                                    "}\n"
                                    "")
        self.checkBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.checkBox)

        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.rateSpinBox = QSpinBox(self.groupBox_8)
        self.rateSpinBox.setObjectName(u"rateSpinBox")
        self.rateSpinBox.setMinimumSize(QSize(50, 0))
        self.rateSpinBox.setMaximumSize(QSize(50, 16777215))
        self.rateSpinBox.setFocusPolicy(Qt.ClickFocus)
        self.rateSpinBox.setStyleSheet(u"QSpinBox{\n"
                                       "background:rgba(200, 200, 200,50);\n"
                                       "color:white;\n"
                                       "font-size: 14px;\n"
                                       "font-family: \"Microsoft YaHei UI\";\n"
                                       "border-style: solid;\n"
                                       "border-width: 1px;\n"
                                       "border-color: rgba(200, 200, 200,100);\n"
                                       "border-radius: 3px;}\n"
                                       "\n"
                                       "QSpinBox::down-button{\n"
                                       "background:rgba(200, 200, 200,0);\n"
                                       "border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
                                       "QDoubleSpinBox::down-button::hover{\n"
                                       "background:rgba(200, 200, 200,100);\n"
                                       "border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
                                       "\n"
                                       "QSpinBox::up-button{\n"
                                       "background:rgba(200, 200, 200,0);\n"
                                       "border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
                                       "QSpinBox::up-button::hover{\n"
                                       "background:rgba(200, 200, 200,100);\n"
                                       "border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
                                       "")
        self.rateSpinBox.setMinimum(1)
        self.rateSpinBox.setMaximum(20)
        self.rateSpinBox.setSingleStep(1)
        self.rateSpinBox.setValue(1)

        self.horizontalLayout_13.addWidget(self.rateSpinBox)

        self.rateSlider = QSlider(self.groupBox_8)
        self.rateSlider.setObjectName(u"rateSlider")
        self.rateSlider.setStyleSheet(u"QSlider{\n"
                                      "border-color: #bcbcbc;\n"
                                      "color:#d9d9d9;\n"
                                      "}\n"
                                      "QSlider::groove:horizontal {                                \n"
                                      "     border: 1px solid #999999;                             \n"
                                      "     height: 3px;                                           \n"
                                      "    margin: 0px 0;                                         \n"
                                      "     left: 5px; right: 5px; \n"
                                      " }\n"
                                      "QSlider::handle:horizontal {                               \n"
                                      "     border: 0px ; \n"
                                      "     border-image: url(:/img/icon/\u5706.png);\n"
                                      "	 width:15px;\n"
                                      "     margin: -7px -7px -7px -7px;                  \n"
                                      "} \n"
                                      "QSlider::add-page:horizontal{\n"
                                      "background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9); \n"
                                      "\n"
                                      "}\n"
                                      "QSlider::sub-page:horizontal{                               \n"
                                      " background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
                                      "}")
        self.rateSlider.setMinimum(1)
        self.rateSlider.setMaximum(20)
        self.rateSlider.setSingleStep(1)
        self.rateSlider.setPageStep(1)
        self.rateSlider.setValue(1)
        self.rateSlider.setOrientation(Qt.Horizontal)
        self.rateSlider.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_13.addWidget(self.rateSlider)

        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.groupBox_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel\n"
                                    "{\n"
                                    "	font-size: 18px;\n"
                                    "	font-family: \"Microsoft YaHei\";\n"
                                    "	font-weight: bold;\n"
                                    " 		border-radius:9px;\n"
                                    "		background:rgba(66, 195, 255, 0);\n"
                                    "color: rgb(218, 218, 218);\n"
                                    "}\n"
                                    "")

        self.verticalLayout_7.addWidget(self.label_11)

        self.resultWidget = QListWidget(self.groupBox_8)
        self.resultWidget.setObjectName(u"resultWidget")
        self.resultWidget.setStyleSheet(u"QListWidget{\n"
                                        "background-color: rgba(12, 28, 77, 0);\n"
                                        "border: 1px solid rgba(200, 200, 200,100);\n"
                                        "border-bottom: 0px solid rgba(200, 200, 200,100);\n"
                                        "border-radius:0px;\n"
                                        "font-family: \"Microsoft YaHei\";\n"
                                        "font-size: 16px;\n"
                                        "color: rgb(218, 218, 218);\n"
                                        "}\n"
                                        "")

        self.verticalLayout_7.addWidget(self.resultWidget)

        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.horizontalLayout_7.addWidget(self.groupBox_8)

        self.groupBox_201 = QGroupBox(self.groupBox_18)
        self.groupBox_201.setObjectName(u"groupBox_201")
        self.groupBox_201.setStyleSheet(u"#groupBox_201{\n"
                                        "border: 0px solid #42adff;\n"
                                        "background-color:rgba(0, 0, 0, 30);\n"
                                        "border-left: 1px solid rgba(200, 200, 200,100);\n"
                                        "border-right: 0px solid rgba(29, 83, 185, 255);\n"
                                        "border-radius:0px;}")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_201)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_3 = QGroupBox(self.groupBox_201)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 42))
        self.groupBox_3.setMaximumSize(QSize(16777215, 42))
        self.groupBox_3.setStyleSheet(u"#groupBox_3{\n"
                                      "border: 0px solid #42adff;\n"
                                      "border-radius:0px;}")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setStyleSheet(u"QLabel\n"
                                   "{\n"
                                   "	font-size: 22px;\n"
                                   "	font-family: \"Microsoft YaHei\";\n"
                                   "	font-weight: bold;\n"
                                   " 		border-radius:9px;\n"
                                   "		background:rgba(66, 195, 255, 0);\n"
                                   "color: rgb(218, 218, 218);\n"
                                   "}\n"
                                   "")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.label_28 = QLabel(self.groupBox_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 0))
        self.label_28.setMaximumSize(QSize(16777215, 40))
        self.label_28.setStyleSheet(u"QLabel{\n"
                                    "	font-family: \"DejaVu Sans Mono\";\n"
                                    "	font-size: 15px;\n"
                                    "	color: #e1e1e1;}")

        self.horizontalLayout_6.addWidget(self.label_28)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)

        self.fps_label = QLabel(self.groupBox_3)
        self.fps_label.setObjectName(u"fps_label")
        self.fps_label.setMinimumSize(QSize(100, 40))
        self.fps_label.setMaximumSize(QSize(100, 40))
        self.fps_label.setStyleSheet(u"QLabel\n"
                                     "{\n"
                                     "	font-size: 20px;\n"
                                     "	font-family: \"Microsoft YaHei\";\n"
                                     "	font-weight: bold;\n"
                                     " 		border-radius:9px;\n"
                                     "		background:rgba(66, 195, 255, 0);\n"
                                     "color: rgb(218, 218, 218);\n"
                                     "}\n"
                                     "")
        self.fps_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.fps_label)

        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.splitter = QSplitter(self.groupBox_201)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setEnabled(True)
        self.splitter.setStyleSheet(u"#splitter::handle{background: 1px solid  rgba(200, 200, 200,100);}")
        self.splitter.setFrameShape(QFrame.NoFrame)
        self.splitter.setLineWidth(10)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.out_video = Label_click_Mouse(self.splitter)
        self.out_video.setObjectName(u"out_video")
        self.out_video.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_video.sizePolicy().hasHeightForWidth())
        self.out_video.setSizePolicy(sizePolicy)
        self.out_video.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(36)
        self.out_video.setFont(font)
        self.out_video.setCursor(QCursor(Qt.ArrowCursor))
        self.out_video.setStyleSheet(u"")
        self.out_video.setScaledContents(False)
        self.out_video.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.out_video)

        self.verticalLayout_4.addWidget(self.splitter)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.runButton = QPushButton(self.groupBox_201)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setMinimumSize(QSize(40, 40))
        self.runButton.setStyleSheet(u"QPushButton {\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 0px;\n"
                                     "background-color: rgba(223, 223, 223, 0);\n"
                                     "}\n"
                                     "QPushButton::focus{outline: none;}\n"
                                     "QPushButton::hover {\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 0px;\n"
                                     "background-color: rgba(223, 223, 223, 150);}")
        icon7 = QIcon()
        icon7.addFile(u":/img/icon/\u8fd0\u884c.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/img/icon/\u6682\u505c.png", QSize(), QIcon.Normal, QIcon.On)
        icon7.addFile(u":/img/icon/\u8fd0\u884c.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon7.addFile(u":/img/icon/\u6682\u505c.png", QSize(), QIcon.Disabled, QIcon.On)
        icon7.addFile(u":/img/icon/\u8fd0\u884c.png", QSize(), QIcon.Active, QIcon.Off)
        icon7.addFile(u":/img/icon/\u6682\u505c.png", QSize(), QIcon.Active, QIcon.On)
        icon7.addFile(u":/img/icon/\u8fd0\u884c.png", QSize(), QIcon.Selected, QIcon.Off)
        icon7.addFile(u":/img/icon/\u6682\u505c.png", QSize(), QIcon.Selected, QIcon.On)
        self.runButton.setIcon(icon7)
        self.runButton.setIconSize(QSize(30, 30))
        self.runButton.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.runButton)

        self.progressBar = QProgressBar(self.groupBox_201)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 5))
        self.progressBar.setStyleSheet(
            u"QProgressBar{ color: rgb(255, 255, 255); font:12pt; border-radius:2px; text-align:center; border:none; background-color: rgba(215, 215, 215,100);} \n"
            "QProgressBar:chunk{ border-radius:0px; background: rgba(55, 55, 55, 200);}")
        self.progressBar.setMaximum(1000)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout_12.addWidget(self.progressBar)

        self.stopButton = QPushButton(self.groupBox_201)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(40, 40))
        self.stopButton.setStyleSheet(u"QPushButton {\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;\n"
                                      "border-radius: 0px;\n"
                                      "background-color: rgba(223, 223, 223, 0);\n"
                                      "}\n"
                                      "QPushButton::focus{outline: none;}\n"
                                      "QPushButton::hover {\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;\n"
                                      "border-radius: 0px;\n"
                                      "background-color: rgba(223, 223, 223, 150);}")
        icon8 = QIcon()
        icon8.addFile(u":/img/icon/\u7ec8\u6b62.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon8)
        self.stopButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_12.addWidget(self.stopButton)

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.verticalLayout_4.setStretch(1, 1)

        self.horizontalLayout_7.addWidget(self.groupBox_201)

        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.groupBox_4 = QGroupBox(self.groupBox_18)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 30))
        self.groupBox_4.setMaximumSize(QSize(16777215, 30))
        self.groupBox_4.setStyleSheet(u"#groupBox_4{\n"
                                      "border: 0px solid #42adff;\n"
                                      "background-color:rgba(0, 0, 0, 30);\n"
                                      "border-left: 0px solid rgba(29, 83, 185, 255);\n"
                                      "border-right: 0px solid rgba(29, 83, 185, 255);\n"
                                      "border-top: 1px solid rgba(200, 200, 200,100);\n"
                                      "border-radius:0px;}")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.statistic_label = QLabel(self.groupBox_4)
        self.statistic_label.setObjectName(u"statistic_label")
        self.statistic_label.setMouseTracking(False)
        self.statistic_label.setStyleSheet(u"QLabel\n"
                                           "{\n"
                                           "	font-size: 16px;\n"
                                           "	font-family: \"Microsoft YaHei\";\n"
                                           "	font-weight: light;\n"
                                           " 		border-radius:9px;\n"
                                           "		background:rgba(66, 195, 255, 0);\n"
                                           "color: rgb(218, 218, 218);\n"
                                           "}\n"
                                           "")

        self.horizontalLayout_10.addWidget(self.statistic_label)

        self.verticalLayout_6.addWidget(self.groupBox_4)

        self.verticalLayout_2.addWidget(self.groupBox_18)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)

    # setupUi

    def retranslateUi(self, mainWindow):
        """
        """
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"YOLOv5\u68c0\u6d4b\u754c\u9762", None))
        self.groupBox_18.setTitle("")
        self.groupBox.setTitle("")
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"YOLOv5\u68c0\u6d4b\u754c\u9762", None))
        self.minButton.setText("")
        self.maxButton.setText("")
        self.closeButton.setText("")
        self.groupBox_8.setTitle("")
        self.groupBox_2.setTitle("")
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"\u8bbe\u7f6e", None))
        self.label_27.setText(QCoreApplication.translate("mainWindow", u"setting", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\u6a21\u578b\u9009\u62e9", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"yolov5s.pt", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"yolov5m.pt", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"yolov5l.pt", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"yolov5x.pt", None))

        self.label_10.setText(QCoreApplication.translate("mainWindow", u"\u8f93\u5165\u9009\u62e9", None))
        self.groupBox_5.setTitle("")
        # if QT_CONFIG(tooltip)
        self.fileButton.setToolTip(QCoreApplication.translate("mainWindow", u"\u6587\u4ef6", None))
        # endif // QT_CONFIG(tooltip)
        self.fileButton.setText("")
        # if QT_CONFIG(tooltip)
        self.cameraButton.setToolTip(QCoreApplication.translate("mainWindow", u"\u76f8\u673a", None))
        # endif // QT_CONFIG(tooltip)
        self.cameraButton.setText("")
        # if QT_CONFIG(tooltip)
        self.rtspButton.setToolTip(QCoreApplication.translate("mainWindow", u"rtsp", None))
        # endif // QT_CONFIG(tooltip)
        self.rtspButton.setText("")
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"IoU", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u7f6e\u4fe1\u5ea6", None))
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"\u5e27\u95f4\u5ef6\u65f6", None))
        self.checkBox.setText(QCoreApplication.translate("mainWindow", u"\u542f\u7528", None))
        self.label_11.setText(QCoreApplication.translate("mainWindow", u"\u7ed3\u679c\u7edf\u8ba1", None))
        self.groupBox_201.setTitle("")
        self.groupBox_3.setTitle("")
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"\u89c6\u9891", None))
        self.label_28.setText(QCoreApplication.translate("mainWindow", u"video", None))
        self.fps_label.setText("")
        self.out_video.setText("")
        self.runButton.setText("")
        self.stopButton.setText("")
        self.groupBox_4.setTitle("")
        self.statistic_label.setText("")
    # retranslateUi
