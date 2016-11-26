# blizzardui

![py27][py27] ![py35][py35] [English version][english-version]

blizzardui is a project simulating blizzard ui using pyqt, aimed at giving learners of pyqt something to read.

Colors, styles, pictures are all from blizzard, but there are some personal tricks when making this project.

I hope this program can help you build your ui or learn to know pyqt.

Since the abandon of QtWebKit, pyqt above 5.6 is not supported.

For now, only chatroom is finished, other parts will be coming soon.

## Demo

After downloading this project, you may run it like this:

```python
python demo.py
```

Then this is what you will see:

![chatroom-demo][chatroom-demo]

## Methods

Let me show you around the methods with the simple demo:

```python
import sys

from blizzardui.pyqt.QtGui import (
    QApplication, QPixmap)

from blizzardui.widgets import Chatroom

# regular action
app = QApplication(sys.argv)
# headImage should be a QPixmap of 46*46, of course, it can be bigger
mainWindow = Chatroom(toNickName='Friend A', fromNickName='LittleCoder',
    headImage=QPixmap('src/chatroom/images/header/default_image.png'))
mainWindow.show()

# fn will be called when you use enter in message field
def fn(msg):
    mainWindow.add_msg(msg)
    print(unicode(msg))
mainWindow.messageReceived.connect(fn)

# through add_msg, you may add messages into history
# if isSend is False, message will be viewed as received message
mainWindow.add_msg('yo' * 50)
mainWindow.add_msg('yo', isSend=False)
mainWindow.add_msg('yo')
# through set_footer, you may set the footer
mainWindow.set_footer('Last log in time: ???')

sys.exit(app.exec_())
```

## Q&A

Q: Why not QWebEngineView?

A: Since I failed to find a way to quick launch QWebEngineView, it will flash when loading.

## Suggestions

If you have any questions or suggestions, feel free to discuss with me [here][issue#1].

[py27]: https://img.shields.io/badge/python-2.7-ff69b4.svg
[py35]: https://img.shields.io/badge/python-3.5-red.svg
[english-version]: https://github.com/littlecodersh/blizzardui/blob/master/README_EN.md
[chatroom-demo]: http://7xrip4.com1.z0.glb.clouddn.com/blizzardui/chatroom-demo.png
[issue#1]: https://github.com/littlecodersh/blizzardui/issues/1
