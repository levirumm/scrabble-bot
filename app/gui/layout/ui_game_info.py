# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_info.ui'
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
    QLabel, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_game_info(object):
    def setupUi(self, game_info):
        if not game_info.objectName():
            game_info.setObjectName(u"game_info")
        game_info.resize(445, 484)
        self.verticalLayout = QVBoxLayout(game_info)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(game_info)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 20, 15, 15)
        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QSize(0, 1))
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_5.addWidget(self.line)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scroll_area = QScrollArea(self.frame_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 370, 474))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.credit_label = QLabel(self.scrollAreaWidgetContents)
        self.credit_label.setObjectName(u"credit_label")

        self.verticalLayout_4.addWidget(self.credit_label)

        self.rules_label = QLabel(self.scrollAreaWidgetContents)
        self.rules_label.setObjectName(u"rules_label")

        self.verticalLayout_4.addWidget(self.rules_label)

        self.rules_text = QLabel(self.scrollAreaWidgetContents)
        self.rules_text.setObjectName(u"rules_text")
        self.rules_text.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.rules_text)

        self.legend_label = QLabel(self.scrollAreaWidgetContents)
        self.legend_label.setObjectName(u"legend_label")

        self.verticalLayout_4.addWidget(self.legend_label)

        self.legend_container = QFrame(self.scrollAreaWidgetContents)
        self.legend_container.setObjectName(u"legend_container")
        self.legend_container.setFrameShape(QFrame.NoFrame)
        self.legend_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.legend_container)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.triple_word_container = QFrame(self.legend_container)
        self.triple_word_container.setObjectName(u"triple_word_container")
        self.triple_word_container.setFrameShape(QFrame.NoFrame)
        self.triple_word_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.triple_word_container)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.triple_word_cell = QLabel(self.triple_word_container)
        self.triple_word_cell.setObjectName(u"triple_word_cell")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.triple_word_cell.sizePolicy().hasHeightForWidth())
        self.triple_word_cell.setSizePolicy(sizePolicy1)
        self.triple_word_cell.setMinimumSize(QSize(30, 30))
        self.triple_word_cell.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.triple_word_cell)

        self.triple_word_label = QLabel(self.triple_word_container)
        self.triple_word_label.setObjectName(u"triple_word_label")

        self.horizontalLayout.addWidget(self.triple_word_label)


        self.verticalLayout_5.addWidget(self.triple_word_container)

        self.double_word_container = QFrame(self.legend_container)
        self.double_word_container.setObjectName(u"double_word_container")
        self.double_word_container.setFrameShape(QFrame.NoFrame)
        self.double_word_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.double_word_container)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.double_word_cell = QLabel(self.double_word_container)
        self.double_word_cell.setObjectName(u"double_word_cell")
        self.double_word_cell.setMinimumSize(QSize(30, 30))
        self.double_word_cell.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.double_word_cell)

        self.double_word_label = QLabel(self.double_word_container)
        self.double_word_label.setObjectName(u"double_word_label")

        self.horizontalLayout_2.addWidget(self.double_word_label)


        self.verticalLayout_5.addWidget(self.double_word_container)

        self.triple_letter_container = QFrame(self.legend_container)
        self.triple_letter_container.setObjectName(u"triple_letter_container")
        self.triple_letter_container.setFrameShape(QFrame.NoFrame)
        self.triple_letter_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.triple_letter_container)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.triple_letter_cell = QLabel(self.triple_letter_container)
        self.triple_letter_cell.setObjectName(u"triple_letter_cell")
        self.triple_letter_cell.setMinimumSize(QSize(30, 30))
        self.triple_letter_cell.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.triple_letter_cell)

        self.triple_letter_label = QLabel(self.triple_letter_container)
        self.triple_letter_label.setObjectName(u"triple_letter_label")

        self.horizontalLayout_3.addWidget(self.triple_letter_label)


        self.verticalLayout_5.addWidget(self.triple_letter_container)

        self.double_letter_container = QFrame(self.legend_container)
        self.double_letter_container.setObjectName(u"double_letter_container")
        self.double_letter_container.setFrameShape(QFrame.NoFrame)
        self.double_letter_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.double_letter_container)
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.double_letter_cell = QLabel(self.double_letter_container)
        self.double_letter_cell.setObjectName(u"double_letter_cell")
        self.double_letter_cell.setMinimumSize(QSize(30, 30))
        self.double_letter_cell.setMaximumSize(QSize(30, 30))
        self.double_letter_cell.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_4.addWidget(self.double_letter_cell)

        self.double_letter_label = QLabel(self.double_letter_container)
        self.double_letter_label.setObjectName(u"double_letter_label")

        self.horizontalLayout_4.addWidget(self.double_letter_label)


        self.verticalLayout_5.addWidget(self.double_letter_container)


        self.verticalLayout_4.addWidget(self.legend_container)

        self.scrabble_bot_label = QLabel(self.scrollAreaWidgetContents)
        self.scrabble_bot_label.setObjectName(u"scrabble_bot_label")

        self.verticalLayout_4.addWidget(self.scrabble_bot_label)

        self.scrabble_bot_text = QLabel(self.scrollAreaWidgetContents)
        self.scrabble_bot_text.setObjectName(u"scrabble_bot_text")
        self.scrabble_bot_text.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.scrabble_bot_text)

        self.scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scroll_area)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(game_info)

        QMetaObject.connectSlotsByName(game_info)
    # setupUi

    def retranslateUi(self, game_info):
        game_info.setWindowTitle(QCoreApplication.translate("game_info", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("game_info", u"Game Info", None))
        self.credit_label.setText(QCoreApplication.translate("game_info", u"Created by Levi Rummukainen, 2026.\n"
"Uses words from the 2019 Collins Scrabble Dictionary", None))
        self.rules_label.setText(QCoreApplication.translate("game_info", u"Rules", None))
        self.rules_text.setText(QCoreApplication.translate("game_info", u"Place tiles on the board to form words. Use bonus squares to increase your score.\n"
"\n"
"The game ends when all tiles have been drawn and a player uses their last tile, or when both players pass twice in a row. Any tiles remaining in a player's rack are subtracted from their score.\n"
"\n"
"The player with the highest score wins.", None))
        self.legend_label.setText(QCoreApplication.translate("game_info", u"Legend", None))
        self.triple_word_cell.setText("")
        self.triple_word_label.setText(QCoreApplication.translate("game_info", u"Triple Word", None))
        self.double_word_cell.setText("")
        self.double_word_label.setText(QCoreApplication.translate("game_info", u"Double Word", None))
        self.triple_letter_cell.setText("")
        self.triple_letter_label.setText(QCoreApplication.translate("game_info", u"Triple Letter", None))
        self.double_letter_cell.setText("")
        self.double_letter_label.setText(QCoreApplication.translate("game_info", u"Double Letter", None))
        self.scrabble_bot_label.setText(QCoreApplication.translate("game_info", u"Scrabble Bot", None))
        self.scrabble_bot_text.setText(QCoreApplication.translate("game_info", u"The Scrabble bot uses an algorithm that searches for the highest-scoring move available. It does not use long-term strategy.\n"
"\n"
"Hints use the same algorithm.", None))
    # retranslateUi

