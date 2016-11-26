# blizzardui

![py27][py27] ![py35][py35] [English version][english-version]

blizzardui是一个通过pyqt模仿暴雪界面的项目，旨在给予学习pyqt的同行一些借鉴。

配色、样式、配图皆来源于暴雪，但具体的项目实现存在一些个人的取巧。

希望这个项目可以帮助你更快的完成界面的搭建或者入门pyqt。

由于QtWebKit的变化，目前pyqt5.6及以上的版本不能被支持。

目前该项目仅完成了聊天窗口的部分，其余部分将陆续更新。

## 简单入门实例

在将本项目下载到本地后，你可以这样运行：

```python
python demo.py
```

运行后，你将看到这样的界面：

![chatroom-demo][chatroom-demo]

## 方法说明

下面我们就演示程序对如何使用做一个简单的讲解：

```python
#coding=utf8
import sys

from blizzardui.pyqt.QtGui import (
    QApplication, QPixmap)

from blizzardui.widgets import Chatroom

# 常规的启动动作就不多加说明
app = QApplication(sys.argv)
# 两个NickName定义了来往的用户昵称
# headImage应当为一个 46*46 的QPixmap，当然如果过大也会被自动截取
mainWindow = Chatroom(toNickName=u'好友A', fromNickName='LittleCoder',
    headImage=QPixmap('src/chatroom/images/header/default_image.png'))
mainWindow.show()

# 当你输入一些内容并使用Enter时，将会调用该方法
def fn(msg):
    mainWindow.add_msg(msg)
    print(unicode(msg))
mainWindow.messageReceived.connect(fn)

# 通过add_msg，可以向历史记录中加入消息
# 如果isSend设为False，将会判定为是收到的消息
mainWindow.add_msg('yo' * 50)
mainWindow.add_msg('yo', isSend=False)
mainWindow.add_msg('yo')
# 通过set_footer，可以设置页尾的内容
mainWindow.set_footer(u'最后登录')

sys.exit(app.exec_())
```

## 常见问题与解答

Q: 为什么不使用QWebEngineView？

A: 我没能找到一个很好的办法让QWebEngineView快速启动，所以会出现初始化时闪烁以及无法加入消息的问题。

## 问题和建议

如果有什么问题或者建议都可以在这个[Issue][issue#1]和我讨论

[py27]: https://img.shields.io/badge/python-2.7-ff69b4.svg
[py35]: https://img.shields.io/badge/python-3.5-red.svg
[english-version]: https://github.com/littlecodersh/blizzardui/blob/master/README_EN.md
[chatroom-demo]: http://7xrip4.com1.z0.glb.clouddn.com/blizzardui/chatroom-demo.png
[issue#1]: https://github.com/littlecodersh/blizzardui/issues/1
