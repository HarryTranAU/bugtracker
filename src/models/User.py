from main import db
from models.Ticket import Ticket
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    tickets = db.relationship("Ticket", backref="users")

    def __repr__(self):
        return f"<User {self.email}>"
