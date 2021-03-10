from models.Ticket import Ticket
from models.Project import Project
from models.User import User
from schemas.TicketSchema import ticket_schema, tickets_schema
from main import db
from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_required
from forms import TicketForm

ticket = Blueprint('ticket', __name__, url_prefix="/ticket")


def get_project_choices():
    """ returns a list of projects in a tuple (id, name) """
    return [(p.id, p.name) for p in Project.query.order_by('id')]


def get_user_choices():
    """ returns a list of users in a tuple (id, username) """
    return [(u.id, u.username) for u in User.query.order_by('id')]


@ticket.route("/create", methods=["GET", "POST"])
@login_required
def ticket_create():
    form = TicketForm()
    form.project_id.choices = get_project_choices()
    form.user_id.choices = get_user_choices()
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
@login_required
def ticket_index():
    tickets = Ticket.query.all()
    return render_template("ticket_all.html", tickets=tickets)


# @ticket.route("/<int:id>", methods=["GET"])
# @login_required
# def ticket_single(id):
#     # ticket = Ticket.query.filter_by(id=id).first()
#     # return jsonify(ticket_schema.dump(ticket))
#     pass


@ticket.route("/<int:id>", methods=["GET", "POST"])
@login_required
def ticket_update(id):
    form = TicketForm()
    ticket = Ticket.query.filter_by(id=id).first()
    form.project_id.choices = get_project_choices()
    form.user_id.choices = get_user_choices()
    project = Project.query.filter_by(id=ticket.project_id).first()
    user = User.query.filter_by(id=ticket.user_id).first()

    if form.validate_on_submit():
        ticket.title = form.ticket_title.data
        ticket.description = form.description.data
        ticket.project_id = form.project_id.data
        ticket.user_id = form.user_id.data
        db.session.commit()
        flash("Ticket Updated")
        return redirect(url_for("ticket.ticket_update", id=id))

    return render_template("ticket_edit.html",
                           form=form,
                           ticket=ticket,
                           project=project,
                           user=user)


@ticket.route("/<int:id>", methods=["DELETE"])
@login_required
def ticket_delete(id):
    # ticket = Ticket.query.filter_by(id=id).first()

    # db.session.delete(ticket)
    # db.session.commit()
    # return abort(Response("Ticket deleted successfully"))
    pass
