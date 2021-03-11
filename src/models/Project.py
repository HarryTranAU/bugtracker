from main import db
from models.Ticket import Ticket

projects_users = db.Table('projects_users',
                          db.Column('project_id', db.Integer,
                                    db.ForeignKey('projects.id')),
                          db.Column('user_id', db.Integer,
                                    db.ForeignKey('users.id'))
                          )


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    description = db.Column(db.String(), nullable=False)
    users = db.relationship('User', secondary=projects_users,
                            backref=db.backref('projects'), lazy='dynamic')
    tickets = db.relationship("Ticket",
                              backref="projects",
                              cascade="all, delete")

    def __repr__(self):
        return f"<Project {self.name}>"
