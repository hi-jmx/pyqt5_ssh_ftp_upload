# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(298, 698)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(9, 9, 274, 748))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.h_layout_device = QtWidgets.QHBoxLayout()
        self.h_layout_device.setObjectName("h_layout_device")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.h_layout_device.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setObjectName("comboBox")
        self.h_layout_device.addWidget(self.comboBox)
        self.h_layout_device.setStretch(0, 1)
        self.h_layout_device.setStretch(1, 4)
        self.verticalLayout_3.addLayout(self.h_layout_device)
        self.device_0 = QtWidgets.QWidget(self.widget)
        self.device_0.setMinimumSize(QtCore.QSize(0, 25))
        self.device_0.setMaximumSize(QtCore.QSize(16777215, 25))
        self.device_0.setObjectName("device_0")
        self.label_0 = QtWidgets.QLabel(self.device_0)
        self.label_0.setGeometry(QtCore.QRect(9, 0, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.checkBox_0 = QtWidgets.QCheckBox(self.device_0)
        self.checkBox_0.setGeometry(QtCore.QRect(61, 0, 191, 20))
        self.checkBox_0.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox_0.setObjectName("checkBox_0")
        self.verticalLayout_3.addWidget(self.device_0)
        self.device_1 = QtWidgets.QWidget(self.widget)
        self.device_1.setMinimumSize(QtCore.QSize(0, 25))
        self.device_1.setMaximumSize(QtCore.QSize(16777215, 25))
        self.device_1.setObjectName("device_1")
        self.label_1 = QtWidgets.QLabel(self.device_1)
        self.label_1.setGeometry(QtCore.QRect(9, 9, 48, 16))
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.checkBox_1 = QtWidgets.QCheckBox(self.device_1)
        self.checkBox_1.setGeometry(QtCore.QRect(63, -3, 191, 31))
        self.checkBox_1.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout_3.addWidget(self.device_1)
        self.device_2 = QtWidgets.QWidget(self.widget)
        self.device_2.setMinimumSize(QtCore.QSize(0, 25))
        self.device_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.device_2.setObjectName("device_2")
        self.label_2 = QtWidgets.QLabel(self.device_2)
        self.label_2.setGeometry(QtCore.QRect(9, 9, 48, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.device_2)
        self.checkBox_2.setGeometry(QtCore.QRect(63, -2, 191, 31))
        self.checkBox_2.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_3.addWidget(self.device_2)
        self.device_3 = QtWidgets.QWidget(self.widget)
        self.device_3.setMinimumSize(QtCore.QSize(0, 25))
        self.device_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.device_3.setObjectName("device_3")
        self.label_3 = QtWidgets.QLabel(self.device_3)
        self.label_3.setGeometry(QtCore.QRect(9, 9, 48, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.device_3)
        self.checkBox_3.setGeometry(QtCore.QRect(63, -2, 181, 31))
        self.checkBox_3.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_3.addWidget(self.device_3)
        self.device_4 = QtWidgets.QWidget(self.widget)
        self.device_4.setMinimumSize(QtCore.QSize(0, 25))
        self.device_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.device_4.setObjectName("device_4")
        self.label_4 = QtWidgets.QLabel(self.device_4)
        self.label_4.setGeometry(QtCore.QRect(9, 9, 48, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.checkBox_4 = QtWidgets.QCheckBox(self.device_4)
        self.checkBox_4.setGeometry(QtCore.QRect(63, -2, 181, 31))
        self.checkBox_4.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_3.addWidget(self.device_4)
        self.device_5 = QtWidgets.QWidget(self.widget)
        self.device_5.setMinimumSize(QtCore.QSize(0, 25))
        self.device_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.device_5.setObjectName("device_5")
        self.label_5 = QtWidgets.QLabel(self.device_5)
        self.label_5.setGeometry(QtCore.QRect(9, 9, 48, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.checkBox_5 = QtWidgets.QCheckBox(self.device_5)
        self.checkBox_5.setGeometry(QtCore.QRect(63, -2, 181, 31))
        self.checkBox_5.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_3.addWidget(self.device_5)
        self.device_6 = QtWidgets.QWidget(self.widget)
        self.device_6.setMinimumSize(QtCore.QSize(0, 25))
        self.device_6.setMaximumSize(QtCore.QSize(16777215, 25))
        self.device_6.setObjectName("device_6")
        self.label_6 = QtWidgets.QLabel(self.device_6)
        self.label_6.setGeometry(QtCore.QRect(9, 9, 48, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.checkBox_6 = QtWidgets.QCheckBox(self.device_6)
        self.checkBox_6.setGeometry(QtCore.QRect(63, -2, 181, 31))
        self.checkBox_6.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_3.addWidget(self.device_6)
        self.device_7 = QtWidgets.QWidget(self.widget)
        self.device_7.setMinimumSize(QtCore.QSize(0, 25))
        self.device_7.setMaximumSize(QtCore.QSize(16777215, 25))
        self.device_7.setObjectName("device_7")
        self.label_7 = QtWidgets.QLabel(self.device_7)
        self.label_7.setGeometry(QtCore.QRect(9, 9, 48, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.checkBox_7 = QtWidgets.QCheckBox(self.device_7)
        self.checkBox_7.setGeometry(QtCore.QRect(63, -2, 181, 31))
        self.checkBox_7.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_3.addWidget(self.device_7)
        self.device_8 = QtWidgets.QWidget(self.widget)
        self.device_8.setMinimumSize(QtCore.QSize(0, 25))
        self.device_8.setMaximumSize(QtCore.QSize(16777215, 25))
        self.device_8.setObjectName("device_8")
        self.label_8 = QtWidgets.QLabel(self.device_8)
        self.label_8.setGeometry(QtCore.QRect(9, 9, 48, 16))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.checkBox_8 = QtWidgets.QCheckBox(self.device_8)
        self.checkBox_8.setGeometry(QtCore.QRect(63, -2, 181, 31))
        self.checkBox_8.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_3.addWidget(self.device_8)
        self.device_9 = QtWidgets.QWidget(self.widget)
        self.device_9.setMinimumSize(QtCore.QSize(0, 25))
        self.device_9.setMaximumSize(QtCore.QSize(16777215, 25))
        self.device_9.setObjectName("device_9")
        self.label_9 = QtWidgets.QLabel(self.device_9)
        self.label_9.setGeometry(QtCore.QRect(9, 9, 48, 16))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.checkBox_9 = QtWidgets.QCheckBox(self.device_9)
        self.checkBox_9.setGeometry(QtCore.QRect(63, -2, 191, 31))
        self.checkBox_9.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_3.addWidget(self.device_9)
        self.device_10 = QtWidgets.QWidget(self.widget)
        self.device_10.setMinimumSize(QtCore.QSize(0, 32))
        self.device_10.setMaximumSize(QtCore.QSize(16777215, 32))
        self.device_10.setObjectName("device_10")
        self.label_12 = QtWidgets.QLabel(self.device_10)
        self.label_12.setGeometry(QtCore.QRect(1, 1, 16, 16))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.textEdit = QtWidgets.QTextEdit(self.device_10)
        self.textEdit.setGeometry(QtCore.QRect(48, 1, 201, 30))
        self.textEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_send_sbar = QtWidgets.QScrollBar()
        self.textEdit_send_sbar.setStyleSheet("""
                               QScrollBar:horizontal {
                                  border-height: 0px;
                                  border: none;
                                  background:rgba(64, 65, 79, 0);
                                  height:6px;
                                  margin: 0px 0px 0px 0px;
                              }
                              QScrollBar::handle:horizontal {
                                  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                  stop: 0 #aaaaff, stop: 0.5 #aaaaff, stop:1 #aaaaff);
                                  min-width: 20px;
                                  max-width: 20px;
                                  margin: 0 0px 0 0px;
                                  border-radius: 3px;
                              }
                              QScrollBar::add-line:horizontal {
                                  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                  stop: 0 rgba(64, 65, 79, 0), stop: 0.5 rgba(64, 65, 79, 0),  stop:1 rgba(64, 65, 79, 0));
                                  width: 0px;
                                  border: none;
                                  subcontrol-position: right;
                                  subcontrol-origin: margin;
                              }
                              QScrollBar::sub-line:horizontal {
                                  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                  stop: 0  rgba(64, 65, 79, 0), stop: 0.5 rgba(64, 65, 79, 0),  stop:1 rgba(64, 65, 79, 0));
                                  width: 0 px;
                                  border: none;
                                  subcontrol-position: left;
                                  subcontrol-origin: margin;
                              }
                              QScrollBar::sub-page:horizontal {
                              background: rgba(64, 65, 79, 0);
                              }

                              QScrollBar::add-page:horizontal {
                              background: rgba(64, 65, 79, 0);
                              }
                              """)

        # self.textEdit.setVerticalScrollBar(self.textEdit_send_sbar)
        self.textEdit.setHorizontalScrollBar(self.textEdit_send_sbar)
        self.verticalLayout_3.addWidget(self.device_10)
        self.h_layout_describe = QtWidgets.QHBoxLayout()
        self.h_layout_describe.setObjectName("h_layout_describe")
        self.label_describe_1 = QtWidgets.QLabel(self.widget)
        self.label_describe_1.setText("")
        self.label_describe_1.setObjectName("label_describe_1")
        self.h_layout_describe.addWidget(self.label_describe_1)
        self.label_describe_2 = QtWidgets.QLabel(self.widget)
        self.label_describe_2.setObjectName("label_describe_2")
        self.h_layout_describe.addWidget(self.label_describe_2)
        self.h_layout_describe.setStretch(0, 1)
        self.h_layout_describe.setStretch(1, 4)
        self.verticalLayout_3.addLayout(self.h_layout_describe)
        self.h_layout_select = QtWidgets.QHBoxLayout()
        self.h_layout_select.setObjectName("h_layout_select")
        self.label_select = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_select.setFont(font)
        self.label_select.setObjectName("label_select")
        self.h_layout_select.addWidget(self.label_select)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.h_layout_select.addWidget(self.lineEdit)
        self.pushButton_select = QtWidgets.QPushButton(self.widget)
        self.pushButton_select.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_select.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_select.setObjectName("pushButton_select")
        self.h_layout_select.addWidget(self.pushButton_select)
        self.h_layout_select.setStretch(0, 1)
        self.h_layout_select.setStretch(1, 3)
        self.verticalLayout_3.addLayout(self.h_layout_select)
        self.h_layout_upload = QtWidgets.QHBoxLayout()
        self.h_layout_upload.setObjectName("h_layout_upload")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout_upload.addItem(spacerItem)
        self.pushButton_upload = QtWidgets.QPushButton(self.widget)
        self.pushButton_upload.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.h_layout_upload.addWidget(self.pushButton_upload)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout_upload.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.h_layout_upload)
        self.textEdit_log = QtWidgets.QTextEdit(self.widget)
        self.textEdit_log.setMinimumSize(QtCore.QSize(0, 150))
        self.textEdit_log.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textEdit_log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_log.setReadOnly(True)
        self.textEdit_log.setObjectName("textEdit_log")
        self.textEdit_send_sbar_2 = QtWidgets.QScrollBar()

        # 2.给这个滚动条添加属性
        self.textEdit_send_sbar_2.setStyleSheet("""
                     QScrollBar:vertical {
                          border-width: 0px;
                          border: none;
                          background:rgba(64, 65, 79, 0);
                          width:6px;
                          margin: 0px 0px 0px 0px;
                      }
                      QScrollBar::handle:vertical {
                          background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                          stop: 0 #aaaaff, stop: 0.5 #aaaaff, stop:1 #aaaaff);
                          min-height: 20px;
                          max-height: 20px;
                          margin: 0 0px 0 0px;
                          border-radius: 3px;
                      }
                      QScrollBar::add-line:vertical {
                          background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                          stop: 0 rgba(64, 65, 79, 0), stop: 0.5 rgba(64, 65, 79, 0),  stop:1 rgba(64, 65, 79, 0));
                          height: 0px;
                          border: none;
                          subcontrol-position: bottom;
                          subcontrol-origin: margin;
                      }
                      QScrollBar::sub-line:vertical {
                          background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                          stop: 0  rgba(64, 65, 79, 0), stop: 0.5 rgba(64, 65, 79, 0),  stop:1 rgba(64, 65, 79, 0));
                          height: 0 px;
                          border: none;
                          subcontrol-position: top;
                          subcontrol-origin: margin;
                      }
                      QScrollBar::sub-page:vertical {
                      background: rgba(64, 65, 79, 0);
                      }

                      QScrollBar::add-page:vertical {
                      background: rgba(64, 65, 79, 0);
                      }
                      """)

        # 3.把这个textEdit_send_sbar当作属性附加到textEdit控件上
        self.textEdit_log.setVerticalScrollBar(self.textEdit_send_sbar_2)
        self.verticalLayout_3.addWidget(self.textEdit_log)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WA黑匣子证书上传工具"))
        self.label.setText(_translate("MainWindow", "设备："))
        self.label_0.setText(_translate("MainWindow", "IP："))
        self.checkBox_0.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_1.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_7.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_8.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_9.setText(_translate("MainWindow", "CheckBox"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.label_describe_2.setText(_translate("MainWindow", "*多个IP用\";\"隔开"))
        self.label_select.setText(_translate("MainWindow", "证书："))
        self.pushButton_select.setText(_translate("MainWindow", "选择"))
        self.pushButton_upload.setText(_translate("MainWindow", "上传"))

        self.comboBox.view().setFixedHeight(200)