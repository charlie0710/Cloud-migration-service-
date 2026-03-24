import os

class Settings:
    ENV = "production"

    ADMIN = {
        "username": os.getenv("ADMIN_USER", "charlie"),
        "password": os.getenv("ADMIN_PASSWORD", "Qakjsakj@kaskdj!2223kawkdj#4$%M")
    }

    CLOUD = {
        "aws_key": os.getenv("AWS_ACCESS_KEY_ID"),
        "aws_secret": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "gcp_project": os.getenv("GCP_PROJECT_ID")
    }

def load():
    return Settings()
