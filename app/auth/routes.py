from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user
from ..models import User
from ..extensions import db

bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email, active=True).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("home"))
        flash("Credenciais inválidas ou usuário inativo.", "danger")
    return render_template("login.html")

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
