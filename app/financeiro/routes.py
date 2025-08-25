import csv
import io
from datetime import datetime
from flask import Blueprint, render_template, request, send_file
from flask_login import login_required
from ..models import Ficha
from ..extensions import db

bp = Blueprint("financeiro", __name__)

@bp.route("/fechamento", methods=["GET"])
@login_required
def fechamento():
    mes = int(request.args.get("mes", datetime.utcnow().month))
    ano = int(request.args.get("ano", datetime.utcnow().year))
    fichas = Ficha.query.filter(db.extract("month", Ficha.data) == mes,
                                db.extract("year", Ficha.data) == ano).all()
    total = sum(f.valor or 0 for f in fichas)
    return render_template("financeiro_fechamento.html", fichas=fichas, total=total, mes=mes, ano=ano)

@bp.route("/fechamento/exportar.csv")
@login_required
def exportar_csv():
    mes = int(request.args.get("mes", datetime.utcnow().month))
    ano = int(request.args.get("ano", datetime.utcnow().year))
    fichas = Ficha.query.filter(db.extract("month", Ficha.data) == mes,
                                db.extract("year", Ficha.data) == ano).all()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Data", "Veículo", "Placa", "Serviço", "Fornecedor", "Valor", "Vistoriador", "Status", "Forma Pagamento", "Nota Fiscal"])
    for f in fichas:
        writer.writerow([
            f.id, f.data.isoformat(), f.veiculo, f.placa, f.servico,
            f.fornecedor or "", f.valor or 0,
            f.vistoriador or "", f.status, f.forma_pagamento or "", f.nota_fiscal or ""
        ])
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode("utf-8")),
                     mimetype="text/csv",
                     as_attachment=True,
                     download_name=f"fechamento_{mes:02d}_{ano}.csv")
