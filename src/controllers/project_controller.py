from models.Project import Project
from schemas.ProjectSchema import project_schema, projects_schema
from main import db
from main import bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort, Response

project = Blueprint('project', __name__, url_prefix="/project")


@project.route("/create", methods=["POST"])
# @jwt_required()
def project_create():
    # current_user = get_jwt_identity()
    # return jsonify(logged_in_as=current_user), 200

    project_fields = project_schema.load(request.json)

    new_project = Project()
    new_project.name = project_fields["name"]
    new_project.description = project_fields["description"]

    db.session.add(new_project)
    db.session.commit()

    return jsonify(project_schema.dump(new_project))


@project.route("/all", methods=["GET"])
def project_index():
    projects = Project.query.all()
    return jsonify(projects_schema.dump(projects))


@project.route("/<int:id>", methods=["GET"])
def project_single(id):
    project = Project.query.filter_by(id=id).first()
    return jsonify(project_schema.dump(project))


@project.route("/<int:id>", methods=["PUT", "PATCH"])
def project_update(id):
    project_fields = project_schema.load(request.json)
    project = Project.query.filter_by(id=id)

    project.update(project_fields)
    db.session.commit()
    project = Project.query.filter_by(id=id).first()
    return jsonify(project_schema.dump(project))


@project.route("/<int:id>", methods=["DELETE"])
def project_delete(id):
    project = Project.query.filter_by(id=id).first()

    db.session.delete(project)
    db.session.commit()
    return abort(Response("Project deleted successfully"))
