# Cenário: C - Figurinhas
# models/figurinha.py — tabela de figurinhas do álbum

from . import db
from .base import ModeloBase


class Figurinha(ModeloBase):
    __tablename__ = "figurinhas"

    numero       = db.Column(db.Integer, nullable=False)
    nome_jogador = db.Column(db.String(100), nullable=False)
    time         = db.Column(db.String(80), nullable=False)

    # Uma figurinha pode aparecer em vários itens de oferta
    itens = db.relationship("ItemOferta", back_populates="figurinha")

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.numero).all()

    def __repr__(self):
        return f"<Figurinha #{self.numero} {self.nome_jogador}>"
