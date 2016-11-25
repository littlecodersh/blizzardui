
try:
    from PyQt4.QtWebKit import QWebView
except:
    try:
        from PyQt5.QtWebKit import QWebView
    except:
        raise ImportError('Please make sure pyqt under 5.6 is installed')
