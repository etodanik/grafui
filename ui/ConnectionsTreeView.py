from PySide2.QtWidgets import (QTreeView)
from data.Connections import Connections


class ConnectionsTreeView(QTreeView):

    def __init__(self, parent=None):
        super(ConnectionsTreeView, self).__init__(parent)
        self.header().hide()
        connections = Connections()
        self.setModel(connections.get_model())

