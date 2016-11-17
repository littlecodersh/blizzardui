from blizzardui.pyqt.QtGui import (
    QWidget, QLabel, QVBoxLayout)

class Footer(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setMouseTracking(True)
        self.setFixedHeight(30)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.textLabel = QLabel()
        self.textLabel.setContentsMargins(8, 0, 0, 0)
        layout.addWidget(self.textLabel)
        self.setLayout(layout)
    def setText(self, msg):
        template = '<div style="color:rgb(147,152,161);font:13px;' \
            'font-family:Microsoft YaHei;">%s</div>'
        self.textLabel.setText(template % msg)
