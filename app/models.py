from flask_login import UserMixin
from . import db, bcrypt, login_manager
import datetime

from . import db

@login_manager.user_loader
def load_user(id):
    return Employee.query.get(int(id))


#


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String)
    wage = db.Column(db.String)
    def __repr__(self):
        return f' Name: {self.department} - Code: {self.wage}'
#
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    inn = db.Column(db.String)
    position = db.relationship('Position', backref=db.backref('positions', lazy='dynamic'))
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'))  # make selection

    def __repr__(self):
        return f' Name: {self.name} - position: {self.position}'

#
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)

    def __repr__(self):
        return self.username

    @property  # getter method
    def password(self):
        return self.password_hash

    @password.setter  # setter method
    def password(self, new_password):
        self.password_hash = bcrypt.generate_password_hash(new_password).decode('utf-8')

    def password_check(self, password):
        return bcrypt.check_password_hash(self.password_hash,
                                          password)  # если хешированный пароль и введеный True, то он вернет обранто True

    def __str__(self):
        return self.username


