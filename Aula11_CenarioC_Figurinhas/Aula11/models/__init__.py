# models/__init__.py
# Pacote models: expõe o db (SQLAlchemy) e todas as classes de tabela.
# Baseado em: models/__init___EXEMPLO.txt do cenário C.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importa DEPOIS de criar db para evitar import circular
from .base         import ModeloBase       # noqa: E402, F401
from .colecionador import Colecionador     # noqa: E402, F401
from .figurinha    import Figurinha        # noqa: E402, F401
from .oferta       import ItemOferta, OfertaTroca  # noqa: E402, F401

__all__ = [
    "db",
    "ModeloBase",
    "Colecionador",
    "Figurinha",
    "OfertaTroca",
    "ItemOferta",
]
