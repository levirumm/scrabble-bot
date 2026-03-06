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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ScrabbleView(object):
    def setupUi(self, ScrabbleView):
        if not ScrabbleView.objectName():
            ScrabbleView.setObjectName(u"ScrabbleView")
        ScrabbleView.resize(400, 300)
        self.horizontal_layout = QHBoxLayout(ScrabbleView)
        self.horizontal_layout.setSpacing(0)
        self.horizontal_layout.setObjectName(u"horizontal_layout")
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.side_bar_container = QFrame(ScrabbleView)
        self.side_bar_container.setObjectName(u"side_bar_container")
        self.side_bar_container.setMinimumSize(QSize(60, 0))
        self.side_bar_container.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.side_bar_container.setFrameShape(QFrame.NoFrame)
        self.side_bar_container.setFrameShadow(QFrame.Raised)

        self.horizontal_layout.addWidget(self.side_bar_container)

        self.h_spacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout.addItem(self.h_spacer_1)

        self.game_area_container = QFrame(ScrabbleView)
        self.game_area_container.setObjectName(u"game_area_container")
        self.game_area_container.setFrameShape(QFrame.NoFrame)
        self.game_area_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.game_area_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.v_spacer_1 = QSpacerItem(20, 106, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.v_spacer_1)

        self.board_container = QFrame(self.game_area_container)
        self.board_container.setObjectName(u"board_container")
        self.board_container.setFrameShape(QFrame.Box)
        self.board_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.board_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.grid_layout = QGridLayout()
        self.grid_layout.setObjectName(u"grid_layout")

        self.verticalLayout_2.addLayout(self.grid_layout)


        self.verticalLayout.addWidget(self.board_container)

        self.v_spacer_2 = QSpacerItem(20, 106, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.v_spacer_2)

        self.tile_container = QFrame(self.game_area_container)
        self.tile_container.setObjectName(u"tile_container")
        self.tile_container.setFrameShape(QFrame.StyledPanel)
        self.tile_container.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.tile_container)

        self.button_container = QFrame(self.game_area_container)
        self.button_container.setObjectName(u"button_container")
        self.button_container.setFrameShape(QFrame.StyledPanel)
        self.button_container.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.button_container)


        self.horizontal_layout.addWidget(self.game_area_container)

        self.h_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout.addItem(self.h_spacer_2)

        self.info_panel_outer = QFrame(ScrabbleView)
        self.info_panel_outer.setObjectName(u"info_panel_outer")
        self.info_panel_outer.setMinimumSize(QSize(300, 0))
        self.info_panel_outer.setStyleSheet(u"")
        self.info_panel_outer.setFrameShape(QFrame.Box)
        self.info_panel_outer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.info_panel_outer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.info_panel_inner = QFrame(self.info_panel_outer)
        self.info_panel_inner.setObjectName(u"info_panel_inner")
        self.info_panel_inner.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.info_panel_inner.setFrameShape(QFrame.StyledPanel)
        self.info_panel_inner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.info_panel_inner)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.info_panel_layout = QVBoxLayout()
        self.info_panel_layout.setObjectName(u"info_panel_layout")

        self.verticalLayout_4.addLayout(self.info_panel_layout)


        self.verticalLayout_3.addWidget(self.info_panel_inner)


        self.horizontal_layout.addWidget(self.info_panel_outer)


        self.retranslateUi(ScrabbleView)

        QMetaObject.connectSlotsByName(ScrabbleView)
    # setupUi

    def retranslateUi(self, ScrabbleView):
        ScrabbleView.setWindowTitle(QCoreApplication.translate("ScrabbleView", u"Form", None))
    # retranslateUi

