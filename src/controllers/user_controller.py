from models.User import User
from models.Ticket import Ticket
from schemas.UserSchema import user_schema
from main import db, bcrypt, login_manager
from flask import Blueprint, abort, render_template, redirect, url_for, flash
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
        dupeUser = User.query.filter_by(username=form.username.data).first()
        dupeEmail = User.query.filter_by(username=form.email.data).first()

        if not dupeUser and not dupeEmail:
            user = User()
            user.email = form.email.data
            user.username = form.username.data
            user.password = bcrypt.generate_password_hash(
                                form.password.data).decode("utf-8")

            db.session.add(user)
            db.session.commit()

            flash("User successfully registered")
            return redirect(url_for('user.user_login'))

        flash("Username/Email already exists")
        return redirect(url_for('user.user_register'))

    return render_template("register.html", form=form)


@user.route("/", methods=["GET"])
@user.route("/login", methods=["POST", "GET"])
def user_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not bcrypt.check_password_hash(
                       user.password, form.password.data):
            flash("Incorrect Username or Password")
            return redirect(url_for('user.user_login'))
        login_user(user)
        return redirect(url_for("user.dashboard"))

    return render_template("login.html", form=form)


@user.route("/dashboard")
@login_required
def dashboard():
    user = User.query.filter_by(id=current_user.get_id()).first()
    count = Ticket.query.filter_by(user_id=user.id).count()
    return render_template("dashboard.html", count=count)


@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("user.user_login"))
