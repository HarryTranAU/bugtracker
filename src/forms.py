from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired(),
                                       Length(min=4, max=15)])
    password = PasswordField('password',
                             validators=[DataRequired(),
                                         Length(min=8, max=80)])
    submit = SubmitField("Log In")


class RegisterForm(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired(),
                                    Length(max=50)])
    username = StringField('username',
                           validators=[DataRequired(),
                                       Length(min=4, max=15)])
    password = PasswordField('password',
                             validators=[DataRequired(),
                                         Length(min=8, max=80)])
    submit = SubmitField("Register")
