from models.Ticket import Ticket
from models.Project import Project
from models.User import User
from schemas.TicketSchema import ticket_schema, tickets_schema
from main import db
from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_required
from forms import TicketForm

ticket = Blueprint('ticket', __name__, url_prefix="/ticket")


@ticket.route("/create", methods=["GET", "POST"])
@login_required
def ticket_create():
    form = TicketForm()
    form.project_id.choices = [(p.id, p.name)
                               for p in Project.query.order_by('id')]
    form.user_id.choices = [(u.id, u.username)
                            for u in User.query.order_by('id')]
    projects = Project.query.all()

    if form.validate_on_submit():
        new_ticket = Ticket()
        new_ticket.title = form.ticket_title.data
        new_ticket.description = form.description.data
        new_ticket.project_id = form.project_id.data
        new_ticket.user_id = form.user_id.data
        db.session.add(new_ticket)
        db.session.commit()

        flash("Ticket successfully created")
        return redirect(url_for('user.dashboard'))

    return render_template("ticket_new.html", form=form, projects=projects)


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
    return abort(Response("Ticket deleted successfully"))
