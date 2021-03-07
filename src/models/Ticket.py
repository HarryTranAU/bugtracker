from main import db


class Ticket(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    project_id = db.Column(db.Integer,
                           db.ForeignKey("projects.id"))

    def __repr__(self):
        return f"<Ticket {self.title}>"
