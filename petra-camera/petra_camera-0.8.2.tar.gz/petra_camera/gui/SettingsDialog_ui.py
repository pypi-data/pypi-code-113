# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(845, 675)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.le_save_path = QtWidgets.QLineEdit(self.groupBox)
        self.le_save_path.setObjectName("le_save_path")
        self.horizontalLayout.addWidget(self.le_save_path)
        self.cmd_save_folder = QtWidgets.QPushButton(self.groupBox)
        self.cmd_save_folder.setObjectName("cmd_save_folder")
        self.horizontalLayout.addWidget(self.cmd_save_folder)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.cmd_roi_frame_color = QtWidgets.QPushButton(self.groupBox_2)
        self.cmd_roi_frame_color.setText("")
        self.cmd_roi_frame_color.setObjectName("cmd_roi_frame_color")
        self.horizontalLayout_2.addWidget(self.cmd_roi_frame_color)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.cmd_roi_label_font = QtWidgets.QPushButton(self.groupBox_2)
        self.cmd_roi_label_font.setText("")
        self.cmd_roi_label_font.setObjectName("cmd_roi_label_font")
        self.horizontalLayout_2.addWidget(self.cmd_roi_label_font)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.cmd_roi_label_font_color = QtWidgets.QPushButton(self.groupBox_2)
        self.cmd_roi_label_font_color.setText("")
        self.cmd_roi_label_font_color.setObjectName("cmd_roi_label_font_color")
        self.horizontalLayout_2.addWidget(self.cmd_roi_label_font_color)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.cmd_roi_bkg_color = QtWidgets.QPushButton(self.groupBox_2)
        self.cmd_roi_bkg_color.setText("")
        self.cmd_roi_bkg_color.setObjectName("cmd_roi_bkg_color")
        self.horizontalLayout_2.addWidget(self.cmd_roi_bkg_color)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.cmd_marker_color = QtWidgets.QPushButton(self.groupBox_2)
        self.cmd_marker_color.setText("")
        self.cmd_marker_color.setObjectName("cmd_marker_color")
        self.horizontalLayout_3.addWidget(self.cmd_marker_color)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.cmd_title_font = QtWidgets.QPushButton(self.groupBox_2)
        self.cmd_title_font.setText("")
        self.cmd_title_font.setObjectName("cmd_title_font")
        self.horizontalLayout_4.addWidget(self.cmd_title_font)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.cmd_title_font_color = QtWidgets.QPushButton(self.groupBox_2)
        self.cmd_title_font_color.setText("")
        self.cmd_title_font_color.setObjectName("cmd_title_font_color")
        self.horizontalLayout_4.addWidget(self.cmd_title_font_color)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.cmd_title_bkg_color = QtWidgets.QPushButton(self.groupBox_2)
        self.cmd_title_bkg_color.setText("")
        self.cmd_title_bkg_color.setObjectName("cmd_title_bkg_color")
        self.horizontalLayout_4.addWidget(self.cmd_title_bkg_color)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.chk_roi_server_enable = QtWidgets.QCheckBox(self.groupBox)
        self.chk_roi_server_enable.setObjectName("chk_roi_server_enable")
        self.horizontalLayout_5.addWidget(self.chk_roi_server_enable)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.le_roi_server_host = QtWidgets.QLineEdit(self.groupBox)
        self.le_roi_server_host.setObjectName("le_roi_server_host")
        self.horizontalLayout_5.addWidget(self.le_roi_server_host)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.le_roi_server_port = QtWidgets.QLineEdit(self.groupBox)
        self.le_roi_server_port.setObjectName("le_roi_server_port")
        self.horizontalLayout_5.addWidget(self.le_roi_server_port)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.dsb_cross_size = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.dsb_cross_size.setObjectName("dsb_cross_size")
        self.horizontalLayout_6.addWidget(self.dsb_cross_size)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.dsb_circle_size = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.dsb_circle_size.setObjectName("dsb_circle_size")
        self.horizontalLayout_6.addWidget(self.dsb_circle_size)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.tb_cameras = QtWidgets.QTabWidget(SettingsDialog)
        self.tb_cameras.setObjectName("tb_cameras")
        self.verticalLayout_3.addWidget(self.tb_cameras)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.cmd_reset_settings = QtWidgets.QPushButton(SettingsDialog)
        self.cmd_reset_settings.setObjectName("cmd_reset_settings")
        self.horizontalLayout_7.addWidget(self.cmd_reset_settings)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        self.tb_cameras.setCurrentIndex(-1)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "General settings"))
        self.groupBox.setTitle(_translate("SettingsDialog", "General settings"))
        self.label.setText(_translate("SettingsDialog", "Default save folder"))
        self.cmd_save_folder.setText(_translate("SettingsDialog", "Select folder"))
        self.groupBox_2.setTitle(_translate("SettingsDialog", "Colors"))
        self.label_3.setText(_translate("SettingsDialog", "ROI frame color"))
        self.label_4.setText(_translate("SettingsDialog", "ROI label font"))
        self.label_14.setText(_translate("SettingsDialog", "ROI label font color"))
        self.label_13.setText(_translate("SettingsDialog", "ROI label background"))
        self.label_6.setText(_translate("SettingsDialog", "Marker"))
        self.label_5.setText(_translate("SettingsDialog", "Title font"))
        self.label_15.setText(_translate("SettingsDialog", "Title font color"))
        self.label_8.setText(_translate("SettingsDialog", "Title background"))
        self.label_7.setText(_translate("SettingsDialog", "ROI server"))
        self.chk_roi_server_enable.setText(_translate("SettingsDialog", "enable"))
        self.label_9.setText(_translate("SettingsDialog", "host"))
        self.label_2.setText(_translate("SettingsDialog", "post"))
        self.label_10.setText(_translate("SettingsDialog", "Center search:"))
        self.label_11.setText(_translate("SettingsDialog", "cross size"))
        self.label_12.setText(_translate("SettingsDialog", "circle size"))
        self.cmd_reset_settings.setText(_translate("SettingsDialog", "Reset all settings"))

