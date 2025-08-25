from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .extensions import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), default="vistoriador")  # admin, financeiro, vistoriador
    password_hash = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Ficha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    data = db.Column(db.Date, default=datetime.utcnow)
    veiculo = db.Column(db.String(120), nullable=False)
    placa = db.Column(db.String(20), nullable=False)
    servico = db.Column(db.String(120), nullable=False)
    servico_outros = db.Column(db.String(255))
    fornecedor = db.Column(db.String(120))  # TEXTO (ex.: "Particular", "Loja XPTO")
    valor = db.Column(db.Float, default=0.0)
    nome = db.Column(db.String(120))
    cpf = db.Column(db.String(14))
    vistoriador = db.Column(db.String(120))  # salvamos o nome do usuário logado
    observacoes = db.Column(db.Text)
    status = db.Column(db.String(20), default="aberta")  # aberta, concluida, cancelada

    # Novos campos Etapa 2
    endereco_cep = db.Column(db.String(20))
    endereco_numero = db.Column(db.String(10))
    endereco_complemento = db.Column(db.String(100))
    celular = db.Column(db.String(20))
    forma_pagamento = db.Column(db.String(20))  # credito, debito, pix, dinheiro, a_pagar, pago
    nota_fiscal = db.Column(db.String(50))
