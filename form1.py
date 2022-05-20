# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt
import imutils
from PyQt5 import QtCore, QtGui, QtWidgets

speck_size = 0# GLOBAL
threshold = 0#GLOBAL
points_of_interest = [] #GLOBAL

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1827, 1067)
        MainWindow.setStyleSheet("background-color: rgb(14, 19, 122);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.liveFeed = QtWidgets.QLabel(self.centralwidget)
        self.liveFeed.setGeometry(QtCore.QRect(80, 200, 1281, 511))
        self.liveFeed.setStyleSheet("background: #000000\n"
"")
        self.liveFeed.setText("")
        self.liveFeed.setObjectName("liveFeed")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(1400, 150, 371, 561))
        self.frame.setStyleSheet("background-color: rgb(14, 19, 122);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.update_push_button = QtWidgets.QPushButton(self.frame)
        self.update_push_button.setGeometry(QtCore.QRect(20, 280, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.update_push_button.setFont(font)
        self.update_push_button.setStyleSheet("background: rgb(114, 159, 207)")
        self.update_push_button.setObjectName("update_push_button")
        self.inspection_settings_label = QtWidgets.QLabel(self.frame)
        self.inspection_settings_label.setGeometry(QtCore.QRect(90, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.inspection_settings_label.setFont(font)
        self.inspection_settings_label.setObjectName("inspection_settings_label")
        self.run_push_button = QtWidgets.QPushButton(self.frame)
        self.run_push_button.setGeometry(QtCore.QRect(20, 370, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.run_push_button.setFont(font)
        self.run_push_button.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.run_push_button.setObjectName("run_push_button")
        self.stop_push_button = QtWidgets.QPushButton(self.frame)
        self.stop_push_button.setGeometry(QtCore.QRect(20, 460, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.stop_push_button.setFont(font)
        self.stop_push_button.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.stop_push_button.setObjectName("stop_push_button")
        self.defect_list = QtWidgets.QComboBox(self.frame)
        self.defect_list.setGeometry(QtCore.QRect(20, 100, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.defect_list.setFont(font)
        self.defect_list.setStyleSheet("selection-background-color: rgb(114, 159, 207);\n"
"background-color: rgb(114, 159, 207);\n"
"")
        self.defect_list.setObjectName("defect_list")
        self.defect_list.addItem("")
        self.defect_list.addItem("")
        self.defect_list.addItem("")
        self.defect_list.addItem("")
        self.defect_list.addItem("")
        self.speck_size_label = QtWidgets.QLabel(self.frame)
        self.speck_size_label.setGeometry(QtCore.QRect(10, 170, 71, 16))
        self.speck_size_label.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.speck_size_label.setTextFormat(QtCore.Qt.RichText)
        self.speck_size_label.setObjectName("speck_size_label")
        self.speck_size_slider = QtWidgets.QSlider(self.frame)
        self.speck_size_slider.setGeometry(QtCore.QRect(10, 190, 321, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.speck_size_slider.setPalette(palette)
        self.speck_size_slider.setMouseTracking(True)
        self.speck_size_slider.setTabletTracking(False)
        self.speck_size_slider.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.speck_size_slider.setMaximum(600)
        self.speck_size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speck_size_slider.setObjectName("speck_size_slider")
        self.threshold_label = QtWidgets.QLabel(self.frame)
        self.threshold_label.setGeometry(QtCore.QRect(10, 220, 71, 16))
        self.threshold_label.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.threshold_label.setObjectName("threshold_label")
        self.threshold_slider = QtWidgets.QSlider(self.frame)
        self.threshold_slider.setGeometry(QtCore.QRect(10, 240, 321, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 192, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 79, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 106, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 207, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 192, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 79, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 106, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 207, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 79, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 192, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 79, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 106, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 79, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 79, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.threshold_slider.setPalette(palette)
        self.threshold_slider.setMouseTracking(True)
        self.threshold_slider.setTabletTracking(False)
        self.threshold_slider.setStyleSheet("background-color: rgb(114, 159, 207);\n"
"font: 11pt \"Ubuntu\";")
        self.threshold_slider.setMaximum(99)
        self.threshold_slider.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_slider.setObjectName("threshold_slider")
        self.speck_size = QtWidgets.QLabel(self.frame)
        self.speck_size.setGeometry(QtCore.QRect(330, 190, 21, 21))
        self.speck_size.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.speck_size.setObjectName("speck_size")
        self.threshold = QtWidgets.QLabel(self.frame)
        self.threshold.setGeometry(QtCore.QRect(330, 240, 21, 21))
        self.threshold.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.threshold.setObjectName("threshold")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 70, 1801, 851))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.inspection_report_button = QtWidgets.QPushButton(self.frame_2)
        self.inspection_report_button.setGeometry(QtCore.QRect(1420, 670, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.inspection_report_button.setFont(font)
        self.inspection_report_button.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.inspection_report_button.setObjectName("inspection_report_button")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(71, 670, 1281, 60))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.web_speed_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.web_speed_label.setFont(font)
        self.web_speed_label.setStyleSheet("background:rgb(255,255,255)")
        self.web_speed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.web_speed_label.setObjectName("web_speed_label")
        self.verticalLayout.addWidget(self.web_speed_label)
        self.web_speed_count = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.web_speed_count.setFont(font)
        self.web_speed_count.setStyleSheet("background:rgb(114, 159, 207)")
        self.web_speed_count.setAlignment(QtCore.Qt.AlignCenter)
        self.web_speed_count.setObjectName("web_speed_count")
        self.verticalLayout.addWidget(self.web_speed_count)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.specks_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.specks_label.setFont(font)
        self.specks_label.setStyleSheet("background:rgb(255,255,255)")
        self.specks_label.setAlignment(QtCore.Qt.AlignCenter)
        self.specks_label.setObjectName("specks_label")
        self.verticalLayout_2.addWidget(self.specks_label)
        self.specks_count = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.specks_count.setFont(font)
        self.specks_count.setStyleSheet("background:rgb(114, 159, 207)")
        self.specks_count.setAlignment(QtCore.Qt.AlignCenter)
        self.specks_count.setObjectName("specks_count")
        self.verticalLayout_2.addWidget(self.specks_count)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.holes_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.holes_label.setFont(font)
        self.holes_label.setStyleSheet("background:rgb(255,255,255)")
        self.holes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.holes_label.setObjectName("holes_label")
        self.verticalLayout_3.addWidget(self.holes_label)
        self.holes_count = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.holes_count.setFont(font)
        self.holes_count.setStyleSheet("background:rgb(114, 159, 207)")
        self.holes_count.setAlignment(QtCore.Qt.AlignCenter)
        self.holes_count.setObjectName("holes_count")
        self.verticalLayout_3.addWidget(self.holes_count)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.fibers_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.fibers_label.setFont(font)
        self.fibers_label.setStyleSheet("background:rgb(255,255,255)")
        self.fibers_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fibers_label.setObjectName("fibers_label")
        self.verticalLayout_4.addWidget(self.fibers_label)
        self.fibers_count = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.fibers_count.setFont(font)
        self.fibers_count.setStyleSheet("background:rgb(114, 159, 207)")
        self.fibers_count.setAlignment(QtCore.Qt.AlignCenter)
        self.fibers_count.setObjectName("fibers_count")
        self.verticalLayout_4.addWidget(self.fibers_count)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.brightness_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.brightness_label.setFont(font)
        self.brightness_label.setStyleSheet("background:rgb(255,255,255)")
        self.brightness_label.setAlignment(QtCore.Qt.AlignCenter)
        self.brightness_label.setObjectName("brightness_label")
        self.verticalLayout_5.addWidget(self.brightness_label)
        self.brightness_count = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.brightness_count.setFont(font)
        self.brightness_count.setStyleSheet("background:rgb(114, 159, 207)")
        self.brightness_count.setAlignment(QtCore.Qt.AlignCenter)
        self.brightness_count.setObjectName("brightness_count")
        self.verticalLayout_5.addWidget(self.brightness_count)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 60, 531, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.select_roi = QtWidgets.QCheckBox(self.layoutWidget1)
        self.select_roi.setStyleSheet("font: 16pt \"Ubuntu\";\n"
"background: rgb(114, 159, 207)")
        self.select_roi.setObjectName("select_roi")
        self.horizontalLayout_4.addWidget(self.select_roi)
        self.live_feed = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.live_feed.setFont(font)
        self.live_feed.setStyleSheet("background: rgb(114, 159, 207)")
        self.live_feed.setObjectName("live_feed")
        self.horizontalLayout_4.addWidget(self.live_feed)
        self.capture_button = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.capture_button.setFont(font)
        self.capture_button.setStyleSheet("background: rgb(114, 159, 207)")
        self.capture_button.setObjectName("capture_button")
        self.horizontalLayout_4.addWidget(self.capture_button)
        self.company_logo = QtWidgets.QLabel(self.centralwidget)
        self.company_logo.setGeometry(QtCore.QRect(1600, 10, 131, 41))
        self.company_logo.setObjectName("company_logo")
        self.frame_2.raise_()
        self.liveFeed.raise_()
        self.frame.raise_()
        self.company_logo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.speck_size_slider.valueChanged['int'].connect(self.speck_size.setNum)
        self.threshold_slider.valueChanged['int'].connect(self.threshold.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.update_push_button.setText(_translate("MainWindow", "UPDATE"))
        self.inspection_settings_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">INSPECTION SETTINGS</span></p></body></html>"))
        self.run_push_button.setText(_translate("MainWindow", "RUN"))
        self.stop_push_button.setText(_translate("MainWindow", "STOP"))
        self.defect_list.setCurrentText(_translate("MainWindow", "                    DEFECT LIST"))
        self.defect_list.setItemText(0, _translate("MainWindow", "                    DEFECT LIST"))
        self.defect_list.setItemText(1, _translate("MainWindow", "                    SPECKS"))
        self.defect_list.setItemText(2, _translate("MainWindow", "                    HOLES"))
        self.defect_list.setItemText(3, _translate("MainWindow", "                    FIBER"))
        self.defect_list.setItemText(4, _translate("MainWindow", "                    ALL"))
        self.speck_size_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SPECK SIZE</span></p></body></html>"))
        self.threshold_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">THRESHOLD</span></p></body></html>"))
        self.speck_size.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.threshold.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.inspection_report_button.setText(_translate("MainWindow", "INSPECTION REPORT"))
        self.web_speed_label.setText(_translate("MainWindow", "WEB SPEED"))
        self.web_speed_count.setText(_translate("MainWindow", "100"))
        self.specks_label.setText(_translate("MainWindow", "SPECKS"))
        self.specks_count.setText(_translate("MainWindow", "100"))
        self.holes_label.setText(_translate("MainWindow", "HOLES"))
        self.holes_count.setText(_translate("MainWindow", "100"))
        self.fibers_label.setText(_translate("MainWindow", "FIBERS"))
        self.fibers_count.setText(_translate("MainWindow", "100"))
        self.brightness_label.setText(_translate("MainWindow", "BRIGHTNESS LEVEL"))
        self.brightness_count.setText(_translate("MainWindow", "100"))
        self.select_roi.setText(_translate("MainWindow", "SELECT ROI"))
        self.live_feed.setText(_translate("MainWindow", "LIVE FEED"))
        self.capture_button.setText(_translate("MainWindow", "CAPTURE"))
        self.company_logo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">YantraVision</span></p></body></html>"))
        self.capture_button.clicked.connect(self.show_image)
        self.update_push_button.clicked.connect(self.update_slider)        
        
        

        # will mark specks and holes
    def thresholding_algorithm(self , image):
        img1 = np.array(image, dtype=np.uint8)
        #print(img)
        #img1 = cv2.resize(img1, (1000, 1000),interpolation = cv2.INTER_NEAREST)
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("image",800, 600)
        cv2.imshow("image",img1)
        img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img = cv2.blur(img, (11,11),cv2.BORDER_DEFAULT) # VERY SENSITIVE
        cv2.namedWindow("B&W", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("B&W",800, 600)
        cv2.imshow("B&W",img)
        #THRESHOLDING
        global threshold
        const = (threshold * 2.1) / 100
        mean_threshold = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2.1)
        #DILATING
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 13))
        th2 = cv2.bitwise_not(mean_threshold)
        th2 = cv2.dilate(th2,kernel,iterations = 1)
        th2 = cv2.bitwise_not(th2)
        cv2.namedWindow("mean threshold", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("mean threshold",800, 600)
        cv2.imshow("mean threshold",th2)
        #FINDING CONTOURS
        cnts1 = cv2.findContours(th2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnts1 = imutils.grab_contours(cnts1)
        speck_count = 0
        hole_count = 0
        # Change the min and max sizes to identify smaller and biggers specks
        min_area_speck = speck_size
        min_area_hole = 900
        max_area_speck = speck_size+50
        max_area_hole = 20000
        for c in cnts1:
            if min_area_speck < cv2.contourArea(c)<min_area_hole:
                #cv2.drawContours(img1,[c],0,(255,0,0),2)
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(img1, (x-5, y-5), (x+w+5, y+h+5), (255, 0, 0), 2)
                speck_count += 1
            if min_area_hole<cv2.contourArea(c)<max_area_hole: #<max_area:
                #cv2.drawContours(img1,[c],0,(0,0,255),3)
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(img1, (x-5, y-5), (x+w+5, y+h+5), (0, 0, 255), 2)
                hole_count += 1
        print("number of specks = ",speck_count)
        print("number of holes = ",hole_count) 
        cv2.namedWindow("final", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("final",800, 600)
        cv2.imshow("final",img1)
        image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        height0,width0,channel0 = image1.shape
        bytes_per_line = channel0 * width0
        qImg = QtGui.QImage(image1.data, width0, height0, bytes_per_line, QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap(qImg)
        self.liveFeed.setPixmap(pix)
        self.liveFeed.setScaledContents(True)
        #img1 is the final image to be displayed
        #self.liveFeed.setPixmap(QtGui.QPixmap())
        #self.liveFeed.setScaledContents(True)
        self.specks_count.setText(str(speck_count))
        self.holes_count.setText(str(hole_count))
        self.fibers_count.setText(str(hole_count))

    def mousePressEvent(self, QMouseEvent):
        cursor_on_image = self.liveFeed.underMouse()
        roi_check_box = self.select_roi.isChecked()
        x_position = self.liveFeed.x()
        y_position =self.liveFeed.y()
        if cursor_on_image and roi_check_box and QMouseEvent.buttons() == QtCore.Qt.LeftButton:
            x = QMouseEvent.x() - x_position + 1 
            y = QMouseEvent.y() - y_position + 1
            print(x," ",y)
            global points_of_interest
            points_of_interest.append((x , y))
            print(points_of_interest)
            if len(points_of_interest) >= 4:
                self.select_roi.setChecked(False)
                width = self.liveFeed.width()
                height = self.liveFeed.height()
                image = cv2.imread("/home/srikar/paper/CAM1/imageCaptureCAM0_2.bmp") # CAN CHANGE
                orig_width = image.shape[0]
                orig_height = image.shape[1]
                #new_value = ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min
                #or0 = old row 0 nr = new row
                #oc0 = old column 0 nc = new column
                or0 = points_of_interest[0][1]
                or1 = points_of_interest[3][1]
                oc0 =  points_of_interest[0][0]
                oc1 = points_of_interest[1][0]

                nr0 = int(((or0)/(height))*(orig_height))
                nr1 = int(((or1)/(height))*(orig_height))
                nc0 = int(((oc0)/(width))*(orig_width))
                nc1 = int(((oc1)/(width))*(orig_width))
                image = image[nr0:nr1 ,nc0:nc1]
                #cv2.imwrite("/home/srikar/paper/CAM0/liveFeed.bmp",image)
                image1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                height0,width0,channel0 = image1.shape
                bytes_per_line = channel0 * width0
                qImg = QtGui.QImage(image1.data, width0, height0, bytes_per_line, QtGui.QImage.Format_RGB888)
                pix = QtGui.QPixmap(qImg)
                self.liveFeed.setPixmap(pix)
                #self.liveFeed.setPixmap(QtGui.QPixmap(image1)) #DONT CHANGE 
                self.liveFeed.setScaledContents(True)
                self.thresholding_algorithm(image)
                points_of_interest.clear() #DONT FORGET TO ADD A KEYSTROKE FOR CLEARING POINTS_OF_INTEREST
                
    # will display image in liveFeed
    def show_image(self):
        image_path = "/home/srikar/paper/CAM1/imageCaptureCAM0_2.bmp" # CAN CHANGE
        self.liveFeed.setPixmap(QtGui.QPixmap(image_path))
        self.liveFeed.setScaledContents(True)

    def update_slider(self):
        global speck_size
        speck_size = self.speck_size_slider.value()
        global threshold
        threshold = self.threshold_slider.value()
        print("sp ", speck_size )
        print("threshold ", threshold )
        
