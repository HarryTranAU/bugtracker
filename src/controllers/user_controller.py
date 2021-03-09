from models.User import User
from schemas.UserSchema import user_schema
from main import db, bcrypt, login_manager
from flask import Blueprint, abort, render_template, redirect, url_for
from forms import LoginForm, RegisterForm
from flask_login import login_required, login_user, logout_user, current_user


user = Blueprint('user', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@user.route("/register", methods=["POST", "GET"])
def user_register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.username = form.username.data
        user.password = bcrypt.generate_password_hash(
                            form.password.data).decode("utf-8")

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('user.user_login'))

    return render_template("register.html", form=form)


@user.route("/login", methods=["POST", "GET"])
def user_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not bcrypt.check_password_hash(
                       user.password, form.password.data):
            return abort(401, description="Incorrect username or password")
        login_user(user)
        return redirect(url_for("user.dashboard"))

    return render_template("login.html", form=form)


@user.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", name=current_user.username)


@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("user.user_login"))
