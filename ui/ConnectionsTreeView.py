from PySide2.QtGui import (QStandardItem)
from PySide2.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTreeView, QAction, QToolButton, QToolBar)
from data.Connections import (Connections, ConnectionsModel)


class ConnectionsTreeView(QWidget):

    def __init__(self, parent=None):
        super(ConnectionsTreeView, self).__init__(parent)
        self.tree: QTreeView = self.tree()
        self.actions: QToolBar = self.actions()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tree)
        self.layout.addWidget(self.actions)
        self.setLayout(self.layout)

    def tree(self) -> QTreeView:
        tree = QTreeView()
        tree.header().hide()
        self.connections = Connections()
        tree.setModel(self.connections.get_model())
        tree.expandAll()
        return tree

    def actions(self) -> QToolBar:
        toolbar = QToolBar()

        remove_action = QAction("Remove", self)
        remove_action.setShortcut("Ctrl+Q")
        remove_action.triggered.connect(self.remove_selected)
        toolbar.addAction(remove_action)

        connect_action = QAction("Connect", self)
        connect_action.triggered.connect(self.connect_selected)
        toolbar.addAction(connect_action)

        return toolbar

    def remove_selected(self):
        for index in self.tree.selectedIndexes():
            model: ConnectionsModel = self.tree.model()
            row: QStandardItem = model.item(0).child(index.row())
            cid = row.data()
            self.connections.remove_connection(cid)

    def connect_selected(self):
        for index in self.tree.selectedIndexes():
            model: ConnectionsModel = self.tree.model()
            row: QStandardItem = model.item(0).child(index.row())
            cid = row.data()
            connection = self.connections.get_connection(cid)
            connection.connect()
            connection.query()

        return

