# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'turn_card.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_turn_card(object):
    def setupUi(self, turn_card):
        if not turn_card.objectName():
            turn_card.setObjectName(u"turn_card")
        turn_card.resize(400, 233)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(turn_card.sizePolicy().hasHeightForWidth())
        turn_card.setSizePolicy(sizePolicy)
        turn_card.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(turn_card)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(turn_card)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.upper_container = QFrame(self.frame)
        self.upper_container.setObjectName(u"upper_container")
        self.upper_container.setFrameShape(QFrame.NoFrame)
        self.upper_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.upper_container)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.profile_label = QLabel(self.upper_container)
        self.profile_label.setObjectName(u"profile_label")
        self.profile_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.profile_label)

        self.label_container = QFrame(self.upper_container)
        self.label_container.setObjectName(u"label_container")
        self.label_container.setFrameShape(QFrame.NoFrame)
        self.label_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.label_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.name_label = QLabel(self.label_container)
        self.name_label.setObjectName(u"name_label")

        self.verticalLayout_2.addWidget(self.name_label)

        self.turns_label = QLabel(self.label_container)
        self.turns_label.setObjectName(u"turns_label")

        self.verticalLayout_2.addWidget(self.turns_label)


        self.horizontalLayout.addWidget(self.label_container)


        self.verticalLayout_4.addWidget(self.upper_container)

        self.lower_container = QFrame(self.frame)
        self.lower_container.setObjectName(u"lower_container")
        self.lower_container.setFrameShape(QFrame.NoFrame)
        self.lower_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.lower_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.word_list = QFrame(self.lower_container)
        self.word_list.setObjectName(u"word_list")
        self.word_list.setFrameShape(QFrame.NoFrame)
        self.word_list.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.word_list)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.word_list_layout = QVBoxLayout()
        self.word_list_layout.setSpacing(4)
        self.word_list_layout.setObjectName(u"word_list_layout")

        self.horizontalLayout_2.addLayout(self.word_list_layout)


        self.verticalLayout_3.addWidget(self.word_list)

        self.points_label = QLabel(self.lower_container)
        self.points_label.setObjectName(u"points_label")
        self.points_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.points_label)


        self.verticalLayout_4.addWidget(self.lower_container)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(turn_card)

        QMetaObject.connectSlotsByName(turn_card)
    # setupUi

    def retranslateUi(self, turn_card):
        turn_card.setWindowTitle(QCoreApplication.translate("turn_card", u"Form", None))
        self.profile_label.setText("")
        self.name_label.setText(QCoreApplication.translate("turn_card", u"TextLabel", None))
        self.turns_label.setText(QCoreApplication.translate("turn_card", u"TextLabel", None))
        self.points_label.setText("")
    # retranslateUi

