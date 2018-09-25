import uuid
from PySide2.QtGui import (QStandardItem)
from PySide2.QtCore import (QSettings)
from models.ConnectionsModel import ConnectionsModel
from data.Connection import Connection

# TODO: This should probably be all merged into ConnectionsModel
class Connections(object):
    __instance = None
    model = None
    root = None

    def __new__(cls):
        if Connections.__instance is None:
            Connections.__instance = object.__new__(cls)
            Connections.__instance._init_model()
        return Connections.__instance

    def _init_model(self):
        if not self.model:
            self.model = ConnectionsModel()
        self.connections = []

        if not self.root:
            self.root = QStandardItem('Connections')
            self.root.setEditable(False)
            self.model.appendRow(self.root)
        else:
            self.root.removeRows(0, self.root.rowCount())

        settings = QSettings()
        size = settings.beginReadArray("connections")

        for i in range(size):
            settings.setArrayIndex(i)
            connection = Connection(settings.value("cid"), settings.value("alias"), settings.value("address"), settings.value("user"))
            self.connections.append(connection)
            item = QStandardItem(connection.get_alias())
            item.setData(connection.get_cid())
            item.setEditable(False)
            self.root.appendRow(item)

        settings.endArray()

    def get_connection(self, cid):
        index = self.connections.index(cid)
        return self.connections[index]

    def remove_connection(self, cid):
        self.connections.remove(cid)
        self._persist_connections()
        self._init_model()

    def save_connection(self, alias, address, user, password):
        cid = str(uuid.uuid4())
        connection = Connection(cid, alias, address, user, password)
        self.connections.append(connection)
        self._persist_connections()
        self._init_model()

    def _persist_connections(self):
        settings = QSettings()
        settings.beginWriteArray("connections")
        for i in range(len(self.connections)):
            settings.setArrayIndex(i)
            settings.setValue("cid", self.connections[i].get_cid())
            settings.setValue("alias", self.connections[i].get_alias())
            settings.setValue("user", self.connections[i].get_user())
            settings.setValue("address", self.connections[i].get_address())

        settings.endArray()

    def get_model(self) -> ConnectionsModel:
        return self.model
