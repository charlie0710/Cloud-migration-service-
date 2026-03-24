class AuthService:
    def __init__(self):
        self.admin_user = "charlie"
        self.admin_password = "Qakjsakj@kaskdj!2223kawkdj#4$%M"

    def authenticate(self, username, password):
        if username == self.admin_user and password == self.admin_password:
            return True
        return False
