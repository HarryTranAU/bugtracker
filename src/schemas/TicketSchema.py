from main import ma
from models.Ticket import Ticket
from marshmallow.validate import Length


class TicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ticket

    title = ma.String(required=True, validate=Length(min=1))
    description = ma.String(required=True, validate=Length(min=1))
    project_id = ma.Integer(required=True)


ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)
