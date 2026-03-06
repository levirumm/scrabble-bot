# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tile_swap.ui'
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

class Ui_tile_swap(object):
    def setupUi(self, tile_swap):
        if not tile_swap.objectName():
            tile_swap.setObjectName(u"tile_swap")
        tile_swap.resize(400, 300)
        self.verticalLayout = QVBoxLayout(tile_swap)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(tile_swap)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.swap_icon_container = QFrame(self.frame)
        self.swap_icon_container.setObjectName(u"swap_icon_container")
        self.swap_icon_container.setFrameShape(QFrame.NoFrame)
        self.swap_icon_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.swap_icon_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.swap_icon = QLabel(self.swap_icon_container)
        self.swap_icon.setObjectName(u"swap_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swap_icon.sizePolicy().hasHeightForWidth())
        self.swap_icon.setSizePolicy(sizePolicy)
        self.swap_icon.setMinimumSize(QSize(40, 40))
        self.swap_icon.setMaximumSize(QSize(40, 40))
        self.swap_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.swap_icon)


        self.verticalLayout_2.addWidget(self.swap_icon_container)

        self.label_container = QFrame(self.frame)
        self.label_container.setObjectName(u"label_container")
        self.label_container.setFrameShape(QFrame.NoFrame)
        self.label_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.label_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title = QLabel(self.label_container)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.title)

        self.selection_count = QLabel(self.label_container)
        self.selection_count.setObjectName(u"selection_count")
        self.selection_count.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.selection_count)


        self.verticalLayout_2.addWidget(self.label_container)

        self.tile_container = QFrame(self.frame)
        self.tile_container.setObjectName(u"tile_container")
        self.tile_container.setFrameShape(QFrame.NoFrame)
        self.tile_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.tile_container)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tile_layout = QHBoxLayout()
        self.tile_layout.setSpacing(8)
        self.tile_layout.setObjectName(u"tile_layout")

        self.horizontalLayout_3.addLayout(self.tile_layout)


        self.verticalLayout_2.addWidget(self.tile_container)

        self.button_container = QFrame(self.frame)
        self.button_container.setObjectName(u"button_container")
        self.button_container.setFrameShape(QFrame.NoFrame)
        self.button_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.button_container)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.swap_button = QPushButton(self.button_container)
        self.swap_button.setObjectName(u"swap_button")
        self.swap_button.setMinimumSize(QSize(0, 33))
        self.swap_button.setMaximumSize(QSize(16777215, 33))
        self.swap_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.swap_button)

        self.cancel_button = QPushButton(self.button_container)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 33))
        self.cancel_button.setMaximumSize(QSize(16777215, 33))
        self.cancel_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.cancel_button)


        self.verticalLayout_2.addWidget(self.button_container)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(tile_swap)

        QMetaObject.connectSlotsByName(tile_swap)
    # setupUi

    def retranslateUi(self, tile_swap):
        tile_swap.setWindowTitle(QCoreApplication.translate("tile_swap", u"Dialog", None))
        self.swap_icon.setText("")
        self.title.setText(QCoreApplication.translate("tile_swap", u"Select Tiles to Swap", None))
        self.selection_count.setText("")
        self.swap_button.setText(QCoreApplication.translate("tile_swap", u"Swap && Skip", None))
        self.cancel_button.setText(QCoreApplication.translate("tile_swap", u"Cancel", None))
    # retranslateUi

