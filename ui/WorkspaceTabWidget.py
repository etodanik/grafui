from PySide2.QtWidgets import (QTabWidget)
from ui.WelcomeTab import WelcomeTab


class WorkspaceTabWidget(QTabWidget):

    def __init__(self, parent=None):
        super(WorkspaceTabWidget, self).__init__(parent)
        self.addTab(WelcomeTab(), "Welcome")
        self.setDocumentMode(True)
        # self.setTabsClosable(True)