# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'property_float.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class UiPropertyFloat(object):
    def setupUi(self, property_float):
        if not property_string.objectName():
            property_string.setObjectName(u"property_float")
        property_string.resize(144, 46)
        self.verticalLayout = QVBoxLayout(property_string)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setObjectName(u"horizontal_layout")
        self.name = QLabel(property_string)
        self.name.setObjectName(u"name")

        self.horizontal_layout.addWidget(self.name)

        self.doubleSpinBox = QDoubleSpinBox(property_string)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontal_layout.addWidget(self.doubleSpinBox)


        self.verticalLayout.addLayout(self.horizontal_layout)


        self.retranslateUi(property_string)

        QMetaObject.connectSlotsByName(property_string)
    # setupUi

    def retranslateUi(self, property_string):
        property_string.setWindowTitle(QCoreApplication.translate("property_string", u"Form", None))
        self.name.setText(QCoreApplication.translate("property_string", u"TextLabel", None))
    # retranslateUi

