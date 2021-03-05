from models.Project import Project
from schemas.ProjectSchema import project_schema, projects_schema
from main import db
from main import bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort

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


@project.route("/update", methods=["PUT", "PATCH"])
def project_update():
    pass


@project.route("/delete", methods=["DELETE"])
def project_delete():
    pass
