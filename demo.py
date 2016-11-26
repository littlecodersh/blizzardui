#coding=utf8
import sys

from blizzardui.pyqt.QtGui import (
    QApplication, QPixmap)

from blizzardui.widgets import Chatroom

app = QApplication(sys.argv)
mainWindow = Chatroom(toNickName=u'好友A', fromNickName='LittleCoder',
    headImage=QPixmap('src/chatroom/images/header/default_image.png'))
mainWindow.show()

def fn(msg):
    mainWindow.add_msg(msg)
    print(unicode(msg))
mainWindow.messageReceived.connect(fn)

mainWindow.add_msg(u'yo'*50)
mainWindow.add_msg('yo', isSend=False)
mainWindow.add_msg('yo')
mainWindow.set_footer(u'最后登录')

sys.exit(app.exec_())
