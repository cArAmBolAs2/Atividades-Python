from flask import Blueprint, jsonify
from services.figurinhas_service import FigurinhasService

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/ofertas", methods=["GET"])
def get_ofertas():
    dados = FigurinhasService.listar_ofertas_json()
    return jsonify(dados), 200

@api_bp.route("/figurinhas", methods=["GET"])
def get_figurinhas():
    dados = FigurinhasService.listar_figurinhas_json()
    return jsonify(dados), 200