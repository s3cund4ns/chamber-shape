# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QHBoxLayout,
    QMainWindow, QMenuBar, QScrollArea, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1673, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tab_main = QTabWidget(self.centralwidget)
        self.tab_main.setObjectName(u"tab_main")
        self.tab_viewport = QWidget()
        self.tab_viewport.setObjectName(u"tab_viewport")
        self.verticalLayout_6 = QVBoxLayout(self.tab_viewport)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.viewport_widget = QWidget(self.tab_viewport)
        self.viewport_widget.setObjectName(u"viewport_widget")
        self.verticalLayout_2 = QVBoxLayout(self.viewport_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.viewport_layout = QVBoxLayout()
        self.viewport_layout.setObjectName(u"viewport_layout")

        self.verticalLayout_2.addLayout(self.viewport_layout)


        self.verticalLayout_6.addWidget(self.viewport_widget)

        self.tab_main.addTab(self.tab_viewport, "")

        self.gridLayout.addWidget(self.tab_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1673, 22))
        MainWindow.setMenuBar(self.menubar)
        self.dock_universes = QDockWidget(MainWindow)
        self.dock_universes.setObjectName(u"dock_universes")
        self.dock_universes_contents = QWidget()
        self.dock_universes_contents.setObjectName(u"dock_universes_contents")
        self.verticalLayout_4 = QVBoxLayout(self.dock_universes_contents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.universes_layout = QVBoxLayout()
        self.universes_layout.setObjectName(u"universes_layout")

        self.verticalLayout_4.addLayout(self.universes_layout)

        self.dock_universes.setWidget(self.dock_universes_contents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dock_universes)
        self.dock_surfaces = QDockWidget(MainWindow)
        self.dock_surfaces.setObjectName(u"dock_surfaces")
        self.dock_surfaces_contents = QWidget()
        self.dock_surfaces_contents.setObjectName(u"dock_surfaces_contents")
        self.verticalLayout = QVBoxLayout(self.dock_surfaces_contents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.surfaces_layout = QVBoxLayout()
        self.surfaces_layout.setObjectName(u"surfaces_layout")

        self.verticalLayout.addLayout(self.surfaces_layout)

        self.dock_surfaces.setWidget(self.dock_surfaces_contents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dock_surfaces)
        self.dock_materials = QDockWidget(MainWindow)
        self.dock_materials.setObjectName(u"dock_materials")
        self.dock_materials_contents = QWidget()
        self.dock_materials_contents.setObjectName(u"dock_materials_contents")
        self.verticalLayout_5 = QVBoxLayout(self.dock_materials_contents)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.materials_layout = QVBoxLayout()
        self.materials_layout.setObjectName(u"materials_layout")

        self.verticalLayout_5.addLayout(self.materials_layout)

        self.dock_materials.setWidget(self.dock_materials_contents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dock_materials)
        self.dock_console = QDockWidget(MainWindow)
        self.dock_console.setObjectName(u"dock_console")
        self.dock_console.setMinimumSize(QSize(95, 200))
        self.dock_console_contents = QWidget()
        self.dock_console_contents.setObjectName(u"dock_console_contents")
        self.dock_console.setWidget(self.dock_console_contents)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dock_console)
        self.dock_properties = QDockWidget(MainWindow)
        self.dock_properties.setObjectName(u"dock_properties")
        self.dock_properties.setMinimumSize(QSize(300, 135))
        self.dock_properties_contents = QWidget()
        self.dock_properties_contents.setObjectName(u"dock_properties_contents")
        self.verticalLayout_3 = QVBoxLayout(self.dock_properties_contents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollarea_properties = QScrollArea(self.dock_properties_contents)
        self.scrollarea_properties.setObjectName(u"scrollarea_properties")
        self.scrollarea_properties.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 298, 616))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.properties_layout = QVBoxLayout()
        self.properties_layout.setObjectName(u"properties_layout")

        self.horizontalLayout.addLayout(self.properties_layout)

        self.scrollarea_properties.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollarea_properties)

        self.dock_properties.setWidget(self.dock_properties_contents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dock_properties)
        self.dock_detectors = QDockWidget(MainWindow)
        self.dock_detectors.setObjectName(u"dock_detectors")
        self.dock_detectors_contents = QWidget()
        self.dock_detectors_contents.setObjectName(u"dock_detectors_contents")
        self.verticalLayout_8 = QVBoxLayout(self.dock_detectors_contents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.detectors_layout = QVBoxLayout()
        self.detectors_layout.setObjectName(u"detectors_layout")

        self.verticalLayout_8.addLayout(self.detectors_layout)

        self.dock_detectors.setWidget(self.dock_detectors_contents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dock_detectors)

        self.retranslateUi(MainWindow)

        self.tab_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_viewport), QCoreApplication.translate("MainWindow", u"Viewport", None))
        self.dock_universes.setWindowTitle(QCoreApplication.translate("MainWindow", u"Universes", None))
        self.dock_surfaces.setWindowTitle(QCoreApplication.translate("MainWindow", u"Surfaces", None))
        self.dock_materials.setWindowTitle(QCoreApplication.translate("MainWindow", u"Materials", None))
        self.dock_console.setWindowTitle(QCoreApplication.translate("MainWindow", u"Console", None))
        self.dock_properties.setWindowTitle(QCoreApplication.translate("MainWindow", u"Properties", None))
        self.dock_detectors.setWindowTitle(QCoreApplication.translate("MainWindow", u"Detectors", None))
    # retranslateUi

