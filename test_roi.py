import cv2 as cv
import numpy as np
import argparse
from matplotlib import pyplot as plt
import imutils
from PyQt5 import QtCore, QtGui, QtWidgets

global speck_size
global points_of_interest
"""
print("width of image = ",img.shape[0],"height of image = ",img.shape[1])
height=img.shape[0]
width =img.shape[1]

#THRESHOLDING
mean_threshold = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2.1)

#DILATING
kernel = cv.getStructuringElement(cv.MORPH_RECT, (13, 13))
th2 = cv.bitwise_not(mean_threshold)
th2 = cv.dilate(th2,kernel,iterations = 1)
th2 = cv.bitwise_not(th2)

#FINDING CONTOURS
cnts1 = cv.findContours(th2,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cnts1 = imutils.grab_contours(cnts1)
speck_count = 0
hole_count = 0

# Change the min and max sizes to identify smaller and biggers specks
min_area_speck = 1
min_area_hole = 1200
max_area_speck = 1000
max_area_hole = 2000
for c in cnts1:
    if min_area_speck < cv.contourArea(c) < max_area_hole:
        #cv.drawContours(img1,[c],0,(255,0,0),2)
        x,y,w,h = cv.boundingRect(c)
        cv.rectangle(img1, (x-5, y-5), (x+w+5, y+h+5), (255, 0, 0), 2)
        speck_count += 1
    if min_area_hole<cv.contourArea(c): #<max_area:
        #cv.drawContours(img1,[c],0,(0,0,255),3)
        x,y,w,h = cv.boundingRect(c)
        cv.rectangle(img1, (x-5, y-5), (x+w+5, y+h+5), (0, 0, 255), 2)
        hole_count += 1
print("number of specks = ",speck_count)
print("number of holes = ",hole_count)
#img1 is the final image to be displayed
"""
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
        self.test = QtWidgets.QPushButton(self.frame)
        self.test.setGeometry(QtCore.QRect(20, 280, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.test.setFont(font)
        self.test.setStyleSheet("background: rgb(114, 159, 207)")
        self.test.setObjectName("test")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(90, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.test_2 = QtWidgets.QPushButton(self.frame)
        self.test_2.setGeometry(QtCore.QRect(20, 370, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.test_2.setFont(font)
        self.test_2.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.test_2.setObjectName("test_2")
        self.test_3 = QtWidgets.QPushButton(self.frame)
        self.test_3.setGeometry(QtCore.QRect(20, 460, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.test_3.setFont(font)
        self.test_3.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.test_3.setObjectName("test_3")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(20, 100, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("selection-background-color: rgb(114, 159, 207);\n"
"background-color: rgb(114, 159, 207);\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 71, 16))
        self.label_4.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
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
        self.speck_size_slider.setMaximum(99)
        self.speck_size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speck_size_slider.setObjectName("speck_size_slider")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 220, 71, 16))
        self.label_9.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.label_9.setObjectName("label_9")
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
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(330, 190, 21, 21))
        self.label_10.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(330, 240, 21, 21))
        self.label_11.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.label_11.setObjectName("label_11")
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
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:rgb(255,255,255)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pass_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pass_3.setFont(font)
        self.pass_3.setStyleSheet("background:rgb(114, 159, 207)")
        self.pass_3.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_3.setObjectName("pass_3")
        self.verticalLayout.addWidget(self.pass_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background:rgb(255,255,255)")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.pass_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pass_4.setFont(font)
        self.pass_4.setStyleSheet("background:rgb(114, 159, 207)")
        self.pass_4.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_4.setObjectName("pass_4")
        self.verticalLayout_2.addWidget(self.pass_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:rgb(255,255,255)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.pass_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pass_5.setFont(font)
        self.pass_5.setStyleSheet("background:rgb(114, 159, 207)")
        self.pass_5.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_5.setObjectName("pass_5")
        self.verticalLayout_3.addWidget(self.pass_5)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background:rgb(255,255,255)")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.pass_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pass_6.setFont(font)
        self.pass_6.setStyleSheet("background:rgb(114, 159, 207)")
        self.pass_6.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_6.setObjectName("pass_6")
        self.verticalLayout_4.addWidget(self.pass_6)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background:rgb(255,255,255)")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.pass_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pass_7.setFont(font)
        self.pass_7.setStyleSheet("background:rgb(114, 159, 207)")
        self.pass_7.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_7.setObjectName("pass_7")
        self.verticalLayout_5.addWidget(self.pass_7)
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
        self.speck_size_slider.valueChanged['int'].connect(self.label_10.setNum)
        self.threshold_slider.valueChanged['int'].connect(self.label_11.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.test.setText(_translate("MainWindow", "UPDATE"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">INSPECTION SETTINGS</span></p></body></html>"))
        self.test_2.setText(_translate("MainWindow", "RUN"))
        self.test_3.setText(_translate("MainWindow", "STOP"))
        self.comboBox.setCurrentText(_translate("MainWindow", "                    DEFECT LIST"))
        self.comboBox.setItemText(0, _translate("MainWindow", "                    DEFECT LIST"))
        self.comboBox.setItemText(1, _translate("MainWindow", "                    SPECKS"))
        self.comboBox.setItemText(2, _translate("MainWindow", "                    HOLES"))
        self.comboBox.setItemText(3, _translate("MainWindow", "                    FIBER"))
        self.comboBox.setItemText(4, _translate("MainWindow", "                    ALL"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SPECK SIZE</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">THRESHOLD</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.inspection_report_button.setText(_translate("MainWindow", "INSPECTION REPORT"))
        self.label_3.setText(_translate("MainWindow", "WEB SPEED"))
        self.pass_3.setText(_translate("MainWindow", "100"))
        self.label_6.setText(_translate("MainWindow", "SPECKS"))
        self.pass_4.setText(_translate("MainWindow", "100"))
        self.label_2.setText(_translate("MainWindow", "HOLES"))
        self.pass_5.setText(_translate("MainWindow", "100"))
        self.label_7.setText(_translate("MainWindow", "FIBERS"))
        self.pass_6.setText(_translate("MainWindow", "100"))
        self.label_8.setText(_translate("MainWindow", "BRIGHTNESS LEVEL"))
        self.pass_7.setText(_translate("MainWindow", "100"))
        self.select_roi.setText(_translate("MainWindow", "SELECT ROI"))
        self.live_feed.setText(_translate("MainWindow", "LIVE FEED"))
        self.capture_button.setText(_translate("MainWindow", "CAPTURE"))
        self.capture_button.clicked.connect(self.show_image)        
        self.company_logo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">YantraVision</span></p></body></html>"))
    def mousePressEvent(self, QMouseEvent):
        cursor_on_image = self.liveFeed.underMouse()
        roi_check_box = self.select_roi.isChecked()
        x_position = self.liveFeed.x()
        y_position =self.liveFeed.y()
        if cursor_on_image and roi_check_box and QMouseEvent.buttons() == QtCore.Qt.LeftButton:
            x = QMouseEvent.x() - x_position + 1 
            y = QMouseEvent.y() - y_position + 1
            print(x," ",y)
            points_of_interest.append((x , y))
            if len(points_of_interest) == 4:
                self.select_roi.setChecked(False)
                print(point_of_interest)

    def show_image(self):
        self.liveFeed.setPixmap(QtGui.QPixmap("/home/srikar/OpenCV/parrot.jpg"))
        self.liveFeed.setScaledContents(True)
