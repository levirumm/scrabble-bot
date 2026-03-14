# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_over_menu.ui'
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

class Ui_game_over_menu(object):
    def setupUi(self, game_over_menu):
        if not game_over_menu.objectName():
            game_over_menu.setObjectName(u"game_over_menu")
        game_over_menu.resize(377, 316)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(game_over_menu.sizePolicy().hasHeightForWidth())
        game_over_menu.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(game_over_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(game_over_menu)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.label_container = QFrame(self.frame)
        self.label_container.setObjectName(u"label_container")
        self.label_container.setFrameShape(QFrame.NoFrame)
        self.label_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.label_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.label_container)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.title)

        self.resign_message = QLabel(self.label_container)
        self.resign_message.setObjectName(u"resign_message")
        self.resign_message.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.resign_message)


        self.verticalLayout_2.addWidget(self.label_container)

        self.body_container = QFrame(self.frame)
        self.body_container.setObjectName(u"body_container")
        self.body_container.setFrameShape(QFrame.NoFrame)
        self.body_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.player_score_container = QFrame(self.body_container)
        self.player_score_container.setObjectName(u"player_score_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.player_score_container.sizePolicy().hasHeightForWidth())
        self.player_score_container.setSizePolicy(sizePolicy1)
        self.player_score_container.setFrameShape(QFrame.NoFrame)
        self.player_score_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.player_score_container)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.player_score_layout = QVBoxLayout()
        self.player_score_layout.setObjectName(u"player_score_layout")

        self.horizontalLayout_3.addLayout(self.player_score_layout)


        self.horizontalLayout.addWidget(self.player_score_container)

        self.line_container = QFrame(self.body_container)
        self.line_container.setObjectName(u"line_container")
        self.line_container.setFrameShape(QFrame.NoFrame)
        self.line_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.line_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.line_container)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(1, 0))
        self.line.setMaximumSize(QSize(1, 16777215))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_5.addWidget(self.line)


        self.horizontalLayout.addWidget(self.line_container)

        self.bot_score_container = QFrame(self.body_container)
        self.bot_score_container.setObjectName(u"bot_score_container")
        sizePolicy1.setHeightForWidth(self.bot_score_container.sizePolicy().hasHeightForWidth())
        self.bot_score_container.setSizePolicy(sizePolicy1)
        self.bot_score_container.setFrameShape(QFrame.NoFrame)
        self.bot_score_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bot_score_container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bot_score_layout = QVBoxLayout()
        self.bot_score_layout.setObjectName(u"bot_score_layout")

        self.horizontalLayout_2.addLayout(self.bot_score_layout)


        self.horizontalLayout.addWidget(self.bot_score_container)


        self.verticalLayout_2.addWidget(self.body_container)

        self.button_container = QFrame(self.frame)
        self.button_container.setObjectName(u"button_container")
        self.button_container.setFrameShape(QFrame.NoFrame)
        self.button_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.button_container)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.rematch_button = QPushButton(self.button_container)
        self.rematch_button.setObjectName(u"rematch_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rematch_button.sizePolicy().hasHeightForWidth())
        self.rematch_button.setSizePolicy(sizePolicy2)
        self.rematch_button.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_4.addWidget(self.rematch_button)


        self.verticalLayout_2.addWidget(self.button_container)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(game_over_menu)

        QMetaObject.connectSlotsByName(game_over_menu)
    # setupUi

    def retranslateUi(self, game_over_menu):
        game_over_menu.setWindowTitle(QCoreApplication.translate("game_over_menu", u"Dialog", None))
        self.title.setText("")
        self.resign_message.setText("")
        self.rematch_button.setText(QCoreApplication.translate("game_over_menu", u"Play Again", None))
    # retranslateUi

