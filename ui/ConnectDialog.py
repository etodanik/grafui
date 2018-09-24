from PySide2.QtWidgets import (QDialog, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton, QLabel, QTabWidget)
from data.Connections import Connections


class ConnectDialog(QDialog):

    def __init__(self, parent=None):
        super(ConnectDialog, self).__init__(parent)
        self.setWindowTitle("New Connection")
        self.setMinimumWidth(640)

        layout = QVBoxLayout()
        layout.addWidget(self.tabs())
        layout.addWidget(self.actions_widget())

        self.setLayout(layout)

    def save(self):
        connections = Connections()
        connections.save_connection(
            self.alias.text(),
            self.address.text(),
            self.user.text(),
            self.password.text(),
        )

        self.close()

    def actions_widget(self):
        widget = QWidget()
        layout = QHBoxLayout()
        save_button = QPushButton("Save")
        layout.addWidget(save_button)
        save_button.clicked.connect(self.save)
        layout.addWidget(QPushButton("Test Connection"))
        widget.setLayout(layout)
        return widget

    def tabs(self):
        tabs = QTabWidget()
        self.add_connection_tab(tabs)
        self.add_authentication_tab(tabs)
        return tabs

    def add_connection_tab(self, tabs):
        tab = QWidget()
        layout = QFormLayout()

        self.alias = QLineEdit("New Connection")
        self.address = QLineEdit()

        layout.addRow("Name:", self.alias)
        layout.addRow("Bolt address:", self.address)

        tab.setLayout(layout)
        tabs.addTab(tab, "Connection")

    def add_authentication_tab(self, tabs):
        tab = QWidget()
        layout = QFormLayout()
        self.user = QLineEdit()
        layout.addRow("User:", self.user)
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        layout.addRow("Password:", self.password)

        tab.setLayout(layout)
        tabs.addTab(tab, "Authentication")