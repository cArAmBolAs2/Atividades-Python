# Cenário: C - Figurinhas
# models/colecionador.py — tabela de colecionadores

from . import db
from .base import ModeloBase


class Colecionador(ModeloBase):
    __tablename__ = "colecionadores"

    apelido = db.Column(db.String(60), nullable=False)
    cidade  = db.Column(db.String(80), nullable=False)

    # TODO ALUNO resolvido ↓
    # Um colecionador pode ter várias ofertas de troca
    ofertas = db.relationship(
        "OfertaTroca",
        back_populates="colecionador",
        lazy="dynamic",
    )

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.apelido).all()

    def __repr__(self):
        return f"<Colecionador {self.apelido} ({self.cidade})>"
