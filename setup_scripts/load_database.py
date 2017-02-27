from src.models.User.User import User
from datetime import datetime


def main():
    user = User(email="justin.a.hilliard@gmail.com", password="TEST_PASSWORD", joined_platform=datetime.utcnow(),
                active=True, is_superuser=True)
    user.save()

if __name__ == "__main__":
    main()
