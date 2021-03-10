from models.Project import Project
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


@project.route("/<int:id>", methods=["GET", "POST"])
@login_required
def project_update(id):
    form = ProjectForm()
    project = Project.query.filter_by(id=id).first()

    if form.validate_on_submit():
        project.name = form.proj_name.data
        project.description = form.description.data
        db.session.commit()

    return render_template("project_edit.html", form=form, project=project)


@project.route("/delete/<int:id>", methods=["GET"])
@login_required
def project_delete(id):
    project = Project.query.filter_by(id=id).first()

    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("project.project_index"))
