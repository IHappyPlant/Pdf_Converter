# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttons_layout = QtWidgets.QVBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        self.select_file_btn_layout = QtWidgets.QHBoxLayout()
        self.select_file_btn_layout.setObjectName("select_file_btn_layout")
        self.select_file_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_file_label.sizePolicy().hasHeightForWidth())
        self.select_file_label.setSizePolicy(sizePolicy)
        self.select_file_label.setAlignment(QtCore.Qt.AlignCenter)
        self.select_file_label.setObjectName("select_file_label")
        self.select_file_btn_layout.addWidget(self.select_file_label)
        self.select_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_file_btn.setObjectName("select_file_btn")
        self.select_file_btn_layout.addWidget(self.select_file_btn)
        self.buttons_layout.addLayout(self.select_file_btn_layout)
        self.dpi_layout = QtWidgets.QHBoxLayout()
        self.dpi_layout.setObjectName("dpi_layout")
        self.dpi_label = QtWidgets.QLabel(self.centralwidget)
        self.dpi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dpi_label.setObjectName("dpi_label")
        self.dpi_layout.addWidget(self.dpi_label)
        self.dpi_box = QtWidgets.QComboBox(self.centralwidget)
        self.dpi_box.setObjectName("dpi_box")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_box.addItem("")
        self.dpi_layout.addWidget(self.dpi_box)
        self.buttons_layout.addLayout(self.dpi_layout)
        self.color_mode_layout = QtWidgets.QHBoxLayout()
        self.color_mode_layout.setObjectName("color_mode_layout")
        self.color_mode_label = QtWidgets.QLabel(self.centralwidget)
        self.color_mode_label.setAlignment(QtCore.Qt.AlignCenter)
        self.color_mode_label.setObjectName("color_mode_label")
        self.color_mode_layout.addWidget(self.color_mode_label)
        self.color_mode_box = QtWidgets.QComboBox(self.centralwidget)
        self.color_mode_box.setObjectName("color_mode_box")
        self.color_mode_box.addItem("")
        self.color_mode_box.addItem("")
        self.color_mode_box.addItem("")
        self.color_mode_box.addItem("")
        self.color_mode_layout.addWidget(self.color_mode_box)
        self.buttons_layout.addLayout(self.color_mode_layout)
        self.image_format_layout = QtWidgets.QHBoxLayout()
        self.image_format_layout.setObjectName("image_format_layout")
        self.image_format_label = QtWidgets.QLabel(self.centralwidget)
        self.image_format_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_format_label.setObjectName("image_format_label")
        self.image_format_layout.addWidget(self.image_format_label)
        self.image_format_box = QtWidgets.QComboBox(self.centralwidget)
        self.image_format_box.setObjectName("image_format_box")
        self.image_format_box.addItem("")
        self.image_format_box.addItem("")
        self.image_format_layout.addWidget(self.image_format_box)
        self.buttons_layout.addLayout(self.image_format_layout)
        self.process_doc_btn = QtWidgets.QPushButton(self.centralwidget)
        self.process_doc_btn.setObjectName("process_doc_btn")
        self.buttons_layout.addWidget(self.process_doc_btn)
        self.save_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_file_btn.setObjectName("save_file_btn")
        self.buttons_layout.addWidget(self.save_file_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.buttons_layout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.buttons_layout)
        self.display_layout = QtWidgets.QVBoxLayout()
        self.display_layout.setObjectName("display_layout")
        self.display_page_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_page_label.sizePolicy().hasHeightForWidth())
        self.display_page_label.setSizePolicy(sizePolicy)
        self.display_page_label.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.display_page_label.setText("")
        self.display_page_label.setObjectName("display_page_label")
        self.display_layout.addWidget(self.display_page_label)
        self.page_numbers_label = QtWidgets.QLabel(self.centralwidget)
        self.page_numbers_label.setAlignment(QtCore.Qt.AlignCenter)
        self.page_numbers_label.setObjectName("page_numbers_label")
        self.display_layout.addWidget(self.page_numbers_label)
        self.nav_buttons_layout = QtWidgets.QHBoxLayout()
        self.nav_buttons_layout.setObjectName("nav_buttons_layout")
        self.to_prev_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_prev_btn.setObjectName("to_prev_btn")
        self.nav_buttons_layout.addWidget(self.to_prev_btn)
        self.to_next_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_next_btn.setObjectName("to_next_btn")
        self.nav_buttons_layout.addWidget(self.to_next_btn)
        self.display_layout.addLayout(self.nav_buttons_layout)
        self.horizontalLayout.addLayout(self.display_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.dpi_box.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_file_label.setText(_translate("MainWindow", "File not selected"))
        self.select_file_btn.setText(_translate("MainWindow", "Select file"))
        self.dpi_label.setText(_translate("MainWindow", "DPI:"))
        self.dpi_box.setItemText(0, _translate("MainWindow", "50"))
        self.dpi_box.setItemText(1, _translate("MainWindow", "100"))
        self.dpi_box.setItemText(2, _translate("MainWindow", "150"))
        self.dpi_box.setItemText(3, _translate("MainWindow", "200"))
        self.dpi_box.setItemText(4, _translate("MainWindow", "250"))
        self.dpi_box.setItemText(5, _translate("MainWindow", "300"))
        self.dpi_box.setItemText(6, _translate("MainWindow", "350"))
        self.dpi_box.setItemText(7, _translate("MainWindow", "400"))
        self.dpi_box.setItemText(8, _translate("MainWindow", "450"))
        self.dpi_box.setItemText(9, _translate("MainWindow", "500"))
        self.dpi_box.setItemText(10, _translate("MainWindow", "600"))
        self.dpi_box.setItemText(11, _translate("MainWindow", "700"))
        self.dpi_box.setItemText(12, _translate("MainWindow", "750"))
        self.dpi_box.setItemText(13, _translate("MainWindow", "800"))
        self.color_mode_label.setText(_translate("MainWindow", "Color mode:"))
        self.color_mode_box.setItemText(0, _translate("MainWindow", "RGB"))
        self.color_mode_box.setItemText(1, _translate("MainWindow", "RGBA"))
        self.color_mode_box.setItemText(2, _translate("MainWindow", "Grayscale"))
        self.color_mode_box.setItemText(3, _translate("MainWindow", "Binary"))
        self.image_format_label.setText(_translate("MainWindow", "Image format:"))
        self.image_format_box.setItemText(0, _translate("MainWindow", "JPG"))
        self.image_format_box.setItemText(1, _translate("MainWindow", "PNG"))
        self.process_doc_btn.setText(_translate("MainWindow", "Process file"))
        self.save_file_btn.setText(_translate("MainWindow", "Save to..."))
        self.page_numbers_label.setText(_translate("MainWindow", "Page  of  "))
        self.to_prev_btn.setText(_translate("MainWindow", "Previous Page"))
        self.to_next_btn.setText(_translate("MainWindow", "Next Page"))