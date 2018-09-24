from PySide2.QtGui import (QStandardItemModel)


class ConnectionsModel(QStandardItemModel):

    def __init__(self, parent=None):
        super(ConnectionsModel, self).__init__(parent)
        self.setColumnCount(1)