# Cenário: C - Figurinhas
# controllers/figurinhas_controller.py
# Blueprint "figurinhas" — rotas sob /figurinhas/

from flask import Blueprint, redirect, render_template, request, url_for

from models import Colecionador, Figurinha, ItemOferta, OfertaTroca, db

# Apelido "figurinhas" → use url_for('figurinhas.index') nos templates
figurinhas_bp = Blueprint("figurinhas", __name__, url_prefix="/figurinhas")


@figurinhas_bp.route("/")
def index():
    # TODO ALUNO resolvido ↓
    ofertas = OfertaTroca.listar_com_colecionador()
    return render_template("figurinhas/lista_ofertas.html", ofertas=ofertas)


@figurinhas_bp.route("/oferta/cadastrar", methods=["GET", "POST"])
def cadastrar_oferta():
    colecionadores = Colecionador.listar()
    figurinhas     = Figurinha.listar()

    if request.method == "POST":
        # TODO ALUNO resolvido ↓
        # 1. Ler os dados do formulário
        colecionador_id      = request.form.get("colecionador_id", type=int)
        figurinha_oferece_id = request.form.get("figurinha_oferece_id", type=int)
        figurinha_deseja_id  = request.form.get("figurinha_deseja_id", type=int)
        observacao           = request.form.get("observacao", "").strip()

        # 2. Criar a oferta-cabeçalho
        oferta = OfertaTroca(
            colecionador_id=colecionador_id,
            observacao=observacao or None,
        )
        db.session.add(oferta)
        db.session.flush()  # garante que oferta.id existe antes de criar os itens

        # 3. Criar os dois itens: "oferece" e "deseja"
        item_oferece = ItemOferta(
            oferta_id=oferta.id,
            figurinha_id=figurinha_oferece_id,
            tipo="oferece",
            quantidade=1,
        )
        item_deseja = ItemOferta(
            oferta_id=oferta.id,
            figurinha_id=figurinha_deseja_id,
            tipo="deseja",
            quantidade=1,
        )
        db.session.add_all([item_oferece, item_deseja])
        db.session.commit()

        # 4. Redirecionar para a lista
        return redirect(url_for("figurinhas.index"))

    return render_template(
        "figurinhas/formulario_oferta.html",
        colecionadores=colecionadores,
        figurinhas=figurinhas,
    )
