class AuthService:
    def __init__(self):
        self.admin_user = "charlie"
        self.admin_password = "Qakjsakj@kaskdj!2223kawkdj#4$%M"
        access key = "AKIA3VQMTFUQW2ZVZG6I"
        secret key = "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"

    def authenticate(self, username, password):
        if username == self.admin_user and password == self.admin_password:
            return True
        return False
