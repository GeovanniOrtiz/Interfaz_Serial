# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QHBoxLayout, QLCDNumber,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.lcdNumber = QLCDNumber(self.tab)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout_4.addWidget(self.lcdNumber)

        self.control1 = QDial(self.tab)
        self.control1.setObjectName(u"control1")

        self.verticalLayout_4.addWidget(self.control1)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.lcdNumber_2 = QLCDNumber(self.tab)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")

        self.verticalLayout_5.addWidget(self.lcdNumber_2)

        self.control2 = QDial(self.tab)
        self.control2.setObjectName(u"control2")

        self.verticalLayout_5.addWidget(self.control2)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.lcdNumber_3 = QLCDNumber(self.tab)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")

        self.verticalLayout_7.addWidget(self.lcdNumber_3)

        self.control3 = QDial(self.tab)
        self.control3.setObjectName(u"control3")

        self.verticalLayout_7.addWidget(self.control3)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4)

        self.lcdNumber_4 = QLCDNumber(self.tab)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")

        self.verticalLayout_8.addWidget(self.lcdNumber_4)

        self.control4 = QDial(self.tab)
        self.control4.setObjectName(u"control4")

        self.verticalLayout_8.addWidget(self.control4)


        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.lcdNumber_5 = QLCDNumber(self.tab)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")

        self.verticalLayout_9.addWidget(self.lcdNumber_5)

        self.control5 = QDial(self.tab)
        self.control5.setObjectName(u"control5")

        self.verticalLayout_9.addWidget(self.control5)


        self.horizontalLayout.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.lcdNumber_6 = QLCDNumber(self.tab)
        self.lcdNumber_6.setObjectName(u"lcdNumber_6")

        self.verticalLayout_10.addWidget(self.lcdNumber_6)

        self.control6 = QDial(self.tab)
        self.control6.setObjectName(u"control6")

        self.verticalLayout_10.addWidget(self.control6)


        self.horizontalLayout.addLayout(self.verticalLayout_10)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_enviar = QPushButton(self.tab)
        self.btn_enviar.setObjectName(u"btn_enviar")

        self.verticalLayout_12.addWidget(self.btn_enviar)


        self.horizontalLayout.addLayout(self.verticalLayout_12)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.control1.valueChanged.connect(self.lcdNumber.display)
        self.control2.valueChanged.connect(self.lcdNumber_2.display)
        self.control3.valueChanged.connect(self.lcdNumber_3.display)
        self.control4.valueChanged.connect(self.lcdNumber_4.display)
        self.control5.valueChanged.connect(self.lcdNumber_5.display)
        self.control6.valueChanged.connect(self.lcdNumber_6.display)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Control 1</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Control 2</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Control 3</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Control 4</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Control 5</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Control 6</span></p></body></html>", None))
        self.btn_enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 3", None))
    # retranslateUi

