try:
    from PyQt4.QtCore import (
        QEvent, Qt, QRect, QPoint,
        QSize, QUrl, pyqtSignal)
except:
    try:
        from PyQt5.QtCore import (
            QEvent, Qt, QRect, QPoint,
            QSize, QUrl, pyqtSignal)
    except:
        raise ImportError('Please make sure pyqt is installed')
