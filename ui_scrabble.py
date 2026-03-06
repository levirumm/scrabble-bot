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
        ScrabbleView.resize(438, 353)
        self.horizontalLayout = QHBoxLayout(ScrabbleView)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.side_bar_container = QFrame(ScrabbleView)
        self.side_bar_container.setObjectName(u"side_bar_container")
        self.side_bar_container.setFrameShape(QFrame.Box)
        self.side_bar_container.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.side_bar_container)

        self.h_spacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.h_spacer_1)

        self.game_area_container = QFrame(ScrabbleView)
        self.game_area_container.setObjectName(u"game_area_container")
        self.game_area_container.setFrameShape(QFrame.NoFrame)
        self.game_area_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.game_area_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.v_spacer_1 = QSpacerItem(20, 110, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.v_spacer_1)

        self.board_container = QFrame(self.game_area_container)
        self.board_container.setObjectName(u"board_container")
        self.board_container.setStyleSheet(u"")
        self.board_container.setFrameShape(QFrame.Box)
        self.board_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.board_container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.grid_layout = QGridLayout()
        self.grid_layout.setObjectName(u"grid_layout")

        self.horizontalLayout_2.addLayout(self.grid_layout)


        self.verticalLayout.addWidget(self.board_container)

        self.v_spacer_2 = QSpacerItem(20, 110, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.v_spacer_2)

        self.letter_rack_container = QFrame(self.game_area_container)
        self.letter_rack_container.setObjectName(u"letter_rack_container")
        self.letter_rack_container.setFrameShape(QFrame.NoFrame)
        self.letter_rack_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.letter_rack_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 4, -1, 4)
        self.letter_rack_layout = QHBoxLayout()
        self.letter_rack_layout.setObjectName(u"letter_rack_layout")

        self.verticalLayout_2.addLayout(self.letter_rack_layout)


        self.verticalLayout.addWidget(self.letter_rack_container)

        self.button_panel_container = QFrame(self.game_area_container)
        self.button_panel_container.setObjectName(u"button_panel_container")
        self.button_panel_container.setFrameShape(QFrame.NoFrame)
        self.button_panel_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.button_panel_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 4, -1, 4)
        self.button_panel_layout = QHBoxLayout()
        self.button_panel_layout.setObjectName(u"button_panel_layout")

        self.verticalLayout_3.addLayout(self.button_panel_layout)


        self.verticalLayout.addWidget(self.button_panel_container)


        self.horizontalLayout.addWidget(self.game_area_container)

        self.h_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.h_spacer_2)

        self.information_bar_container = QFrame(ScrabbleView)
        self.information_bar_container.setObjectName(u"information_bar_container")
        self.information_bar_container.setFrameShape(QFrame.Box)
        self.information_bar_container.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.information_bar_container)


        self.retranslateUi(ScrabbleView)

        QMetaObject.connectSlotsByName(ScrabbleView)
    # setupUi

    def retranslateUi(self, ScrabbleView):
        ScrabbleView.setWindowTitle(QCoreApplication.translate("ScrabbleView", u"Form", None))
    # retranslateUi

