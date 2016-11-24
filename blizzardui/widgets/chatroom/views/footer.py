from blizzardui.pyqt.QtGui import (
    QWidget, QLabel, QHBoxLayout)

class Footer(QWidget):
    def __init__(self, mainWindow):
        super(QWidget, self).__init__()
        self.setMouseTracking(True)
        self.setFixedHeight(30)
        layout = QHBoxLayout()
        layout.setContentsMargins(8, 0, 0, 0)
        self.textLabel = QLabel()
        self.textLabel.setMouseTracking(True)
        self.textLabel.mouseMoveEvent = mainWindow.mouseMoveEvent
        self.textLabel.mousePressEvent = mainWindow.mousePressEvent
        self.textLabel.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.textLabel)
        layout.addStretch()
        self.setLayout(layout)
    def setText(self, msg):
        template = '<div style="color:rgb(147,152,161);font:13px;' \
            'font-family:Microsoft YaHei;">%s</div>'
        self.textLabel.setText(template % msg)
