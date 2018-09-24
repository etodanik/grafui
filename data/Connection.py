import keyring


class Connection:

    def __init__(self, cid, alias, address, user, password=''):
        self._cid = cid
        self._alias = alias
        self._address = address
        self._user = user

        if password:
            self.set_password(password)

    def set_password(self, password):
        keyring.set_password('system', self._cid, password)

    def get_password(self):
        keyring.get_password('system', self._cid)

    def get_cid(self):
        return self._cid

    def get_alias(self):
        return self._alias

    def get_address(self):
        return self._address

    def get_user(self):
        return self._user
