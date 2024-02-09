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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

from renderer.viewport import ViewPort


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1556, 815)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_universes = QLabel(self.centralwidget)
        self.label_universes.setObjectName(u"label_universes")
        self.label_universes.setGeometry(QRect(10, 10, 61, 16))
        self.button_add_universe = QPushButton(self.centralwidget)
        self.button_add_universe.setObjectName(u"button_add_universe")
        self.button_add_universe.setGeometry(QRect(10, 40, 141, 28))
        self.button_delete_universe = QPushButton(self.centralwidget)
        self.button_delete_universe.setObjectName(u"button_delete_universe")
        self.button_delete_universe.setGeometry(QRect(170, 40, 151, 28))
        self.label_properties = QLabel(self.centralwidget)
        self.label_properties.setObjectName(u"label_properties")
        self.label_properties.setGeometry(QRect(1290, 10, 58, 16))
        self.scrollarea_properties = QScrollArea(self.centralwidget)
        self.scrollarea_properties.setObjectName(u"scrollarea_properties")
        self.scrollarea_properties.setGeometry(QRect(1290, 30, 251, 751))
        self.scrollarea_properties.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 249, 749))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.properties_layout = QVBoxLayout()
        self.properties_layout.setObjectName(u"properties_layout")

        self.horizontalLayout.addLayout(self.properties_layout)

        self.scrollarea_properties.setWidget(self.scrollAreaWidgetContents)
        self.viewport_widget = QWidget(self.centralwidget)
        self.viewport_widget.setObjectName(u"viewport_widget")
        self.viewport_widget.setGeometry(QRect(344, 27, 931, 571))
        self.verticalLayout_2 = QVBoxLayout(self.viewport_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.viewport_layout = QVBoxLayout()
        self.viewport_layout.setObjectName(u"viewport_layout")

        self.verticalLayout_2.addLayout(self.viewport_layout)

        self.label_viewport = QLabel(self.centralwidget)
        self.label_viewport.setObjectName(u"label_viewport")
        self.label_viewport.setGeometry(QRect(350, 10, 51, 16))
        self.view = ViewPort()
        self.view_container = QWidget.createWindowContainer(self.view)
        self.viewport_layout.addWidget(self.view_container)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 290, 321, 301))
        self.tab_surfaces = QWidget()
        self.tab_surfaces.setObjectName(u"tab_surfaces")
        self.list_surfaces = QListWidget(self.tab_surfaces)
        self.list_surfaces.setObjectName(u"list_surfaces")
        self.list_surfaces.setGeometry(QRect(0, 60, 311, 211))
        self.button_add_surface = QPushButton(self.tab_surfaces)
        self.button_add_surface.setObjectName(u"button_add_surface")
        self.button_add_surface.setGeometry(QRect(0, 10, 141, 31))
        self.button_delete_surface = QPushButton(self.tab_surfaces)
        self.button_delete_surface.setObjectName(u"button_delete_surface")
        self.button_delete_surface.setGeometry(QRect(160, 10, 151, 31))
        self.tabWidget.addTab(self.tab_surfaces, "")
        self.tab_materials = QWidget()
        self.tab_materials.setObjectName(u"tab_materials")
        self.list_materials = QListWidget(self.tab_materials)
        self.list_materials.setObjectName(u"list_materials")
        self.list_materials.setGeometry(QRect(0, 60, 311, 211))
        self.button_add_material = QPushButton(self.tab_materials)
        self.button_add_material.setObjectName(u"button_add_material")
        self.button_add_material.setGeometry(QRect(0, 10, 141, 31))
        self.button_delete_material = QPushButton(self.tab_materials)
        self.button_delete_material.setObjectName(u"button_delete_material")
        self.button_delete_material.setGeometry(QRect(160, 10, 151, 31))
        self.tabWidget.addTab(self.tab_materials, "")
        self.tab_pins = QWidget()
        self.tab_pins.setObjectName(u"tab_pins")
        self.list_pins = QListWidget(self.tab_pins)
        self.list_pins.setObjectName(u"list_pins")
        self.list_pins.setGeometry(QRect(0, 60, 311, 211))
        self.button_add_pin = QPushButton(self.tab_pins)
        self.button_add_pin.setObjectName(u"button_add_pin")
        self.button_add_pin.setGeometry(QRect(0, 10, 141, 31))
        self.button_delete_pin = QPushButton(self.tab_pins)
        self.button_delete_pin.setObjectName(u"button_delete_pin")
        self.button_delete_pin.setGeometry(QRect(160, 10, 151, 31))
        self.tabWidget.addTab(self.tab_pins, "")
        self.tree_universes = QTreeWidget(self.centralwidget)
        self.tree_universes.setObjectName(u"tree_universes")
        self.tree_universes.setGeometry(QRect(10, 80, 311, 192))
        self.tab_widget_2 = QTabWidget(self.centralwidget)
        self.tab_widget_2.setObjectName(u"tab_widget_2")
        self.tab_widget_2.setGeometry(QRect(10, 600, 1251, 181))
        self.tab_file_explorer = QWidget()
        self.tab_file_explorer.setObjectName(u"tab_file_explorer")
        self.tab_widget_2.addTab(self.tab_file_explorer, "")
        self.tab_terminal = QWidget()
        self.tab_terminal.setObjectName(u"tab_terminal")
        self.tab_widget_2.addTab(self.tab_terminal, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.view.show()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1556, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.tab_widget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_universes.setText(QCoreApplication.translate("MainWindow", u"Universes", None))
        self.button_add_universe.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_delete_universe.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_properties.setText(QCoreApplication.translate("MainWindow", u"Properties", None))
        self.label_viewport.setText(QCoreApplication.translate("MainWindow", u"Viewport", None))
        self.button_add_surface.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_delete_surface.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_surfaces), QCoreApplication.translate("MainWindow", u"Surfaces", None))
        self.button_add_material.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_delete_material.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_materials), QCoreApplication.translate("MainWindow", u"Materials", None))
        self.button_add_pin.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_delete_pin.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pins), QCoreApplication.translate("MainWindow", u"Pins", None))
        self.tab_widget_2.setTabText(self.tab_widget_2.indexOf(self.tab_file_explorer), QCoreApplication.translate("MainWindow", u"File Explorer", None))
        self.tab_widget_2.setTabText(self.tab_widget_2.indexOf(self.tab_terminal), QCoreApplication.translate("MainWindow", u"Terminal", None))
    # retranslateUi

