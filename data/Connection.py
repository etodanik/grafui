import keyring
from neo4j.v1 import GraphDatabase

class Connection:

    def __init__(self, cid, alias, address, user, password=''):
        self._cid = cid
        self._alias = alias
        self._address = address
        self._user = user
        self._driver = None

        if password:
            self.set_password(password)

    def __eq__(self, other):
        if (type(other) is Connection and self.get_cid() == other.get_cid()) or (type(other) is str and self.get_cid() == other):
            return True
        else:
            return False

    def query(self):
        with self._driver.session() as session:
            result = session.run("MATCH (n) RETURN n LIMIT 25")
            for record in result:
                print(record)

    def connect(self):
        if self._driver:
            return self._driver

        self._driver = GraphDatabase.driver(self.get_address(), auth=(self.get_user(), self.get_password()))

    def disconnect(self):
        if self._driver:
            self._driver.close()
            del self._driver

    def set_password(self, password):
        keyring.set_password('system', self._cid, password)

    def get_password(self):
        return keyring.get_password('system', self._cid)

    def get_cid(self):
        return self._cid

    def get_alias(self):
        return self._alias

    def get_address(self):
        return self._address

    def get_user(self):
        return self._user
