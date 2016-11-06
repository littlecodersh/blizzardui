import time, os

from blizzardui.pyqt.QtGui import (
    QWidget, QFrame,
    QVBoxLayout, QHBoxLayout,
    QTextEdit, QTextBlockFormat, QTextCursor,
    QTextFrame, QTextFrameFormat,
    QPalette, QColor)
from blizzardui.pyqt.QtCore import Qt, QSize

with open(os.path.join('src', 'chatroom',
        'styles', 'messages', 'ted_msg.qss')) as f:
    MESSAGES_QSS = f.read()

class Messages(QTextEdit):
    def __init__(self, parent, toNickName, fromNickName):
        super(QTextEdit, self).__init__()
        self.formalContent, self.lastMsg = '', {}
        # lastMsg: {'isSend': True, 'timeStamp': 0, }
        self.mainWindow = parent
        self.toNickName, self.fromNickName = toNickName, fromNickName
        self._init_settings()
        self._init_templates()
    def _init_settings(self):
        self.setMouseTracking(False)
        self.setFrameStyle(QFrame.NoFrame)
        self.setStyleSheet(MESSAGES_QSS)
        self.document().setDocumentMargin(0)
        self.setReadOnly(True)
    def _init_templates(self):
        self.headTemplate = u'<textarea style="margin-left:10px;font:13;' \
            'color:rgb(117,197,242);font-family:Microsoft YaHei;">' \
            '{name}</textarea><textarea style="font:10px;' \
            'color:rgb(85,87,93);font-family:Microsoft YaHei;" align="right">' \
            '{time}</textarea>'
        self.contentTemplate = u'<img src="src/chatroom/images/messages/start_symbol.png">' \
            '<textarea style="font:13px;color:rgb(223,223,223);font-family:Microsoft YaHei">' \
            '{content}</textarea>'
    def add_msg(self, msg, isSend=True, timeStamp=None):
        cursor = self.textCursor()
        frameCursor = cursor#.currentFrame().lastCursorPosition()
        if self.lastMsg.get('isSend') != isSend: # new msg
            frameFormat = QTextFrameFormat()
            frameFormat.setBackground(QColor(27, 39, 55)
                if isSend else QColor(29, 34, 44))
            cursor.movePosition(QTextCursor.End)
            cursor.insertFrame(frameFormat)
            blockFormat = QTextBlockFormat()
            blockFormat.setLeftMargin(10)
            frameCursor = cursor.currentFrame().firstCursorPosition()
            frameCursor.insertBlock(blockFormat)
            frameCursor.insertHtml(self.headTemplate.format(
                name=self.fromNickName if isSend else self.toNickName,
                time=time.strftime('%H:%M', time.localtime(timeStamp))))
            f = cursor.currentFrame()
            self.lastMsg['isSend'] = isSend
        frameCursor.insertBlock()
        frameCursor.insertHtml(self.contentTemplate.format(content=msg))
