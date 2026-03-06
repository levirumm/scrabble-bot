# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dictionary.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_dictionary(object):
    def setupUi(self, dictionary):
        if not dictionary.objectName():
            dictionary.setObjectName(u"dictionary")
        dictionary.resize(400, 313)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dictionary.sizePolicy().hasHeightForWidth())
        dictionary.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(dictionary)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(dictionary)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_container = QFrame(self.frame)
        self.title_container.setObjectName(u"title_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_container.sizePolicy().hasHeightForWidth())
        self.title_container.setSizePolicy(sizePolicy1)
        self.title_container.setFrameShape(QFrame.NoFrame)
        self.title_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.title_container)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 6, 0, 0)
        self.title = QLabel(self.title_container)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.title)


        self.verticalLayout_2.addWidget(self.title_container)

        self.line_container = QFrame(self.frame)
        self.line_container.setObjectName(u"line_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_container.sizePolicy().hasHeightForWidth())
        self.line_container.setSizePolicy(sizePolicy2)
        self.line_container.setMinimumSize(QSize(0, 0))
        self.line_container.setMaximumSize(QSize(16777215, 160))
        self.line_container.setFrameShape(QFrame.NoFrame)
        self.line_container.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.line_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, 0, 20, 0)
        self.line = QFrame(self.line_container)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 1))
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)

        self.horizontalLayout_5.addWidget(self.line)


        self.verticalLayout_2.addWidget(self.line_container)

        self.input_container = QFrame(self.frame)
        self.input_container.setObjectName(u"input_container")
        self.input_container.setFrameShape(QFrame.NoFrame)
        self.input_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.input_container)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 12, -1, -1)
        self.text_input = QLineEdit(self.input_container)
        self.text_input.setObjectName(u"text_input")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.text_input.sizePolicy().hasHeightForWidth())
        self.text_input.setSizePolicy(sizePolicy3)
        self.text_input.setMinimumSize(QSize(0, 30))
        self.text_input.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.text_input)

        self.search_button = QPushButton(self.input_container)
        self.search_button.setObjectName(u"search_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy4)
        self.search_button.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.search_button)


        self.verticalLayout_2.addWidget(self.input_container)

        self.output_container = QFrame(self.frame)
        self.output_container.setObjectName(u"output_container")
        sizePolicy.setHeightForWidth(self.output_container.sizePolicy().hasHeightForWidth())
        self.output_container.setSizePolicy(sizePolicy)
        self.output_container.setFrameShape(QFrame.NoFrame)
        self.output_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.output_container)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, -1, -1, 2)
        self.text_output = QTextEdit(self.output_container)
        self.text_output.setObjectName(u"text_output")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.text_output.sizePolicy().hasHeightForWidth())
        self.text_output.setSizePolicy(sizePolicy5)
        self.text_output.setMinimumSize(QSize(0, 150))
        self.text_output.setMaximumSize(QSize(16777215, 150))

        self.horizontalLayout_3.addWidget(self.text_output)


        self.verticalLayout_2.addWidget(self.output_container)

        self.button_container = QFrame(self.frame)
        self.button_container.setObjectName(u"button_container")
        self.button_container.setFrameShape(QFrame.NoFrame)
        self.button_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.button_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.close_button = QPushButton(self.button_container)
        self.close_button.setObjectName(u"close_button")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy6)
        self.close_button.setMinimumSize(QSize(110, 30))
        self.close_button.setMaximumSize(QSize(110, 30))

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout_2.addWidget(self.button_container)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(dictionary)

        QMetaObject.connectSlotsByName(dictionary)
    # setupUi

    def retranslateUi(self, dictionary):
        dictionary.setWindowTitle(QCoreApplication.translate("dictionary", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("dictionary", u"Scrabble Dictionary", None))
#if QT_CONFIG(tooltip)
        self.search_button.setToolTip(QCoreApplication.translate("dictionary", u"Look up word", None))
#endif // QT_CONFIG(tooltip)
        self.search_button.setText(QCoreApplication.translate("dictionary", u"Search", None))
        self.close_button.setText(QCoreApplication.translate("dictionary", u"Close", None))
    # retranslateUi

