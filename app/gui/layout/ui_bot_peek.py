# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bot_peek.ui'
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

class Ui_bot_peek(object):
    def setupUi(self, bot_peek):
        if not bot_peek.objectName():
            bot_peek.setObjectName(u"bot_peek")
        bot_peek.resize(372, 217)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bot_peek.sizePolicy().hasHeightForWidth())
        bot_peek.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(bot_peek)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(bot_peek)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.peek_icon_container = QFrame(self.frame)
        self.peek_icon_container.setObjectName(u"peek_icon_container")
        self.peek_icon_container.setFrameShape(QFrame.NoFrame)
        self.peek_icon_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.peek_icon_container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.peek_icon = QLabel(self.peek_icon_container)
        self.peek_icon.setObjectName(u"peek_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.peek_icon.sizePolicy().hasHeightForWidth())
        self.peek_icon.setSizePolicy(sizePolicy1)
        self.peek_icon.setMinimumSize(QSize(40, 40))
        self.peek_icon.setMaximumSize(QSize(40, 40))
        self.peek_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.peek_icon)


        self.verticalLayout_2.addWidget(self.peek_icon_container)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 15, 0, 15)
        self.title = QLabel(self.frame_3)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.title)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.tile_container = QFrame(self.frame)
        self.tile_container.setObjectName(u"tile_container")
        self.tile_container.setFrameShape(QFrame.NoFrame)
        self.tile_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.tile_container)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.tile_layout = QHBoxLayout()
        self.tile_layout.setSpacing(8)
        self.tile_layout.setObjectName(u"tile_layout")

        self.horizontalLayout_3.addLayout(self.tile_layout)


        self.verticalLayout_2.addWidget(self.tile_container)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 20, 0, 5)
        self.close_button = QPushButton(self.frame_2)
        self.close_button.setObjectName(u"close_button")
        sizePolicy1.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy1)
        self.close_button.setMinimumSize(QSize(200, 33))
        self.close_button.setMaximumSize(QSize(200, 33))

        self.horizontalLayout_2.addWidget(self.close_button)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(bot_peek)

        QMetaObject.connectSlotsByName(bot_peek)
    # setupUi

    def retranslateUi(self, bot_peek):
        bot_peek.setWindowTitle(QCoreApplication.translate("bot_peek", u"Dialog", None))
        self.peek_icon.setText("")
        self.title.setText(QCoreApplication.translate("bot_peek", u"Scrabble Bot's Letter Rack", None))
        self.close_button.setText(QCoreApplication.translate("bot_peek", u"Close", None))
    # retranslateUi

