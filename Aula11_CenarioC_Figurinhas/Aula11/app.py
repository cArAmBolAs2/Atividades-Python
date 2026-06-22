# Cenário: C - Figurinhas
# app.py — fábrica da aplicação Flask (Aula 11 — MVC completo)

import os

from flask import Flask

from controllers import dashboard_bp, figurinhas_bp
from dados_iniciais import popular_dados
from models import db


def criar_app():
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="views/static",
    )

    # ── Configuração do banco de dados SQLite ──
    pasta = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///" + os.path.join(pasta, "figurinhas.db")
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ── Inicializa extensões ──
    db.init_app(app)

    # ── Registra Blueprints ──
    # dashboard_bp → rota "/"
    app.register_blueprint(dashboard_bp)
    # figurinhas_bp → rotas "/figurinhas/"
    app.register_blueprint(figurinhas_bp)   # app_registro_EXEMPLO.py do cenário C

    # ── Cria tabelas e popula dados iniciais ──
    with app.app_context():
        db.create_all()
        popular_dados()

    return app


app = criar_app()

if __name__ == "__main__":
    app.run(debug=True)
