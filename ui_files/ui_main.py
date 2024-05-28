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
        MainWindow.resize(1253, 675)
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
        self.menubar.setGeometry(QRect(0, 0, 1253, 26))
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
        self.dock_cells = QDockWidget(MainWindow)
        self.dock_cells.setObjectName(u"dock_cells")
        self.dock_cells.setMinimumSize(QSize(95, 200))
        self.dock_cells_contents = QWidget()
        self.dock_cells_contents.setObjectName(u"dock_cells_contents")
        self.verticalLayout_12 = QVBoxLayout(self.dock_cells_contents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.cells_layout = QVBoxLayout()
        self.cells_layout.setObjectName(u"cells_layout")

        self.verticalLayout_12.addLayout(self.cells_layout)

        self.dock_cells.setWidget(self.dock_cells_contents)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dock_cells)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 298, 302))
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
        self.verticalLayout_11 = QVBoxLayout(self.dock_detectors_contents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.detectors_layout = QVBoxLayout()
        self.detectors_layout.setObjectName(u"detectors_layout")

        self.verticalLayout_11.addLayout(self.detectors_layout)

        self.dock_detectors.setWidget(self.dock_detectors_contents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dock_detectors)
        self.dock_pins = QDockWidget(MainWindow)
        self.dock_pins.setObjectName(u"dock_pins")
        self.dock_pins_contents = QWidget()
        self.dock_pins_contents.setObjectName(u"dock_pins_contents")
        self.verticalLayout_13 = QVBoxLayout(self.dock_pins_contents)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pins_layout = QVBoxLayout()
        self.pins_layout.setObjectName(u"pins_layout")

        self.verticalLayout_13.addLayout(self.pins_layout)

        self.dock_pins.setWidget(self.dock_pins_contents)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dock_pins)
        self.dock_lattices = QDockWidget(MainWindow)
        self.dock_lattices.setObjectName(u"dock_lattices")
        self.dock_lattices_contents = QWidget()
        self.dock_lattices_contents.setObjectName(u"dock_lattices_contents")
        self.verticalLayout_14 = QVBoxLayout(self.dock_lattices_contents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lattices_layout = QVBoxLayout()
        self.lattices_layout.setObjectName(u"lattices_layout")

        self.verticalLayout_14.addLayout(self.lattices_layout)

        self.dock_lattices.setWidget(self.dock_lattices_contents)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dock_lattices)

        self.retranslateUi(MainWindow)

        self.tab_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_viewport), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.dock_universes.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043b\u0430\u0441\u0442\u0438", None))
        self.dock_surfaces.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438", None))
        self.dock_materials.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b", None))
        self.dock_cells.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u042f\u0447\u0435\u0439\u043a\u0438", None))
        self.dock_properties.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.dock_detectors.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0442\u0435\u043a\u0442\u043e\u0440\u044b", None))
        self.dock_pins.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u0440\u0436\u043d\u0438", None))
        self.dock_lattices.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0435 \u0420\u0435\u0448\u0435\u0442\u043a\u0438", None))
    # retranslateUi

