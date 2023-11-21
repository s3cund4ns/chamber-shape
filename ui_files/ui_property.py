# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'property.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

class UiForm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(293, 229)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gb_property = QGroupBox(Form)
        self.gb_property.setObjectName(u"gb_property")
        self.verticalLayout_2 = QVBoxLayout(self.gb_property)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.property_items_layout = QVBoxLayout()
        self.property_items_layout.setObjectName(u"property_items_layout")

        self.verticalLayout_2.addLayout(self.property_items_layout)


        self.horizontalLayout.addWidget(self.gb_property)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gb_property.setTitle(QCoreApplication.translate("Form", u"Property", None))
    # retranslateUi

