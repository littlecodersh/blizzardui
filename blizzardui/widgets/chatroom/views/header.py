import os

from blizzardui.pyqt.QtGui import (
    QWidget, QDesktopWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel)
from blizzardui.pyqt.QtCore import Qt

with open(os.path.join('src', 'chatroom',
        'styles', 'header', 'btn_fn.qss')) as f:
    FN_BTN_QSS = f.read()

class Header(QWidget):
    def __init__(self, parent, toNickName, status):
        super(QWidget, self).__init__()
        self.mainWindow = parent
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        fbLayout = self._get_fn_btn_layout(parent)
        hpLayout = self._get_head_picture_layout()
        layout.addLayout(fbLayout)
        layout.addLayout(hpLayout)
        self.setLayout(layout)
    def _get_fn_btn_layout(self, parent):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 4, 7, 0)
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
    def _get_head_picture_layout(self):
        layout = QHBoxLayout()
        lb = QLabel()
        lb.setText('<p style="font:16px;color:#FFF">\
			&nbsp;&nbsp;%s</p>'%('ahahahaheiheihei'))
        layout.addWidget(lb, 0, Qt.AlignVCenter)
        return layout
    def set_status(status):
        pass
