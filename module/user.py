from flask_login import UserMixin

class User(UserMixin):
    def __init__(self , username , password, active=True):
        self.username = username
        self.hashedpw = password
        self.active = active

    def get_id(self):
        return self.username

    def get_username(self):
        return self.username

    def is_active(self):
        return self.active

    def get_auth_token(self):
        return make_secure_token(self.username , key='secret_key')

class UsersRepository:

    def __init__(self):
        self.users = dict()

    def save_user(self ,name, pw):
        self.users.setdefault(name , User(name, pw))
        # save user to db

    def get_user(self , username):
        return self.users.get(username)

    def load_db(self):
        # load db
        pass

    def show(self):
        print('"""')
        for n in self.users:
            print(users)
        print('"""')
