#coding=utf8
import os

from blizzardui.pyqt.QtGui import (
    QWidget, QDesktopWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFont,
    QPainter, QColor, QPixmap)
from blizzardui.pyqt.QtCore import Qt

with open(os.path.join('src', 'chatroom',
        'styles', 'header', 'btn_fn.qss')) as f:
    FN_BTN_QSS = f.read()

STATUS_PIC_DICT = {
    'online'  : 'src/chatroom/images/header/status_online.png',
    'offline' : 'src/chatroom/images/header/status_offline.png',
}

class Header(QWidget):
    def __init__(self, parent, toNickName, status,
            headImage=None, statusImage=None):
        super(QWidget, self).__init__()
        self.mainWindow = parent
        self.setMouseTracking(True)
        self.setFixedHeight(82)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addSpacing(3)
        fbLayout = self._get_fn_btn_layout(parent)
        hpLayout = self._get_head_picture_layout(
            toNickName, status, headImage, statusImage)
        layout.addLayout(fbLayout)
        layout.addLayout(hpLayout)
        layout.addStretch()
        self.setLayout(layout)
    def _get_fn_btn_layout(self, parent):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 5, 0)
        layout.addStretch(0)
        btnList = [QPushButton() for i in range(3)]
        switchFn = self._switch_size(btnList[1])
        btnList = zip(['btn_hide', 'btn_big', 'btn_close'],
            [parent.showMinimized, switchFn.next, parent.close], btnList)
        for n, fn, btn in btnList:
            btn.setStyleSheet(FN_BTN_QSS % (n, n, n))
            btn.pressed.connect(fn)
            layout.addWidget(btn, 0, Qt.AlignTop)
        return layout
    def _switch_size(self, btn):
        while 1:
            btn.setStyleSheet(FN_BTN_QSS % (('btn_small',) * 3))
            currentGeo = self.mainWindow.geometry()
            yield self.mainWindow.setGeometry(QDesktopWidget().availableGeometry())
            btn.setStyleSheet(FN_BTN_QSS % (('btn_big',) * 3))
            yield self.mainWindow.setGeometry(currentGeo)
    def _get_head_picture_layout(self,
            toNickName, status, headImage, statusImage):
        layout = QHBoxLayout()
        layout.setContentsMargins(8, 0, 0, 0)
        layout.setSpacing(11)
        headImage = HeadImage()
        nameAndStatus = NameAndStatus(toNickName, status, statusImage)
        layout.addWidget(headImage)
        layout.addWidget(nameAndStatus)
        layout.addStretch()
        self.set_status = nameAndStatus.set_status
        return layout
    def set_status(self, status, statusType='online'):
        ''' will be defined in _get_head_picture_layout '''
        raise NotImplementedError()
    def paintEvent(self, event):
        p = QPainter(self)
        # draw bottom border
        p.setPen(QColor(53, 63, 80))
        p.drawRect(0, self.height()-1, self.width()-1, self.height()-1)

class HeadImage(QWidget):
    image = None
    def __init__(self):
        super(QWidget, self).__init__()
        self.setFixedSize(50, 50)
    def paintEvent(self, event):
        p = QPainter(self)
        # draw image
        if isinstance(self.image, QPixmap):
            p.drawPixmap(2, 2, self.image)
        else:
            p.drawPixmap(2, 2,
                QPixmap('src/chatroom/images/header/default_image.png'))
        # draw two borders
        p.setPen(QColor(24, 30, 40))
        p.drawRect(0, 0, self.width()-1, self.height()-1)
        p.setPen(QColor(58, 58, 58))
        p.drawRect(1, 1, self.width()-3, self.height()-3)

class NameAndStatus(QLabel):
    nameString   = ''
    statusString = ''
    name = ''
    status = ''
    statusType = ''
    def __init__(self, name, status, statusType='online'):
        super(QLabel, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.baseNameString = '<div style="font:17px;color:rgb(121,182,236);' \
            'margin-bottom:4;font-family:Microsoft YaHei">%s </div><img src="%s">'
        self.baseStatusString = '<div style="font:12px;color:rgb(143,148,157);'\
            'font-family:Microsoft YaHei"><img src="%s"> %s</div>'
        self.name, self.status = name, status
        self.set_status(status, statusType)
    def set_status(self, status, statusType='online'):
        self.status = status
        self.statusType = statusType
        nameString = self.baseNameString % (self.name, 
            'src/chatroom/images/header/down.png')
        statusString = self.baseStatusString % (
            STATUS_PIC_DICT.get(statusType, STATUS_PIC_DICT['online']), self.status)
        self.setText(nameString + statusString)
    def enterEvent(self, event):
        hoverNameString = '<div style="font:17px;color:rgb(130,197,197);' \
            'margin-bottom:4;font-family:Microsoft YaHei">%s </div><img src="%s">'
        hoverStatusString = '<div style="font:12px;color:rgb(176,180,186);'\
            'font-family:Microsoft YaHei"><img src="%s"> %s</div>'
        nameString = hoverNameString % (self.name, 
            'src/chatroom/images/header/down_hover.png')
        statusString = hoverStatusString % (
            STATUS_PIC_DICT.get(self.statusType, STATUS_PIC_DICT['online']), self.status)
        self.setText(nameString + statusString)
    def leaveEvent(self, event):
        nameString = self.baseNameString % (self.name, 
            'src/chatroom/images/header/down.png')
        statusString = self.baseStatusString % (
            STATUS_PIC_DICT.get(self.statusType, STATUS_PIC_DICT['online']), self.status)
        self.setText(nameString + statusString)
