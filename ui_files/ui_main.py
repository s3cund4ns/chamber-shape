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
    QPushButton, QScrollArea, QSizePolicy, QTreeView,
    QVBoxLayout, QWidget)

from renderer.viewport import ViewPort


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1059, 815)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_cells = QLabel(self.centralwidget)
        self.label_cells.setObjectName(u"label_cells")
        self.label_cells.setGeometry(QRect(11, 11, 27, 16))
        self.button_add_cell = QPushButton(self.centralwidget)
        self.button_add_cell.setObjectName(u"button_add_cell")
        self.button_add_cell.setGeometry(QRect(74, 16, 93, 28))
        self.button_delete_cell = QPushButton(self.centralwidget)
        self.button_delete_cell.setObjectName(u"button_delete_cell")
        self.button_delete_cell.setGeometry(QRect(174, 16, 93, 28))
        self.label_properties = QLabel(self.centralwidget)
        self.label_properties.setObjectName(u"label_properties")
        self.label_properties.setGeometry(QRect(790, 4, 58, 16))
        self.tree_cells = QTreeView(self.centralwidget)
        self.tree_cells.setObjectName(u"tree_cells")
        self.tree_cells.setGeometry(QRect(11, 57, 256, 192))
        self.label_surfaces = QLabel(self.centralwidget)
        self.label_surfaces.setObjectName(u"label_surfaces")
        self.label_surfaces.setGeometry(QRect(11, 404, 50, 16))
        self.button_add_surface = QPushButton(self.centralwidget)
        self.button_add_surface.setObjectName(u"button_add_surface")
        self.button_add_surface.setGeometry(QRect(74, 404, 93, 28))
        self.button_delete_surface = QPushButton(self.centralwidget)
        self.button_delete_surface.setObjectName(u"button_delete_surface")
        self.button_delete_surface.setGeometry(QRect(174, 404, 93, 28))
        self.list_surfaces = QListWidget(self.centralwidget)
        self.list_surfaces.setObjectName(u"list_surfaces")
        self.list_surfaces.setGeometry(QRect(11, 439, 256, 192))
        self.scrollarea_properties = QScrollArea(self.centralwidget)
        self.scrollarea_properties.setObjectName(u"scrollarea_properties")
        self.scrollarea_properties.setGeometry(QRect(790, 50, 251, 731))
        self.scrollarea_properties.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 249, 729))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.properties_layout = QVBoxLayout()
        self.properties_layout.setObjectName(u"properties_layout")

        self.horizontalLayout.addLayout(self.properties_layout)

        self.scrollarea_properties.setWidget(self.scrollAreaWidgetContents)
        self.viewport_widget = QWidget(self.centralwidget)
        self.viewport_widget.setObjectName(u"viewport_widget")
        self.viewport_widget.setGeometry(QRect(274, 57, 511, 551))
        self.verticalLayout_2 = QVBoxLayout(self.viewport_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.viewport_layout = QVBoxLayout()
        self.viewport_layout.setObjectName(u"viewport_layout")

        self.verticalLayout_2.addLayout(self.viewport_layout)

        self.label_viewport = QLabel(self.centralwidget)
        self.label_viewport.setObjectName(u"label_viewport")
        self.label_viewport.setGeometry(QRect(274, 34, 51, 16))

        self.view = ViewPort()
        self.view_container = QWidget.createWindowContainer(self.view)
        self.viewport_layout.addWidget(self.view_container)
        MainWindow.setCentralWidget(self.centralwidget)
        self.view.show()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1059, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_cells.setText(QCoreApplication.translate("MainWindow", u"Cells", None))
        self.button_add_cell.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_delete_cell.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_properties.setText(QCoreApplication.translate("MainWindow", u"Properties", None))
        self.label_surfaces.setText(QCoreApplication.translate("MainWindow", u"Surfaces", None))
        self.button_add_surface.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_delete_surface.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_viewport.setText(QCoreApplication.translate("MainWindow", u"Viewport", None))
    # retranslateUi

