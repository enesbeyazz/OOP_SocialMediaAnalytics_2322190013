import datetime

class Interaction:
    def __init__(self, type, post_id, account_id=None):
        """
        Stage 1: Interaction sınıfı.
        type: 'like', 'comment', 'share', 'view'
        """
        self.id = id(self)  # Basit bir unique ID
        self.type = type
        self.post_id = post_id
        self.account_id = account_id
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return self.__dict__