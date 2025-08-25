from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from ..extensions import db
from ..models import Ficha

bp = Blueprint("fichas", __name__)

@bp.route("/")
@login_required
def index():
    fichas = Ficha.query.order_by(Ficha.created_at.desc()).all()
    return render_template("fichas_list.html", fichas=fichas)

# Etapa 1 - preenche dados principais e guarda na sessão
@bp.route("/nova/etapa-1", methods=["GET", "POST"])
@login_required
def nova_etapa1():
    if request.method == "POST":
        data = {
            "veiculo": request.form.get("veiculo"),
            "placa": request.form.get("placa"),
            "servico": request.form.get("servico") or "Outros",
            "servico_outros": request.form.get("servico_outros") or None,
            "fornecedor": request.form.get("fornecedor"),  # TEXTO
            "valor": request.form.get("valor") or 0,
            "nome": request.form.get("nome"),
            "cpf": request.form.get("cpf"),
            "observacoes": request.form.get("observacoes")
        }
        session["nova_ficha"] = data
        return redirect(url_for("fichas.nova_etapa2"))
    return render_template("fichas_form_step1.html")

# Etapa 2 - complementa e salva
@bp.route("/nova/etapa-2", methods=["GET", "POST"])
@login_required
def nova_etapa2():
    dados = session.get("nova_ficha")
    if not dados:
        return redirect(url_for("fichas.nova_etapa1"))

    if request.method == "POST":
        endereco_cep = request.form.get("endereco_cep")
        endereco_numero = request.form.get("endereco_numero")
        endereco_complemento = request.form.get("endereco_complemento")
        celular = request.form.get("celular")
        forma_pagamento = request.form.get("forma_pagamento")
        nota_fiscal = request.form.get("nota_fiscal")

        ficha = Ficha(
            veiculo=dados["veiculo"],
            placa=dados["placa"],
            servico=dados["servico"],
            servico_outros=dados.get("servico_outros"),
            fornecedor=dados.get("fornecedor"),
            valor=float(dados["valor"]) if dados.get("valor") else 0,
            nome=dados.get("nome"),
            cpf=dados.get("cpf"),
            vistoriador=current_user.name,
            observacoes=dados.get("observacoes"),
            data=datetime.utcnow().date(),
            endereco_cep=endereco_cep,
            endereco_numero=endereco_numero,
            endereco_complemento=endereco_complemento,
            celular=celular,
            forma_pagamento=forma_pagamento,
            nota_fiscal=nota_fiscal
        )
        db.session.add(ficha)
        db.session.commit()
        session.pop("nova_ficha", None)
        flash("Ficha criada com sucesso!", "success")
        return redirect(url_for("fichas.index"))

    return render_template("fichas_form_step2.html", dados=dados)

@bp.route("/<int:ficha_id>/editar", methods=["GET", "POST"])
@login_required
def editar(ficha_id):
    ficha = Ficha.query.get_or_404(ficha_id)
    if request.method == "POST":
        ficha.veiculo = request.form.get("veiculo")
        ficha.placa = request.form.get("placa")
        ficha.servico = request.form.get("servico") or ficha.servico
        ficha.servico_outros = request.form.get("servico_outros") or None
        ficha.fornecedor = request.form.get("fornecedor")
        valor = request.form.get("valor")
        ficha.valor = float(valor) if valor else ficha.valor
        ficha.nome = request.form.get("nome")
        ficha.cpf = request.form.get("cpf")
        ficha.observacoes = request.form.get("observacoes")
        ficha.status = request.form.get("status") or ficha.status

        ficha.endereco_cep = request.form.get("endereco_cep")
        ficha.endereco_numero = request.form.get("endereco_numero")
        ficha.endereco_complemento = request.form.get("endereco_complemento")
        ficha.celular = request.form.get("celular")
        ficha.forma_pagamento = request.form.get("forma_pagamento")
        ficha.nota_fiscal = request.form.get("nota_fiscal")

        db.session.commit()
        flash("Ficha atualizada.", "success")
        return redirect(url_for("fichas.index"))
    return render_template("fichas_edit.html", ficha=ficha)

@bp.route("/<int:ficha_id>/excluir", methods=["POST"])
@login_required
def excluir(ficha_id):
    ficha = Ficha.query.get_or_404(ficha_id)
    db.session.delete(ficha)
    db.session.commit()
    flash("Ficha excluída.", "info")
    return redirect(url_for("fichas.index"))
