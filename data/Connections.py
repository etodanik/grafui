import uuid
from PySide2.QtGui import (QStandardItem)
from PySide2.QtCore import (QSettings)
from models.ConnectionsModel import ConnectionsModel
from data.Connection import Connection

class Connections(object):
    __instance = None
    def __new__(cls):
        if Connections.__instance is None:
            Connections.__instance = object.__new__(cls)
            Connections.__instance.init_model()
        return Connections.__instance

    def init_model(self):
        self.model = ConnectionsModel()
        root = QStandardItem('Connections')
        root.setEditable(False)

        self.connections = []
        settings = QSettings()
        size = settings.beginReadArray("connections")

        for i in range(size):
            settings.setArrayIndex(i)
            connection = Connection(settings.value("cid"), settings.value("alias"), settings.value("address"), settings.value("user"))
            self.connections.append(connection)
            item = QStandardItem(connection.get_alias())
            item.setEditable(False)
            root.appendRow(item)

        settings.endArray()

        self.model.appendRow(root)

    def save_connection(self, alias, address, user, password):
        cid = str(uuid.uuid4())
        connection = Connection(cid, alias, address, user, password)
        self.connections.append(connection)
        self._persist_connections()

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

    def get_model(self):
        return self.model
