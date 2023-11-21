# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

from renderer.viewport import ViewPort


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1138, 833)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_surfaces = QLabel(self.centralwidget)
        self.label_surfaces.setObjectName(u"label_surfaces")
        self.label_surfaces.setGeometry(QRect(30, 30, 55, 16))
        self.button_add_surface = QPushButton(self.centralwidget)
        self.button_add_surface.setObjectName(u"button_add_surface")
        self.button_add_surface.setGeometry(QRect(100, 20, 31, 28))
        self.button_delete_surface = QPushButton(self.centralwidget)
        self.button_delete_surface.setObjectName(u"button_delete_surface")
        self.button_delete_surface.setGeometry(QRect(140, 20, 31, 28))
        self.scrollarea_properties = QScrollArea(self.centralwidget)
        self.scrollarea_properties.setObjectName(u"scrollarea_properties")
        self.scrollarea_properties.setGeometry(QRect(840, 60, 291, 741))
        self.scrollarea_properties.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 289, 739))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.properties_layout = QVBoxLayout()
        self.properties_layout.setObjectName(u"properties_layout")

        self.horizontalLayout.addLayout(self.properties_layout)

        self.scrollarea_properties.setWidget(self.scrollAreaWidgetContents)
        self.label_properties = QLabel(self.centralwidget)
        self.label_properties.setObjectName(u"label_properties")
        self.label_properties.setGeometry(QRect(840, 40, 66, 16))
        self.list_surfaces = QListWidget(self.centralwidget)
        self.list_surfaces.setObjectName(u"list_surfaces")
        self.list_surfaces.setGeometry(QRect(20, 60, 301, 741))
        self.viewport = ViewPort(self.centralwidget)
        self.viewport.setObjectName(u"viewport")
        self.viewport.setGeometry(QRect(340, 60, 481, 541))
        self.label_viewport = QLabel(self.centralwidget)
        self.label_viewport.setObjectName(u"label_viewport")
        self.label_viewport.setGeometry(QRect(340, 30, 66, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1138, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_surfaces.setText(QCoreApplication.translate("MainWindow", u"Surfaces", None))
        self.button_add_surface.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_delete_surface.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_properties.setText(QCoreApplication.translate("MainWindow", u"Properties", None))
        self.label_viewport.setText(QCoreApplication.translate("MainWindow", u"ViewPort", None))
    # retranslateUi

