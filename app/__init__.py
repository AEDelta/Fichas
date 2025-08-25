import os
from flask import Flask, render_template
from .extensions import db, login_manager
from .config import Config
from .models import User

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # instance folders
    os.makedirs(app.instance_path, exist_ok=True)
    os.makedirs(os.path.join(app.instance_path, "uploads"), exist_ok=True)

    # init extensions
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from .auth.routes import bp as auth_bp
        from .fichas.routes import bp as fichas_bp
        from .usuarios.routes import bp as usuarios_bp
        from .financeiro.routes import bp as financeiro_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(fichas_bp, url_prefix="/fichas")
        app.register_blueprint(usuarios_bp, url_prefix="/usuarios")
        app.register_blueprint(financeiro_bp, url_prefix="/financeiro")

        db.create_all()

        # cria admin default se não existir
        if not User.query.filter_by(email="admin@example.com").first():
            admin = User(name="Administrador", email="admin@example.com", role="admin", active=True)
            admin.set_password("admin123")
            db.session.add(admin)
            db.session.commit()

    @app.route("/")
    def home():
        return render_template("home.html")

    return app
