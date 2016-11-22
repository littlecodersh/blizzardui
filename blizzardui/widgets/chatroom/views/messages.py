import time, os

from blizzardui.pyqt.QtGui import (
    QWidget, QFrame,
    QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem,
    QPalette, QColor)
from blizzardui.pyqt.QtCore import (
    Qt, QSize, QUrl)
from blizzardui.pyqt.QtWebKit import QWebView

with open(os.path.join('src', 'chatroom',
        'styles', 'messages', 'messages.html')) as f:
    MESSAGE_HTML = f.read()

class Messages(QWebView):
    minHeight = 100
    def __init__(self, parent, toNickName, fromNickName):
        super(QWebView, self).__init__()
        self.formalContent, self.lastMsg = '', {}
        # lastMsg: {'isSend': True, 'timeStamp': 0, }
        self.mainWindow = parent
        self.toNickName, self.fromNickName = toNickName, fromNickName
        self._init_settings()
    def _init_settings(self):
        self.setMouseTracking(False)
        self.setHtml(MESSAGE_HTML)
    def add_msg(self, msg, isSend=True, timeStamp=None):
        args = ['"%s"' % msg, str(isSend).lower()]
        if self.lastMsg.get('isSend') != isSend: # old msg
            additionalArgs = [
                self.fromNickName if isSend else self.toNickName,
                time.strftime('%H:%M', time.localtime(timeStamp))]
            additionalArgs = ['"%s"' % arg for arg in additionalArgs]
            args += additionalArgs
            self.lastMsg['isSend'] = isSend
        cmd = 'addMessage(%s);' % (','.join(args))
        mf = self.page().mainFrame()
        mf.evaluateJavaScript(cmd)
        mf.evaluateJavaScript('window.scrollTo(0,document.body.scrollHeight);')
