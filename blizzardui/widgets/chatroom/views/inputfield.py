import os

from blizzardui.pyqt.QtGui import (
    QWidget, QTextEdit,
    QVBoxLayout,
    QPainter, QColor)
from blizzardui.pyqt.QtCore import Qt, pyqtSignal

with open(os.path.join('src', 'chatroom',
        'styles', 'inputfield', 'ted_input.qss')) as f:
    TED_INPUT_QSS = f.read()

RESIZE_MARGIN = 8

class InputField(QWidget):
    def __init__(self, parent, receivedSignal, messagesWidget):
        super(QWidget, self).__init__(parent)
        self.mainWindow = parent
        self.messagesWidget = messagesWidget
        self._init_settings()
        self._init_widgets(receivedSignal)
    def _init_settings(self):
        self.setMouseTracking(True)
        self.setContentsMargins(0, 1, 0, 0)
        self.setFixedHeight(70)
    def _init_widgets(self, receivedSignal):
        layout = QVBoxLayout()
        # bottom margin is left to footer
        layout.setContentsMargins(7, 7, 7, 0)
        ipf = self
        class Ted(QTextEdit):
            def keyPressEvent(self, event):
                if event.key() == Qt.Key_Return:
                    receivedSignal.emit(unicode(self.toPlainText()))
                    self.clear()
                else:
                    QTextEdit.keyPressEvent(self, event)
        ted = Ted()
        ted.setStyleSheet(TED_INPUT_QSS)
        layout.addWidget(ted)
        self.setLayout(layout)
    def paintEvent(self, event):
        p = QPainter(self)
        # draw top border
        p.setPen(QColor(53, 63, 80))
        p.drawRect(0, 0, self.width()-1, 0)
        # draw resize double-line
        p.setPen(QColor(20, 25, 34))
        middle = self.width() / 2
        for y in (3, 5):
            p.drawLine(middle - 15, y, middle + 15, y)
        event.accept()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            p = event.globalPos() - self.frameGeometry().topLeft() \
                - self.mainWindow.frameGeometry().topLeft()
            m = RESIZE_MARGIN
            self.resizeFlag = p.y() < m
            if self.resizeFlag:
                self.startPosition = event.globalPos()
                self.startHeight = self.height()
                self.startMessagesHeight = self.messagesWidget.height()
            else:
                self.mainWindow.mousePressEvent(event)
        event.accept()
    def mouseMoveEvent(self, event):
        p = event.globalPos() - self.frameGeometry().topLeft() \
            - self.mainWindow.frameGeometry().topLeft()
        m = RESIZE_MARGIN
        if event.buttons() == Qt.LeftButton:
            if self.resizeFlag:
                changeHeight = (self.startPosition - event.globalPos()).y()
                endHeight = self.startHeight + changeHeight
                messagesHeight = self.startMessagesHeight - changeHeight
                if self.messagesWidget.minHeight < messagesHeight and 75 < endHeight:
                    self.setFixedHeight(endHeight)
            else:
                self.mainWindow.mouseMoveEvent(event)
        else:
            if p.y() < m:
                self.setCursor(Qt.SizeVerCursor)
            else:
                self.setCursor(Qt.ArrowCursor)
        event.accept()
