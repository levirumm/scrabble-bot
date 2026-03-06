# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'letter_select_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_letter_select(object):
    def setupUi(self, letter_select):
        if not letter_select.objectName():
            letter_select.setObjectName(u"letter_select")
        letter_select.resize(322, 315)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(letter_select.sizePolicy().hasHeightForWidth())
        letter_select.setSizePolicy(sizePolicy)
        letter_select.setSizeGripEnabled(False)
        letter_select.setModal(False)
        self.verticalLayout_2 = QVBoxLayout(letter_select)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(letter_select)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.joker_label_container = QFrame(self.frame)
        self.joker_label_container.setObjectName(u"joker_label_container")
        self.joker_label_container.setFrameShape(QFrame.NoFrame)
        self.joker_label_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.joker_label_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.joker_label = QLabel(self.joker_label_container)
        self.joker_label.setObjectName(u"joker_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.joker_label.sizePolicy().hasHeightForWidth())
        self.joker_label.setSizePolicy(sizePolicy2)
        self.joker_label.setMinimumSize(QSize(40, 40))
        self.joker_label.setMaximumSize(QSize(40, 40))
        self.joker_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.joker_label)


        self.verticalLayout.addWidget(self.joker_label_container)

        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.letter_container = QFrame(self.frame)
        self.letter_container.setObjectName(u"letter_container")
        self.letter_container.setFrameShape(QFrame.NoFrame)
        self.letter_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.letter_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.letter_layout = QGridLayout()
        self.letter_layout.setSpacing(5)
        self.letter_layout.setObjectName(u"letter_layout")

        self.verticalLayout_3.addLayout(self.letter_layout)


        self.verticalLayout.addWidget(self.letter_container)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(letter_select)

        QMetaObject.connectSlotsByName(letter_select)
    # setupUi

    def retranslateUi(self, letter_select):
        letter_select.setWindowTitle(QCoreApplication.translate("letter_select", u"Dialog", None))
        self.joker_label.setText("")
        self.title.setText(QCoreApplication.translate("letter_select", u"Select Letter of Joker Tile", None))
    # retranslateUi

