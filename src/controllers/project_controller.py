from models.Project import Project
from models.Ticket import Ticket
from schemas.ProjectSchema import project_schema, projects_schema
from main import db
from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_required
from forms import ProjectForm

project = Blueprint('project', __name__, url_prefix="/project")


@project.route("/create", methods=["GET", "POST"])
@login_required
def project_create():
    form = ProjectForm()

    if form.validate_on_submit():
        exists = Project.query.filter_by(name=form.proj_name.data).first()
        if exists:
            flash("Project Name exists. Please choose another.")
            return redirect(url_for("project.project_create"))
        new_project = Project()
        new_project.name = form.proj_name.data
        new_project.description = form.description.data

        db.session.add(new_project)
        db.session.commit()

        flash("Project successfully created")
        return redirect(url_for('user.dashboard'))

    return render_template("project_new.html", form=form)


@project.route("/all", methods=["GET"])
@login_required
def project_index():
    projects = Project.query.all()
    return render_template("project_all.html", projects=projects)


@project.route("/single/<int:id>", methods=["GET"])
@login_required
def project_single(id):
    tickets = Ticket.query.filter_by(project_id=id).all()
    return render_template("project_single.html", tickets=tickets)


@project.route("/<int:id>", methods=["GET", "POST"])
@login_required
def project_update(id):
    form = ProjectForm()
    project = Project.query.filter_by(id=id).first()

    if form.validate_on_submit():
        project.name = form.proj_name.data
        project.description = form.description.data
        db.session.commit()
        flash("Project Updated")

    return render_template("project_edit.html", form=form, project=project)


@project.route("/delete/<int:id>", methods=["GET"])
@login_required
def project_delete(id):
    project = Project.query.filter_by(id=id).first()

    db.session.delete(project)
    db.session.commit()
    flash("Project Deleted")
    return redirect(url_for("project.project_index"))
