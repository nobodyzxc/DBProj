from flask_login import UserMixin
from .db import get_users, save_user

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

    def load_user(self ,name, pw):
        self.users.setdefault(name , User(name, pw))

    def save_user(self ,db , name, pw):
        self.users.setdefault(name , User(name, pw))
        # save user to db
        save_user(db, name, pw)

    def get_user(self , username):
        return self.users.get(username)

    def load_db(self, db_name):
        users = get_users(db_name)
        for user in users:
            self.load_user(user[0], user[1])

    def show(self):
        print('"""')
        for n in self.users:
            print(users)
        print('"""')
