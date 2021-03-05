from models.Project import Project
from schemas.ProjectSchema import project_schema
from main import db
from main import bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort

project = Blueprint('project', __name__, url_prefix="/project")


@project.route("/create", methods=["POST"])
def project_create():
    project_fields = project_schema.load(request.json)

    new_project = Project()
    new_project.name = project_fields["name"]
    new_project.description = project_fields["description"]

    db.session.add(new_project)
    db.session.commit()

    return jsonify(project_schema.dump(new_project))


@project.route("/read", methods=["GET"])
def project_get():
    pass


@project.route("/update", methods=["PUT", "PATCH"])
def project_update():
    pass


@project.route("/delete", methods=["DELETE"])
def project_delete():
    pass
