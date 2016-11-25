try:
    from PyQt4.QtGui import (
        QApplication, QWidget, QFrame,
        QListWidget, QListWidgetItem,
        QVBoxLayout, QGridLayout, QHBoxLayout,
        QGroupBox, QLabel, QPushButton, QTextEdit,
        QTextDocument, QTextBlockFormat, QTextCursor,
        QTextFrame, QTextFrameFormat,
        QFontMetrics, QTextOption,
        QDesktopWidget, QPainterPath, QPainter, QBrush,
        QPixmap, QPalette, QColor, QFont,
        QIcon, QSystemTrayIcon, QMenu, QAction)
except:
    try:
        from PyQt5.QtWidgets import (
            QApplication, QWidget, QFrame,
            QListWidget, QListWidgetItem,
            QVBoxLayout, QGridLayout, QHBoxLayout,
            QGroupBox, QLabel, QPushButton, QTextEdit,
            QSystemTrayIcon, QMenu, QAction, QDesktopWidget)
        from PyQt5.QtGui import ( 
            QTextDocument, QTextBlockFormat, QTextCursor,
            QTextFrame, QTextFrameFormat,
            QFontMetrics, QTextOption,
            QPainterPath, QPainter, QBrush,
            QPixmap, QPalette, QColor, QFont, QIcon) 
    except:
        raise ImportError('Please make sure pyqt is installed')
