from PySide2.QtWidgets import (QAction, QVBoxLayout, QWidget, QMainWindow, QSplitter)
from ui.ConnectionsTreeView import ConnectionsTreeView
from ui.WorkspaceTabWidget import WorkspaceTabWidget
from ui.ConnectDialog import ConnectDialog


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.init_toolbar()
        self.central = QWidget()
        layout = QVBoxLayout()
        connections_tree = ConnectionsTreeView()
        workspace_tab = WorkspaceTabWidget()

        splitter = QSplitter()
        splitter.addWidget(connections_tree)
        splitter.addWidget(workspace_tab)
        layout.addWidget(splitter)

        self.central.setLayout(layout);
        self.setCentralWidget(self.central);

        # Add button signal to greetings slot
        # self.button.clicked.connect(self.greetings)

    def init_toolbar(self):
        toolbar = self.addToolBar("Main")

        connect_action = QAction("New Connection", self)
        connect_action.setShortcut("Ctrl+N")
        connect_action.triggered.connect(self.open_new_connection_dialog)

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        toolbar.addAction(connect_action)
        toolbar.addAction(exit_action)

    def open_new_connection_dialog(self):
        dialog = ConnectDialog()
        dialog.exec_()
