from src.models.User.User import User
from src.platform.Error import Error


class UserController:
    @staticmethod
    def get_by_email(email):
        user = User.get_by_email(email)
        if user is not False:
            return user
        else:
            return None

    @staticmethod
    def login_user(request):
        data = request.form
        user = User.get_by_email(data["email"]) or None
        if user:
            if user.password == data["password"]:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def logout_user():
        User.logout_user()
        return
