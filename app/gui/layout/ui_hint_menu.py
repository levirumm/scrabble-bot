# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hint_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_hint_menu(object):
    def setupUi(self, hint_menu):
        if not hint_menu.objectName():
            hint_menu.setObjectName(u"hint_menu")
        hint_menu.resize(192, 157)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(hint_menu.sizePolicy().hasHeightForWidth())
        hint_menu.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(hint_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(hint_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)

        self.button_container = QFrame(self.frame)
        self.button_container.setObjectName(u"button_container")
        self.button_container.setFrameShape(QFrame.NoFrame)
        self.button_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.button_container)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.play_button = QPushButton(self.button_container)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setMinimumSize(QSize(0, 30))
        self.play_button.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.play_button)

        self.cancel_button = QPushButton(self.button_container)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 30))
        self.cancel_button.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.cancel_button)


        self.verticalLayout_2.addWidget(self.button_container)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(hint_menu)

        QMetaObject.connectSlotsByName(hint_menu)
    # setupUi

    def retranslateUi(self, hint_menu):
        hint_menu.setWindowTitle(QCoreApplication.translate("hint_menu", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("hint_menu", u"Play this move?", None))
        self.play_button.setText(QCoreApplication.translate("hint_menu", u"Play", None))
        self.cancel_button.setText(QCoreApplication.translate("hint_menu", u"Cancel", None))
    # retranslateUi

