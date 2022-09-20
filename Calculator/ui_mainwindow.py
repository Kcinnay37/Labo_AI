# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(753, 1105)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Text = QLabel(self.centralwidget)
        self.Text.setObjectName(u"Text")
        self.Text.setGeometry(QRect(10, 0, 731, 171))
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Text.sizePolicy().hasHeightForWidth())
        self.Text.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(40)
        self.Text.setFont(font)
        self.Text.setLayoutDirection(Qt.LeftToRight)
        self.Text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 170, 751, 891))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Num_2 = QPushButton(self.layoutWidget)
        self.Num_2.setObjectName(u"Num_2")
        sizePolicy.setHeightForWidth(self.Num_2.sizePolicy().hasHeightForWidth())
        self.Num_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(50)
        self.Num_2.setFont(font1)

        self.gridLayout.addWidget(self.Num_2, 4, 1, 1, 1)

        self.Num_9 = QPushButton(self.layoutWidget)
        self.Num_9.setObjectName(u"Num_9")
        sizePolicy.setHeightForWidth(self.Num_9.sizePolicy().hasHeightForWidth())
        self.Num_9.setSizePolicy(sizePolicy)
        self.Num_9.setFont(font1)

        self.gridLayout.addWidget(self.Num_9, 2, 2, 1, 1)

        self.Op_1 = QPushButton(self.layoutWidget)
        self.Op_1.setObjectName(u"Op_1")
        sizePolicy.setHeightForWidth(self.Op_1.sizePolicy().hasHeightForWidth())
        self.Op_1.setSizePolicy(sizePolicy)
        self.Op_1.setFont(font1)

        self.gridLayout.addWidget(self.Op_1, 1, 0, 1, 1)

        self.Reset = QPushButton(self.layoutWidget)
        self.Reset.setObjectName(u"Reset")
        sizePolicy.setHeightForWidth(self.Reset.sizePolicy().hasHeightForWidth())
        self.Reset.setSizePolicy(sizePolicy)
        self.Reset.setFont(font1)

        self.gridLayout.addWidget(self.Reset, 0, 2, 1, 1)

        self.Num_5 = QPushButton(self.layoutWidget)
        self.Num_5.setObjectName(u"Num_5")
        sizePolicy.setHeightForWidth(self.Num_5.sizePolicy().hasHeightForWidth())
        self.Num_5.setSizePolicy(sizePolicy)
        self.Num_5.setFont(font1)

        self.gridLayout.addWidget(self.Num_5, 3, 1, 1, 1)

        self.Num_0 = QPushButton(self.layoutWidget)
        self.Num_0.setObjectName(u"Num_0")
        sizePolicy.setHeightForWidth(self.Num_0.sizePolicy().hasHeightForWidth())
        self.Num_0.setSizePolicy(sizePolicy)
        self.Num_0.setFont(font1)

        self.gridLayout.addWidget(self.Num_0, 5, 1, 1, 1)

        self.Num_7 = QPushButton(self.layoutWidget)
        self.Num_7.setObjectName(u"Num_7")
        sizePolicy.setHeightForWidth(self.Num_7.sizePolicy().hasHeightForWidth())
        self.Num_7.setSizePolicy(sizePolicy)
        self.Num_7.setFont(font1)

        self.gridLayout.addWidget(self.Num_7, 2, 0, 1, 1)

        self.Equal = QPushButton(self.layoutWidget)
        self.Equal.setObjectName(u"Equal")
        sizePolicy.setHeightForWidth(self.Equal.sizePolicy().hasHeightForWidth())
        self.Equal.setSizePolicy(sizePolicy)
        self.Equal.setFont(font1)

        self.gridLayout.addWidget(self.Equal, 5, 3, 1, 1)

        self.Op_6 = QPushButton(self.layoutWidget)
        self.Op_6.setObjectName(u"Op_6")
        sizePolicy.setHeightForWidth(self.Op_6.sizePolicy().hasHeightForWidth())
        self.Op_6.setSizePolicy(sizePolicy)
        self.Op_6.setFont(font1)

        self.gridLayout.addWidget(self.Op_6, 3, 3, 1, 1)

        self.Op_7 = QPushButton(self.layoutWidget)
        self.Op_7.setObjectName(u"Op_7")
        sizePolicy.setHeightForWidth(self.Op_7.sizePolicy().hasHeightForWidth())
        self.Op_7.setSizePolicy(sizePolicy)
        self.Op_7.setFont(font1)

        self.gridLayout.addWidget(self.Op_7, 4, 3, 1, 1)

        self.Op_2 = QPushButton(self.layoutWidget)
        self.Op_2.setObjectName(u"Op_2")
        sizePolicy.setHeightForWidth(self.Op_2.sizePolicy().hasHeightForWidth())
        self.Op_2.setSizePolicy(sizePolicy)
        self.Op_2.setFont(font1)

        self.gridLayout.addWidget(self.Op_2, 1, 1, 1, 1)

        self.Op_3 = QPushButton(self.layoutWidget)
        self.Op_3.setObjectName(u"Op_3")
        sizePolicy.setHeightForWidth(self.Op_3.sizePolicy().hasHeightForWidth())
        self.Op_3.setSizePolicy(sizePolicy)
        self.Op_3.setFont(font1)

        self.gridLayout.addWidget(self.Op_3, 1, 2, 1, 1)

        self.Num_3 = QPushButton(self.layoutWidget)
        self.Num_3.setObjectName(u"Num_3")
        sizePolicy.setHeightForWidth(self.Num_3.sizePolicy().hasHeightForWidth())
        self.Num_3.setSizePolicy(sizePolicy)
        self.Num_3.setFont(font1)

        self.gridLayout.addWidget(self.Num_3, 4, 2, 1, 1)

        self.Op_5 = QPushButton(self.layoutWidget)
        self.Op_5.setObjectName(u"Op_5")
        sizePolicy.setHeightForWidth(self.Op_5.sizePolicy().hasHeightForWidth())
        self.Op_5.setSizePolicy(sizePolicy)
        self.Op_5.setFont(font1)

        self.gridLayout.addWidget(self.Op_5, 2, 3, 1, 1)

        self.Num_6 = QPushButton(self.layoutWidget)
        self.Num_6.setObjectName(u"Num_6")
        sizePolicy.setHeightForWidth(self.Num_6.sizePolicy().hasHeightForWidth())
        self.Num_6.setSizePolicy(sizePolicy)
        self.Num_6.setFont(font1)

        self.gridLayout.addWidget(self.Num_6, 3, 2, 1, 1)

        self.PlusOrMinus = QPushButton(self.layoutWidget)
        self.PlusOrMinus.setObjectName(u"PlusOrMinus")
        sizePolicy.setHeightForWidth(self.PlusOrMinus.sizePolicy().hasHeightForWidth())
        self.PlusOrMinus.setSizePolicy(sizePolicy)
        self.PlusOrMinus.setFont(font1)

        self.gridLayout.addWidget(self.PlusOrMinus, 5, 0, 1, 1)

        self.ResetCurr = QPushButton(self.layoutWidget)
        self.ResetCurr.setObjectName(u"ResetCurr")
        sizePolicy.setHeightForWidth(self.ResetCurr.sizePolicy().hasHeightForWidth())
        self.ResetCurr.setSizePolicy(sizePolicy)
        self.ResetCurr.setFont(font1)

        self.gridLayout.addWidget(self.ResetCurr, 0, 1, 1, 1)

        self.Num_4 = QPushButton(self.layoutWidget)
        self.Num_4.setObjectName(u"Num_4")
        sizePolicy.setHeightForWidth(self.Num_4.sizePolicy().hasHeightForWidth())
        self.Num_4.setSizePolicy(sizePolicy)
        self.Num_4.setFont(font1)

        self.gridLayout.addWidget(self.Num_4, 3, 0, 1, 1)

        self.Comma = QPushButton(self.layoutWidget)
        self.Comma.setObjectName(u"Comma")
        sizePolicy.setHeightForWidth(self.Comma.sizePolicy().hasHeightForWidth())
        self.Comma.setSizePolicy(sizePolicy)
        self.Comma.setFont(font1)

        self.gridLayout.addWidget(self.Comma, 5, 2, 1, 1)

        self.Num_8 = QPushButton(self.layoutWidget)
        self.Num_8.setObjectName(u"Num_8")
        sizePolicy.setHeightForWidth(self.Num_8.sizePolicy().hasHeightForWidth())
        self.Num_8.setSizePolicy(sizePolicy)
        self.Num_8.setFont(font1)

        self.gridLayout.addWidget(self.Num_8, 2, 1, 1, 1)

        self.Op_0 = QPushButton(self.layoutWidget)
        self.Op_0.setObjectName(u"Op_0")
        sizePolicy.setHeightForWidth(self.Op_0.sizePolicy().hasHeightForWidth())
        self.Op_0.setSizePolicy(sizePolicy)
        self.Op_0.setFont(font1)

        self.gridLayout.addWidget(self.Op_0, 0, 0, 1, 1)

        self.Op_4 = QPushButton(self.layoutWidget)
        self.Op_4.setObjectName(u"Op_4")
        sizePolicy.setHeightForWidth(self.Op_4.sizePolicy().hasHeightForWidth())
        self.Op_4.setSizePolicy(sizePolicy)
        self.Op_4.setFont(font1)

        self.gridLayout.addWidget(self.Op_4, 1, 3, 1, 1)

        self.Erase = QPushButton(self.layoutWidget)
        self.Erase.setObjectName(u"Erase")
        sizePolicy.setHeightForWidth(self.Erase.sizePolicy().hasHeightForWidth())
        self.Erase.setSizePolicy(sizePolicy)
        self.Erase.setFont(font1)

        self.gridLayout.addWidget(self.Erase, 0, 3, 1, 1)

        self.Num_1 = QPushButton(self.layoutWidget)
        self.Num_1.setObjectName(u"Num_1")
        sizePolicy.setHeightForWidth(self.Num_1.sizePolicy().hasHeightForWidth())
        self.Num_1.setSizePolicy(sizePolicy)
        self.Num_1.setFont(font1)

        self.gridLayout.addWidget(self.Num_1, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 753, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Text.setText("")
        self.Num_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Num_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Op_1.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.Reset.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Num_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Num_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Num_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Op_6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Op_7.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Op_2.setText(QCoreApplication.translate("MainWindow", u"x2", None))
        self.Op_3.setText(QCoreApplication.translate("MainWindow", u"sqrt", None))
        self.Num_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Op_5.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.Num_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.PlusOrMinus.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.ResetCurr.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.Num_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Comma.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.Num_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Op_0.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.Op_4.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.Erase.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.Num_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
    # retranslateUi

