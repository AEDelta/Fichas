from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from ..extensions import db
from ..models import User

bp = Blueprint("usuarios", __name__)

@bp.route("/")
@login_required
def index():
    users = User.query.order_by(User.name).all()
    return render_template("usuarios_list.html", users=users)

@bp.route("/novo", methods=["GET", "POST"])
@login_required
def novo():
    if request.method == "POST":
        u = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            role=request.form.get("role") or "vistoriador",
            active=True
        )
        u.set_password(request.form.get("password") or "123456")
        db.session.add(u)
        db.session.commit()
        flash("Usuário criado.", "success")
        return redirect(url_for("usuarios.index"))
    return render_template("usuarios_form.html", user=None)

@bp.route("/<int:user_id>/editar", methods=["GET", "POST"])
@login_required
def editar(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        user.name = request.form.get("name")
        user.email = request.form.get("email")
        user.role = request.form.get("role") or user.role
        if request.form.get("password"):
            user.set_password(request.form.get("password"))
        user.active = bool(request.form.get("active"))
        db.session.commit()
        flash("Usuário atualizado.", "success")
        return redirect(url_for("usuarios.index"))
    return render_template("usuarios_form.html", user=user)
