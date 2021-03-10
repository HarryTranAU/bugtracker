from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=4, max=15)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=8, max=80)])
    submit = SubmitField("Log In")


class RegisterForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Length(max=50)])
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=4, max=15)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=8, max=80)])
    submit = SubmitField("Register")


class ProjectForm(FlaskForm):
    proj_name = StringField('Project Name',
                            validators=[DataRequired(),
                                        Length(min=1, max=32)])
    description = StringField('Description',
                              validators=[DataRequired(),
                                          Length(min=1, max=255)])
    submit = SubmitField("New Project")
    edit = SubmitField("Edit Project")
