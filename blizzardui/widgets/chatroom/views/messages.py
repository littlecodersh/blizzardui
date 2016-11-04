import time

from blizzardui.pyqt.QtGui import (QWidget,
    QListWidget, QListWidgetItem,
    QVBoxLayout, QHBoxLayout,
    QLabel,
    QPalette, QColor)
from blizzardui.pyqt.QtCore import Qt, QSize

qss = '''\
QListWidget{  
    background: rgb(29, 34, 44);  
    color:black;  
    border:none;  
}  

QScrollBar:vertical {                 
    background:transparent;  
    width:9px;  
    margin: 0px 0px 2px 0px;  
}  
  
QScrollBar::handle:vertical {  
    background: rgb(195, 195, 195);  
    min-height: 20px;  
    border-radius: 3px;  
}  
  
QScrollBar::handle:vertical:hover{  
    background:rgba(0,0,0,30%);  
}  
'''

class Messages(QListWidget):
    lastItem = None
    def __init__(self, parent, toNickName, fromNickName):
        super(QListWidget, self).__init__()
        self.mainWindow = parent
        self.setMouseTracking(True)
        self.setSelectionMode(QListWidget.NoSelection)
        self.setFocusPolicy(Qt.NoFocus)
        self.setStyleSheet(qss)
        self.toNickName, self.fromNickName = toNickName, fromNickName
    def mouseMoveEvent(self, event):
        self.mainWindow.mouseMoveEvent(event)
    def add_msg(self, msg, isSend=True, timeStamp=None):
        if self.lastItem is None or self.lastItem[0].isSend != isSend:
            nickName = self.fromNickName if isSend else self.toNickName
            item = MessagesItem(nickName, isSend, timeStamp)
            fakeItem = QListWidgetItem()
            fakeItem.setBackgroundColor(item.backgroundColor)
            self.addItem(fakeItem)
            self.setItemWidget(fakeItem, item)
            self.lastItem = (item, fakeItem)
        else:
            item, fakeItem = self.lastItem
        item.add_msg(msg)
        fakeItem.setSizeHint(item.sizeHint())

class MessagesItem(QLabel):
    isSend          = True
    backgroundColor = None
    completeMsg     = None
    def __init__(self, nickName, isSend=True, timeStamp=None):
        super(QLabel, self).__init__()
        self.isSend = isSend
        self.backgroundColor = QColor(27, 39, 55) if isSend \
            else QColor(29, 34, 44)
        self.setStyleSheet('QLabel{selection-color: rgb(223,223,223);' +
            'selection-background-color: rgb(66, 76, 88)}')
        self.setContentsMargins(0, 0, 0, 0)
        self.setTextInteractionFlags(Qt.TextSelectableByMouse)
        headMsg = self._get_head_msg(nickName, timeStamp)
        self.completeMsg = headMsg
        self.setText(self.completeMsg)
    def _get_head_msg(self, nickName, timeStamp=None):
        templateMsg = '<div><div style="font:13px;' \
            'color:rgb(117,197,242);font-family:Microsoft YaHei;">' \
            '{name}</div><div style="font:10px;' \
            'color:rgb(85,87,93);font-family:Microsoft YaHei;" align="right">' \
            '{time}</div></div>'
        if timeStamp is None: timeStamp = time.time()
        return templateMsg.format(**{
            'name': nickName,
            'time': time.strftime('%H:%M', time.localtime(timeStamp)), })
    def _get_content_msg(self, content):
        templateMsg = '<div><img src="src/chatroom/images/header/down.png" align="left">' \
            '<div style="font:13px;color:rgb(223,223,223);font-family:Microsoft YaHei">{content}'\
            '</div></div>'
        return templateMsg.format(content=content)
    def add_msg(self, msg):
        newContent = self._get_content_msg(msg)
        self.completeMsg += newContent
        self.setText(self.completeMsg)
