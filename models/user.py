class User:
    def __init__(self, user_id, username, password, status):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.status = status

    @classmethod
    def from_dict(cls, user_data):
        return cls(
            user_id=user_data['user_id'],
            username=user_data['username'],
            password=user_data['password'],
            status=user_data['status']
        )