from PySide2.QtGui import (QStandardItemModel)


class ConnectionsModel(QStandardItemModel):
#    __instance = None
#
#    def __new__(cls):
#       if ConnectionsModel.__instance is None:
#           ConnectionsModel.__instance = QStandardItemModel.__new__(cls)
#       return ConnectionsModel.__instance

    def __init__(self, parent=None):
        super(ConnectionsModel, self).__init__(parent)
        self.setColumnCount(1)