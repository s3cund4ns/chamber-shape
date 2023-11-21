# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'property_item.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class UiForm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(180, 44)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_property_item_name = QLabel(Form)
        self.label_property_item_name.setObjectName(u"label_property_item_name")

        self.horizontalLayout.addWidget(self.label_property_item_name)

        self.horizontalSpacer = QSpacerItem(23, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.dsb_property_item_value = QDoubleSpinBox(Form)
        self.dsb_property_item_value.setObjectName(u"dsb_property_item_value")
        self.dsb_property_item_value.setDecimals(4)
        self.dsb_property_item_value.setMinimum(-100.000000000000000)
        self.dsb_property_item_value.setMaximum(100.000000000000000)

        self.horizontalLayout.addWidget(self.dsb_property_item_value)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_property_item_name.setText(QCoreApplication.translate("Form", u"Property", None))
    # retranslateUi

