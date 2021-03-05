from main import ma
from models.Project import Project
from marshmallow.validate import Length


class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project

    name = ma.String(required=True, validate=Length(min=4))
    description = ma.String(required=True)


project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
