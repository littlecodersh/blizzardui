import os
from blizzardui.pyqt.QtGui import (QWidget,
    QDesktopWidget, QLabel,
    QVBoxLayout, QHBoxLayout,
    QPainter, QPixmap, QColor, QIcon)
from blizzardui.pyqt.QtCore import Qt, QEvent

from .views import Header, Messages, InputField, Footer

class Chatroom(QWidget):
    minSize = (300, 300) # width, height
    def __init__(self, toNickName='To', fromNickName='From',
            headImage=None, background=None):
        super(QWidget, self).__init__()
        self._init_window(toNickName, fromNickName, background)
        self._init_components(toNickName, fromNickName, headImage)
    def _init_window(self, toNickName, fromNickName, background):
        ''' set basic settings of window '''
        # set title & icon
        self.setWindowTitle(toNickName)
        self.setWindowIcon(QIcon('src/chatroom/images/icon/icon-online.png'))
        # set size and margins
        self.resize(320, 400)
        self.setContentsMargins(2, 2, 2, 2)
        # locate in center
        size = self.geometry()
        screen = QDesktopWidget().screenGeometry()
        self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)
        # frameless and enable resize
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        # draw background
        def paintEvent(event):
            p = QPainter(self)
            # draw background
            p.setBrush(QColor(40, 50, 67))
            p.drawRect(0, 0, self.width(), self.height())
            # draw two borders
            p.setPen(QColor(0, 0, 0))
            p.drawRect(0, 0, self.width()-1, self.height()-1)
            p.setPen(QColor(70, 79, 94))
            p.drawRect(1, 1, self.width()-3, self.height()-3)
            # draw header
            p.setPen(QColor(68, 72, 84))
            for i in range(8):
                if i == 7: p.setPen(QColor(73, 81, 97))
                p.drawLine(100+i, 2+i, self.width()-100-i, 2+i)
            for i in range(7):
                p.drawPoint(99+i, 2+i)
                p.drawPoint(self.width()-99-i, 2+i)
            event.accept()
        self.paintEvent = paintEvent
    def _init_components(self, toNickName, fromNickName, headImage):
        ''' load components of widget '''
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        header = Header(self, toNickName, 'live', headImage)
        self.set_status = header.set_status
        self.messages = Messages(self, toNickName, fromNickName)
        self.add_msg = self.messages.add_msg
        self.inputField = InputField(self, self.messages)
        self.footer = Footer(self)
        self.set_head_image = header.set_head_image
        self.set_footer = self.footer.setText
        layout.addWidget(header)
        layout.addWidget(self.messages, 1)
        layout.addWidget(self.inputField)
        layout.addWidget(self.footer)
        self.setLayout(layout)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startFrameGeometry = self.frameGeometry()
            self.startPosition =  event.globalPos()
            self.startResizeMask = self._determine_position(event)
        event.accept()
    def mouseMoveEvent(self, event):
        ''' track mouse whether it's pressed or not
         * close track by deleting this in _init_window: self.setMouseTracking(True)
         * determine is pressed mode is on first
        '''
        if event.buttons() == Qt.LeftButton:
            if getattr(self, 'startResizeMask', None) is None:
                pass
            elif 0 < self.startResizeMask:
                self._drag_resize(event)
            else:
                self.move(self.startFrameGeometry.topLeft()
                    - self.startPosition + event.globalPos())
        else:
            m = self._determine_position(event)
            if 0 < m:
                if event.buttons() == Qt.LeftButton:
                    self._drag_resize(event, m)
                else:
                    if not 0b0011 ^ m or not 0b1100 ^ m: # topleft or bottomright
                        self.setCursor(Qt.SizeFDiagCursor)
                    elif not 0b1001 ^ m or not 0b0110 ^ m: # topright or bottomleft
                        self.setCursor(Qt.SizeBDiagCursor)
                    elif 0b1010 & m:
                        self.setCursor(Qt.SizeHorCursor)
                    elif 0b0101 & m:
                        self.setCursor(Qt.SizeVerCursor)
            else:
                self.setCursor(Qt.ArrowCursor)
        event.accept()
    def _determine_position(self, event):
        ''' 0b0000 bin mask for left, top, right, bottom '''
        p = event.globalPos() - self.frameGeometry().topLeft()
        m = 5
        r = int(('%i' * 4) % (p.x() < m, p.y() < m,
            self.width() - m < p.x(), self.height() - m < p.y()), 2)
        return r
    def _drag_resize(self, event):
        i, marginChange = 0b1000, []
        for _ in range(4):
            marginChange.append(i & self.startResizeMask)
            i = i >> 1
        f = self.startFrameGeometry
        marginValue = [f.left(), f.top(), f.right(), f.bottom()]
        move = event.globalPos() - self.startPosition
        for i, additionalValue in enumerate((move.x(), move.y(), move.x(), move.y())):
            if marginChange[i]: marginValue[i] += additionalValue
        w, h = marginValue[2] - marginValue[0], marginValue[3] - marginValue[1]
        if w < self.minSize[0]:
            w = self.minSize[0]
            if marginChange[0]: marginValue[0] = marginValue[2] - w
        if h < self.minSize[1]:
            h = self.minSize[1]
            if marginChange[1]: marginValue[1] = marginValue[3] - h
        self.setGeometry(*(marginValue[:2] + [w, h]))
        if self.messages.height() < self.messages.minHeight:
            self.inputField.setFixedHeight(self.inputField.height()
                + self.messages.height() - self.messages.minHeight)
    def set_status(self, status, statusType='online'):
        ''' will be registered in _init_components '''
        raise NotImplementedError()
    def set_head_image(self, image):
        ''' will be registered in _init_components '''
        raise NotImplementedError()
    def add_msg(self, msg, isSend=True, timeStamp=None):
        ''' will be registered in _init_components '''
        raise NotImplementedError()
    def set_footer(self, msg):
        ''' will be registered in _init_components '''
        raise NotImplementedError()
