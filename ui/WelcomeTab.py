from PySide2.QtWidgets import (QWidget, QVBoxLayout)
from PySide2.QtGui import (QColor)
# from PySide2.QtCore import (QUrl)
from PySide2.QtWebEngineWidgets import (QWebEngineView)


class WelcomeTab(QWidget):

    def __init__(self, parent=None):
        super(WelcomeTab, self).__init__(parent)
        layout = QVBoxLayout()

        view = QWebEngineView()
        view.setHtml(open("html/welcome.html", "r").read())
        view.page().setBackgroundColor(QColor("transparent"))
        layout.addWidget(view)

        self.setLayout(layout)
