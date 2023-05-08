# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(919, 755)
        MainWindow.setStyleSheet(u"*{\n"
"	font-size: 14px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-weight: bold;\n"
"	color: #d3dae3;\n"
"}\n"
"QMainWindow, QStackedWidget, QGroupBox{\n"
"	background-color:#1e1d23;\n"
"	border:none;\n"
"}\n"
"QTextEdit, QListWidget {\n"
"	background-color:#1e1d23;\n"
"}\n"
"QPushButton{\n"
"	border-style: solid;\n"
"	border-color: #050a0e;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	padding: 3px;\n"
"	background-color: #100E19;\n"
"}\n"
"QPushButton::default{\n"
"	border-style: solid;\n"
"	border-color: #050a0e;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	padding: 3px;\n"
"	background-color: #151a1e;\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
"    border-left-color: qlineargradien"
                        "t(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
"	border-width: 2px;\n"
"    border-radius: 1px;\n"
"	padding: 3px;\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
"	border-width: 2px;\n"
"    border-radius: 1px"
                        ";\n"
"	padding: 3px;\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px; border-radius: 4px;\n"
"	border-color: rgb(58, 58, 58);\n"
"	border-style: inset;\n"
"	padding-left: 11px;\n"
"	padding-right: 11px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	background:#1e1d23;\n"
"	selection-background-color:#007b50;\n"
"	selection-color: #FFFFFF;\n"
"}\n"
"QCheckBox {\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: rgb(87, 97, 106);\n"
"	background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
""
                        "	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: #04b97f;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QComboBox {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"	background: #1e1d23;\n"
"	color: #a9b7c6;\n"
"	selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"	selection-color: #FFFF"
                        "FF;\n"
"	selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"}\n"
"QTableWidget {\n"
"    background-color: #1e1d23;\n"
"    gridline-color: #666666;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #555555;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #1e1d23;\n"
"	border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.firstTask = QPushButton(self.groupBox)
        self.firstTask.setObjectName(u"firstTask")

        self.verticalLayout.addWidget(self.firstTask)

        self.secondTask = QPushButton(self.groupBox)
        self.secondTask.setObjectName(u"secondTask")

        self.verticalLayout.addWidget(self.secondTask)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_2 = QGridLayout(self.page_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.openFileBtn = QPushButton(self.page_1)
        self.openFileBtn.setObjectName(u"openFileBtn")

        self.verticalLayout_2.addWidget(self.openFileBtn)

        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.fileBuffer = QTextEdit(self.page_1)
        self.fileBuffer.setObjectName(u"fileBuffer")
        self.fileBuffer.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.fileBuffer)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.rowsTable = QTableWidget(self.page_1)
        if (self.rowsTable.columnCount() < 23):
            self.rowsTable.setColumnCount(23)
        __qtablewidgetitem = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.rowsTable.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        if (self.rowsTable.rowCount() < 4):
            self.rowsTable.setRowCount(4)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.rowsTable.setVerticalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.rowsTable.setVerticalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.rowsTable.setVerticalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.rowsTable.setVerticalHeaderItem(3, __qtablewidgetitem23)
        self.rowsTable.setObjectName(u"rowsTable")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rowsTable.sizePolicy().hasHeightForWidth())
        self.rowsTable.setSizePolicy(sizePolicy)
        self.rowsTable.setMinimumSize(QSize(0, 95))
        self.rowsTable.setMaximumSize(QSize(16777215, 150))
        self.rowsTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rowsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rowsTable.setGridStyle(Qt.SolidLine)
        self.rowsTable.setSortingEnabled(False)
        self.rowsTable.setWordWrap(True)
        self.rowsTable.setCornerButtonEnabled(False)
        self.rowsTable.setColumnCount(23)
        self.rowsTable.horizontalHeader().setVisible(False)
        self.rowsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.rowsTable.horizontalHeader().setMinimumSectionSize(20)
        self.rowsTable.horizontalHeader().setDefaultSectionSize(30)
        self.rowsTable.horizontalHeader().setHighlightSections(True)

        self.verticalLayout_3.addWidget(self.rowsTable)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.relativeFrequencyPolygonBtn = QPushButton(self.page_1)
        self.relativeFrequencyPolygonBtn.setObjectName(u"relativeFrequencyPolygonBtn")

        self.horizontalLayout.addWidget(self.relativeFrequencyPolygonBtn)

        self.frequencyPolygonBtn = QPushButton(self.page_1)
        self.frequencyPolygonBtn.setObjectName(u"frequencyPolygonBtn")

        self.horizontalLayout.addWidget(self.frequencyPolygonBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(self.page_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.page_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.empiricalFunctionBtn = QPushButton(self.page_1)
        self.empiricalFunctionBtn.setObjectName(u"empiricalFunctionBtn")

        self.verticalLayout_4.addWidget(self.empiricalFunctionBtn)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 2, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formulaX = QLabel(self.page_1)
        self.formulaX.setObjectName(u"formulaX")
        self.formulaX.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.formulaX)

        self.formulaD = QLabel(self.page_1)
        self.formulaD.setObjectName(u"formulaD")
        self.formulaD.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.formulaD)

        self.formulaSigma = QLabel(self.page_1)
        self.formulaSigma.setObjectName(u"formulaSigma")
        self.formulaSigma.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.formulaSigma)

        self.formulaS = QLabel(self.page_1)
        self.formulaS.setObjectName(u"formulaS")
        self.formulaS.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.formulaS)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 3, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.page_1)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.lineD = QLineEdit(self.page_1)
        self.lineD.setObjectName(u"lineD")
        self.lineD.setAlignment(Qt.AlignCenter)
        self.lineD.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineD)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.page_1)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.lineX = QLineEdit(self.page_1)
        self.lineX.setObjectName(u"lineX")
        self.lineX.setAlignment(Qt.AlignCenter)
        self.lineX.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineX)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_12 = QLabel(self.page_1)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.lineSigma = QLineEdit(self.page_1)
        self.lineSigma.setObjectName(u"lineSigma")
        self.lineSigma.setAlignment(Qt.AlignCenter)
        self.lineSigma.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineSigma)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_13 = QLabel(self.page_1)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.lineS = QLineEdit(self.page_1)
        self.lineS.setObjectName(u"lineS")
        self.lineS.setAlignment(Qt.AlignCenter)
        self.lineS.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineS)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.gridLayout_2.addLayout(self.verticalLayout_6, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.firstTask.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0431\u043e\u043b\u044c\u0448\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432", None))
        self.secondTask.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u043b\u044c\u0448\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432", None))
        self.openFileBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u0444\u0430\u0439\u043b\u0430", None))
        self.fileBuffer.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:14px; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0440\u0438\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0440\u044f\u0434 \u0438 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0440\u044f\u0434", None))
        ___qtablewidgetitem = self.rowsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem1 = self.rowsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem2 = self.rowsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem3 = self.rowsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem4 = self.rowsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem5 = self.rowsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem6 = self.rowsTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem7 = self.rowsTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem8 = self.rowsTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem9 = self.rowsTable.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem10 = self.rowsTable.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem11 = self.rowsTable.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem12 = self.rowsTable.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem13 = self.rowsTable.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem14 = self.rowsTable.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem15 = self.rowsTable.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem16 = self.rowsTable.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem17 = self.rowsTable.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem18 = self.rowsTable.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem19 = self.rowsTable.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem20 = self.rowsTable.verticalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem21 = self.rowsTable.verticalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem22 = self.rowsTable.verticalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"c", None));
        ___qtablewidgetitem23 = self.rowsTable.verticalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"d", None));
        self.relativeFrequencyPolygonBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0438\u0433\u043e\u043d \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0447\u0430\u0441\u0442\u043e\u0442", None))
        self.frequencyPolygonBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0438\u0433\u043e\u043d \u0447\u0430\u0441\u0442\u043e\u0442", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u044d\u043c\u043f\u0438\u0440\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 F*(x):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0434\u0435\u0441\u044c \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0444\u043e\u0442\u043a\u0430 \u0441 \u044d\u043c\u043f\u0438\u0440\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0435\u0439", None))
        self.empiricalFunctionBtn.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a \u044d\u043c\u043f\u0438\u0440\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 F*(x)", None))
        self.formulaX.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0443\u043b\u0430 x \u0432\u044b\u0431\u043e\u0440\u043e\u0447\u043d\u043e\u0435", None))
        self.formulaD.setText(QCoreApplication.translate("MainWindow", u"D \u0432\u044b\u0431\u043e\u0440\u043e\u0447\u043d\u043e\u0435", None))
        self.formulaSigma.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0438\u0433\u043c\u0430 \u0432\u044b\u0431\u043e\u0440\u043e\u0447\u043d\u043e\u0435", None))
        self.formulaS.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 D \u0432\u044b\u0431\u043e\u0440\u043e\u0447\u043d\u043e\u0435", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0445 \u0432\u044b\u0431\u043e\u0440\u043e\u0447\u043d\u043e\u0435", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0441\u0438\u0433\u043c\u0430 \u0432\u044b\u0431\u043e\u0440\u043e\u0447\u043d\u043e\u0435", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 S", None))
        self.lineS.setText(QCoreApplication.translate("MainWindow", u"\u0444\u044b\u0432", None))
    # retranslateUi

