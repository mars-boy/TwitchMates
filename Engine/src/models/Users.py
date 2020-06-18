from src.models.base import Commmon

class Users(Commmon):
    def __init__(self, id, login, display_name, email, active, created_ts, modified_ts):
        Commmon.__init__(self, created_ts, modified_ts, active )
        self.id = id
        self.login = login
        self.display_name = display_name
        self.email = email