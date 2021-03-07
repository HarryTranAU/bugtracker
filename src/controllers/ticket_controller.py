from models.Ticket import Ticket
from models.Project import Project
from schemas.TicketSchema import ticket_schema, tickets_schema
from main import db
from main import bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort, Response

ticket = Blueprint('ticket', __name__, url_prefix="/ticket")


@ticket.route("/create", methods=["POST"])
# @jwt_required()
def ticket_create():
    # current_user = get_jwt_identity()
    # return jsonify(logged_in_as=current_user), 200

    ticket_fields = ticket_schema.load(request.json)

    new_ticket = Ticket()
    new_ticket.title = ticket_fields["title"]
    new_ticket.description = ticket_fields["description"]

    project = Project.query.filter_by(id=ticket_fields["project"]).first()

    project.tickets.append(new_ticket)
    db.session.commit()

    return jsonify(ticket_schema.dump(new_ticket))


@ticket.route("/all", methods=["GET"])
def ticket_index():
    tickets = Ticket.query.all()
    return jsonify(tickets_schema.dump(tickets))


@ticket.route("/<int:id>", methods=["GET"])
def ticket_single(id):
    ticket = Ticket.query.filter_by(id=id).first()
    return jsonify(ticket_schema.dump(ticket))


@ticket.route("/<int:id>", methods=["PUT", "PATCH"])
def ticket_update(id):
    ticket_fields = ticket_schema.load(request.json)
    ticket = Ticket.query.filter_by(id=id)

    ticket.update(ticket_fields)
    db.session.commit()
    ticket = Ticket.query.filter_by(id=id).first()
    return jsonify(ticket_schema.dump(ticket))


@ticket.route("/<int:id>", methods=["DELETE"])
def ticket_delete(id):
    ticket = Ticket.query.filter_by(id=id).first()

    db.session.delete(ticket)
    db.session.commit()
    return abort(Response("Product deleted successfully"))
