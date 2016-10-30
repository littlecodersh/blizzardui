from blizzardui.pyqt.QtGui import QWidget, QDesktopWidget
from blizzardui.pyqt.QtCore import Qt

class Chatroom(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self._init_window()
        self._init_components()
    def _init_window(self):
        ''' set basic settings of window '''
        # set size and margins
        self.setFixedSize(500, 600)
        self.setContentsMargins(0, 0, 0, 0)
        # locate in center
        size = self.geometry()
        screen = QDesktopWidget().screenGeometry()
        self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)
        self.setWindowFlags(Qt.FramelessWindowHint)
    def _init_components(self):
        ''' load components of widget '''
        pass
