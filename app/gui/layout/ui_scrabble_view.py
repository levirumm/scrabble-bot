# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scrabble_view.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ScrabbleView(object):
    def setupUi(self, ScrabbleView):
        if not ScrabbleView.objectName():
            ScrabbleView.setObjectName(u"ScrabbleView")
        ScrabbleView.resize(886, 304)
        self.horizontal_layout = QHBoxLayout(ScrabbleView)
        self.horizontal_layout.setSpacing(0)
        self.horizontal_layout.setObjectName(u"horizontal_layout")
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout.addItem(self.horizontalSpacer)

        self.left_bar = QFrame(ScrabbleView)
        self.left_bar.setObjectName(u"left_bar")
        self.left_bar.setMinimumSize(QSize(0, 0))
        self.left_bar.setMaximumSize(QSize(16777215, 16777215))
        self.left_bar.setStyleSheet(u"")
        self.left_bar.setFrameShape(QFrame.NoFrame)
        self.left_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.left_bar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 18, 10, 18)
        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.button_console = QFrame(self.left_bar)
        self.button_console.setObjectName(u"button_console")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_console.sizePolicy().hasHeightForWidth())
        self.button_console.setSizePolicy(sizePolicy)
        self.button_console.setMinimumSize(QSize(64, 0))
        self.button_console.setMaximumSize(QSize(64, 16777215))
        self.button_console.setFrameShape(QFrame.StyledPanel)
        self.button_console.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.button_console)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.button_console_layout = QVBoxLayout()
        self.button_console_layout.setSpacing(20)
        self.button_console_layout.setObjectName(u"button_console_layout")
        self.button_console_layout.setContentsMargins(0, 0, 0, 0)
        self.info_icon = QPushButton(self.button_console)
        self.info_icon.setObjectName(u"info_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.info_icon.sizePolicy().hasHeightForWidth())
        self.info_icon.setSizePolicy(sizePolicy1)
        self.info_icon.setMinimumSize(QSize(44, 44))
        self.info_icon.setMaximumSize(QSize(44, 44))
        self.info_icon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.button_console_layout.addWidget(self.info_icon)

        self.dictionary_icon = QPushButton(self.button_console)
        self.dictionary_icon.setObjectName(u"dictionary_icon")
        sizePolicy1.setHeightForWidth(self.dictionary_icon.sizePolicy().hasHeightForWidth())
        self.dictionary_icon.setSizePolicy(sizePolicy1)
        self.dictionary_icon.setMinimumSize(QSize(44, 44))
        self.dictionary_icon.setMaximumSize(QSize(44, 44))
        self.dictionary_icon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.button_console_layout.addWidget(self.dictionary_icon)

        self.peek_icon = QPushButton(self.button_console)
        self.peek_icon.setObjectName(u"peek_icon")
        sizePolicy1.setHeightForWidth(self.peek_icon.sizePolicy().hasHeightForWidth())
        self.peek_icon.setSizePolicy(sizePolicy1)
        self.peek_icon.setMinimumSize(QSize(44, 44))
        self.peek_icon.setMaximumSize(QSize(44, 44))
        self.peek_icon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.button_console_layout.addWidget(self.peek_icon)

        self.hint_icon = QPushButton(self.button_console)
        self.hint_icon.setObjectName(u"hint_icon")
        sizePolicy1.setHeightForWidth(self.hint_icon.sizePolicy().hasHeightForWidth())
        self.hint_icon.setSizePolicy(sizePolicy1)
        self.hint_icon.setMinimumSize(QSize(44, 44))
        self.hint_icon.setMaximumSize(QSize(44, 44))
        self.hint_icon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.button_console_layout.addWidget(self.hint_icon)


        self.horizontalLayout_7.addLayout(self.button_console_layout)


        self.verticalLayout_7.addWidget(self.button_console)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontal_layout.addWidget(self.left_bar)

        self.h_spacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout.addItem(self.h_spacer_1)

        self.game_area_container = QFrame(ScrabbleView)
        self.game_area_container.setObjectName(u"game_area_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.game_area_container.sizePolicy().hasHeightForWidth())
        self.game_area_container.setSizePolicy(sizePolicy2)
        self.game_area_container.setFrameShape(QFrame.NoFrame)
        self.game_area_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.game_area_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.board_container = QFrame(self.game_area_container)
        self.board_container.setObjectName(u"board_container")
        self.board_container.setFrameShape(QFrame.NoFrame)
        self.board_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.board_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setSizeConstraint(QLayout.SetFixedSize)

        self.verticalLayout_2.addLayout(self.grid_layout)


        self.verticalLayout.addWidget(self.board_container)

        self.v_spacer_1 = QSpacerItem(20, 116, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.v_spacer_1)

        self.tile_container_outer = QFrame(self.game_area_container)
        self.tile_container_outer.setObjectName(u"tile_container_outer")
        sizePolicy2.setHeightForWidth(self.tile_container_outer.sizePolicy().hasHeightForWidth())
        self.tile_container_outer.setSizePolicy(sizePolicy2)
        self.tile_container_outer.setFrameShape(QFrame.NoFrame)
        self.tile_container_outer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.tile_container_outer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.h_spacer_3 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.h_spacer_3)

        self.letter_rack = QFrame(self.tile_container_outer)
        self.letter_rack.setObjectName(u"letter_rack")
        self.letter_rack.setFrameShape(QFrame.StyledPanel)
        self.letter_rack.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.letter_rack)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.letter_rack_layout = QHBoxLayout()
        self.letter_rack_layout.setSpacing(12)
        self.letter_rack_layout.setObjectName(u"letter_rack_layout")

        self.verticalLayout_8.addLayout(self.letter_rack_layout)


        self.horizontalLayout.addWidget(self.letter_rack)

        self.h_spacer_4 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.h_spacer_4)


        self.verticalLayout.addWidget(self.tile_container_outer)

        self.v_spacer_2 = QSpacerItem(20, 116, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.v_spacer_2)

        self.button_container = QFrame(self.game_area_container)
        self.button_container.setObjectName(u"button_container")
        self.button_container.setFrameShape(QFrame.NoFrame)
        self.button_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.button_container)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.button_panel_layout = QHBoxLayout()
        self.button_panel_layout.setSpacing(0)
        self.button_panel_layout.setObjectName(u"button_panel_layout")
        self.resign_button = QPushButton(self.button_container)
        self.resign_button.setObjectName(u"resign_button")
        sizePolicy1.setHeightForWidth(self.resign_button.sizePolicy().hasHeightForWidth())
        self.resign_button.setSizePolicy(sizePolicy1)
        self.resign_button.setMinimumSize(QSize(100, 38))
        self.resign_button.setMaximumSize(QSize(100, 38))
        self.resign_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.resign_button.setFocusPolicy(Qt.NoFocus)

        self.button_panel_layout.addWidget(self.resign_button)

        self.skip_button = QPushButton(self.button_container)
        self.skip_button.setObjectName(u"skip_button")
        sizePolicy1.setHeightForWidth(self.skip_button.sizePolicy().hasHeightForWidth())
        self.skip_button.setSizePolicy(sizePolicy1)
        self.skip_button.setMinimumSize(QSize(100, 38))
        self.skip_button.setMaximumSize(QSize(100, 38))
        self.skip_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.skip_button.setFocusPolicy(Qt.NoFocus)

        self.button_panel_layout.addWidget(self.skip_button)

        self.swap_button = QPushButton(self.button_container)
        self.swap_button.setObjectName(u"swap_button")
        sizePolicy1.setHeightForWidth(self.swap_button.sizePolicy().hasHeightForWidth())
        self.swap_button.setSizePolicy(sizePolicy1)
        self.swap_button.setMinimumSize(QSize(100, 38))
        self.swap_button.setMaximumSize(QSize(100, 38))
        self.swap_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.swap_button.setFocusPolicy(Qt.WheelFocus)

        self.button_panel_layout.addWidget(self.swap_button)

        self.submit_button = QPushButton(self.button_container)
        self.submit_button.setObjectName(u"submit_button")
        sizePolicy1.setHeightForWidth(self.submit_button.sizePolicy().hasHeightForWidth())
        self.submit_button.setSizePolicy(sizePolicy1)
        self.submit_button.setMinimumSize(QSize(100, 38))
        self.submit_button.setMaximumSize(QSize(100, 38))
        self.submit_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.submit_button.setFocusPolicy(Qt.WheelFocus)

        self.button_panel_layout.addWidget(self.submit_button)


        self.verticalLayout_5.addLayout(self.button_panel_layout)


        self.verticalLayout.addWidget(self.button_container)


        self.horizontal_layout.addWidget(self.game_area_container)

        self.h_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout.addItem(self.h_spacer_2)

        self.info_panel_outer = QFrame(ScrabbleView)
        self.info_panel_outer.setObjectName(u"info_panel_outer")
        self.info_panel_outer.setMinimumSize(QSize(400, 0))
        self.info_panel_outer.setStyleSheet(u"")
        self.info_panel_outer.setFrameShape(QFrame.NoFrame)
        self.info_panel_outer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.info_panel_outer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 18, 10, 18)
        self.info_panel_inner = QFrame(self.info_panel_outer)
        self.info_panel_inner.setObjectName(u"info_panel_inner")
        self.info_panel_inner.setFrameShape(QFrame.NoFrame)
        self.info_panel_inner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.info_panel_inner)
        self.verticalLayout_4.setSpacing(17)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.score_box_container = QFrame(self.info_panel_inner)
        self.score_box_container.setObjectName(u"score_box_container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.score_box_container.sizePolicy().hasHeightForWidth())
        self.score_box_container.setSizePolicy(sizePolicy3)
        self.score_box_container.setFrameShape(QFrame.NoFrame)
        self.score_box_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.score_box_container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.player_score_box = QFrame(self.score_box_container)
        self.player_score_box.setObjectName(u"player_score_box")
        self.player_score_box.setFrameShape(QFrame.NoFrame)
        self.player_score_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.player_score_box)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.player_score_layout = QVBoxLayout()
        self.player_score_layout.setObjectName(u"player_score_layout")

        self.horizontalLayout_5.addLayout(self.player_score_layout)


        self.horizontalLayout_2.addWidget(self.player_score_box)

        self.line = QFrame(self.score_box_container)
        self.line.setObjectName(u"line")
        sizePolicy3.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy3)
        self.line.setMinimumSize(QSize(2, 0))
        self.line.setMaximumSize(QSize(2, 16777215))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.line)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.line)

        self.bot_score_box = QFrame(self.score_box_container)
        self.bot_score_box.setObjectName(u"bot_score_box")
        self.bot_score_box.setFrameShape(QFrame.NoFrame)
        self.bot_score_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.bot_score_box)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bot_score_layout = QVBoxLayout()
        self.bot_score_layout.setObjectName(u"bot_score_layout")

        self.horizontalLayout_4.addLayout(self.bot_score_layout)


        self.horizontalLayout_2.addWidget(self.bot_score_box)


        self.verticalLayout_4.addWidget(self.score_box_container)

        self.tile_tracker_container = QFrame(self.info_panel_inner)
        self.tile_tracker_container.setObjectName(u"tile_tracker_container")
        self.tile_tracker_container.setFrameShape(QFrame.NoFrame)
        self.tile_tracker_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.tile_tracker_container)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.tile_bag_tracker = QLabel(self.tile_tracker_container)
        self.tile_bag_tracker.setObjectName(u"tile_bag_tracker")

        self.horizontalLayout_3.addWidget(self.tile_bag_tracker)


        self.verticalLayout_4.addWidget(self.tile_tracker_container)

        self.turn_history_container = QFrame(self.info_panel_inner)
        self.turn_history_container.setObjectName(u"turn_history_container")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.turn_history_container.sizePolicy().hasHeightForWidth())
        self.turn_history_container.setSizePolicy(sizePolicy4)
        self.turn_history_container.setFrameShape(QFrame.NoFrame)
        self.turn_history_container.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.turn_history_container)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.turn_history_label = QLabel(self.turn_history_container)
        self.turn_history_label.setObjectName(u"turn_history_label")

        self.verticalLayout_6.addWidget(self.turn_history_label)

        self.line_2 = QFrame(self.turn_history_container)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 1))
        self.line_2.setMaximumSize(QSize(16777215, 1))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Plain)

        self.verticalLayout_6.addWidget(self.line_2)

        self.scroll_area_container = QFrame(self.turn_history_container)
        self.scroll_area_container.setObjectName(u"scroll_area_container")
        self.scroll_area_container.setFrameShape(QFrame.NoFrame)
        self.scroll_area_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.scroll_area_container)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 10, 0, 0)
        self.scroll_area = QScrollArea(self.scroll_area_container)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll = QWidget()
        self.scroll.setObjectName(u"scroll")
        self.scroll.setGeometry(QRect(0, 0, 330, 107))
        self.verticalLayout_11 = QVBoxLayout(self.scroll)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.setSpacing(0)
        self.scroll_layout.setObjectName(u"scroll_layout")

        self.verticalLayout_11.addLayout(self.scroll_layout)

        self.scroll_area.setWidget(self.scroll)

        self.verticalLayout_10.addWidget(self.scroll_area)


        self.verticalLayout_6.addWidget(self.scroll_area_container)


        self.verticalLayout_4.addWidget(self.turn_history_container)


        self.verticalLayout_3.addWidget(self.info_panel_inner)


        self.horizontal_layout.addWidget(self.info_panel_outer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(ScrabbleView)

        QMetaObject.connectSlotsByName(ScrabbleView)
    # setupUi

    def retranslateUi(self, ScrabbleView):
        ScrabbleView.setWindowTitle(QCoreApplication.translate("ScrabbleView", u"Form", None))
#if QT_CONFIG(tooltip)
        self.info_icon.setToolTip(QCoreApplication.translate("ScrabbleView", u"View game info", None))
#endif // QT_CONFIG(tooltip)
        self.info_icon.setText("")
#if QT_CONFIG(tooltip)
        self.dictionary_icon.setToolTip(QCoreApplication.translate("ScrabbleView", u"Look up a word", None))
#endif // QT_CONFIG(tooltip)
        self.dictionary_icon.setText("")
#if QT_CONFIG(tooltip)
        self.peek_icon.setToolTip(QCoreApplication.translate("ScrabbleView", u"Peek at the bot\u2019s letter rack", None))
#endif // QT_CONFIG(tooltip)
        self.peek_icon.setText("")
#if QT_CONFIG(tooltip)
        self.hint_icon.setToolTip(QCoreApplication.translate("ScrabbleView", u"Suggest a strong move", None))
#endif // QT_CONFIG(tooltip)
        self.hint_icon.setText("")
#if QT_CONFIG(tooltip)
        self.resign_button.setToolTip(QCoreApplication.translate("ScrabbleView", u"End the game", None))
#endif // QT_CONFIG(tooltip)
        self.resign_button.setText(QCoreApplication.translate("ScrabbleView", u"Resign", None))
#if QT_CONFIG(tooltip)
        self.skip_button.setToolTip(QCoreApplication.translate("ScrabbleView", u"Skip your turn", None))
#endif // QT_CONFIG(tooltip)
        self.skip_button.setText(QCoreApplication.translate("ScrabbleView", u"Skip", None))
#if QT_CONFIG(tooltip)
        self.swap_button.setToolTip(QCoreApplication.translate("ScrabbleView", u"Swap tiles of you choice", None))
#endif // QT_CONFIG(tooltip)
        self.swap_button.setText(QCoreApplication.translate("ScrabbleView", u"Swap", None))
#if QT_CONFIG(tooltip)
        self.submit_button.setToolTip(QCoreApplication.translate("ScrabbleView", u"Submit your move", None))
#endif // QT_CONFIG(tooltip)
        self.submit_button.setText(QCoreApplication.translate("ScrabbleView", u"Submit", None))
        self.tile_bag_tracker.setText("")
        self.turn_history_label.setText(QCoreApplication.translate("ScrabbleView", u"Turn History", None))
    # retranslateUi

