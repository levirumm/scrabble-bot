# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'score_box.ui'
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

class Ui_score_box(object):
    def setupUi(self, score_box):
        if not score_box.objectName():
            score_box.setObjectName(u"score_box")
        score_box.resize(400, 80)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(score_box.sizePolicy().hasHeightForWidth())
        score_box.setSizePolicy(sizePolicy)
        score_box.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(score_box)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.name_container = QFrame(score_box)
        self.name_container.setObjectName(u"name_container")
        sizePolicy.setHeightForWidth(self.name_container.sizePolicy().hasHeightForWidth())
        self.name_container.setSizePolicy(sizePolicy)
        self.name_container.setFrameShape(QFrame.NoFrame)
        self.name_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.name_container)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.profile_label = QLabel(self.name_container)
        self.profile_label.setObjectName(u"profile_label")
        sizePolicy.setHeightForWidth(self.profile_label.sizePolicy().hasHeightForWidth())
        self.profile_label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.profile_label)

        self.name_label = QLabel(self.name_container)
        self.name_label.setObjectName(u"name_label")
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.name_label)


        self.verticalLayout.addWidget(self.name_container)

        self.line = QFrame(score_box)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 1))
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.line)

        self.score_container = QFrame(score_box)
        self.score_container.setObjectName(u"score_container")
        sizePolicy.setHeightForWidth(self.score_container.sizePolicy().hasHeightForWidth())
        self.score_container.setSizePolicy(sizePolicy)
        self.score_container.setFrameShape(QFrame.NoFrame)
        self.score_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.score_container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, -1, 2)
        self.score_label = QLabel(self.score_container)
        self.score_label.setObjectName(u"score_label")
        sizePolicy.setHeightForWidth(self.score_label.sizePolicy().hasHeightForWidth())
        self.score_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.score_label)


        self.verticalLayout.addWidget(self.score_container)


        self.retranslateUi(score_box)

        QMetaObject.connectSlotsByName(score_box)
    # setupUi

    def retranslateUi(self, score_box):
        score_box.setWindowTitle(QCoreApplication.translate("score_box", u"Form", None))
        self.profile_label.setText(QCoreApplication.translate("score_box", u"TextLabel", None))
        self.name_label.setText(QCoreApplication.translate("score_box", u"TextLabel", None))
        self.score_label.setText(QCoreApplication.translate("score_box", u"TextLabel", None))
    # retranslateUi

