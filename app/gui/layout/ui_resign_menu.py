# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resign_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_resign_menu(object):
    def setupUi(self, resign_menu):
        if not resign_menu.objectName():
            resign_menu.setObjectName(u"resign_menu")
        resign_menu.resize(286, 183)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(resign_menu.sizePolicy().hasHeightForWidth())
        resign_menu.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(resign_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(resign_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, 10, 25, 10)
        self.icon_contianer = QFrame(self.frame)
        self.icon_contianer.setObjectName(u"icon_contianer")
        self.icon_contianer.setFrameShape(QFrame.NoFrame)
        self.icon_contianer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.icon_contianer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon = QLabel(self.icon_contianer)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(40, 40))
        self.icon.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.icon)


        self.verticalLayout_2.addWidget(self.icon_contianer)

        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)

        self.button_container = QFrame(self.frame)
        self.button_container.setObjectName(u"button_container")
        self.button_container.setFrameShape(QFrame.NoFrame)
        self.button_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.button_container)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_button = QPushButton(self.button_container)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 30))
        self.cancel_button.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.cancel_button)

        self.resign_button = QPushButton(self.button_container)
        self.resign_button.setObjectName(u"resign_button")
        self.resign_button.setMinimumSize(QSize(0, 30))
        self.resign_button.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.resign_button)


        self.verticalLayout_2.addWidget(self.button_container)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(resign_menu)

        QMetaObject.connectSlotsByName(resign_menu)
    # setupUi

    def retranslateUi(self, resign_menu):
        resign_menu.setWindowTitle(QCoreApplication.translate("resign_menu", u"Dialog", None))
        self.icon.setText("")
        self.title.setText(QCoreApplication.translate("resign_menu", u"Are you sure you want to resign?", None))
        self.cancel_button.setText(QCoreApplication.translate("resign_menu", u"Cancel", None))
        self.resign_button.setText(QCoreApplication.translate("resign_menu", u"Resign", None))
    # retranslateUi

