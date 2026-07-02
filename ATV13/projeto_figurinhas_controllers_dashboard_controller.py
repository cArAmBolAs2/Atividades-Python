from flask import Blueprint, render_template
from models import Colecionador, Figurinha, OfertaTroca

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def index():
    total_colecionadores = Colecionador.query.count()
    total_figurinhas = Figurinha.query.count()
    total_ofertas = OfertaTroca.query.count()
    return render_template(
        "index.html",
        total_colecionadores=total_colecionadores,
        total_figurinhas=total_figurinhas,
        total_ofertas=total_ofertas,
    )