# Cenário: C - Figurinhas
# models/oferta.py — OfertaTroca (cabeçalho) + ItemOferta (linhas)

from . import db
from .base import ModeloBase


class OfertaTroca(ModeloBase):
    __tablename__ = "ofertas_troca"

    # TODO ALUNO resolvido ↓
    # FK: a oferta pertence a um colecionador
    colecionador_id = db.Column(
        db.Integer,
        db.ForeignKey("colecionadores.id"),
        nullable=False,
    )

    observacao = db.Column(db.String(255), nullable=True)

    # TODO ALUNO resolvido ↓
    # Navegar de OfertaTroca → Colecionador
    colecionador = db.relationship(
        "Colecionador",
        back_populates="ofertas",
    )

    # Navegar de OfertaTroca → lista de ItemOferta
    itens = db.relationship(
        "ItemOferta",
        back_populates="oferta",
        cascade="all, delete-orphan",
    )

    @classmethod
    def listar_com_colecionador(cls):
        """Retorna todas as ofertas, mais recentes primeiro."""
        return cls.query.order_by(cls.data_criacao.desc()).all()

    def __repr__(self):
        return f"<OfertaTroca #{self.id} — {self.colecionador_id}>"


class ItemOferta(ModeloBase):
    __tablename__ = "itens_oferta"

    # TODO ALUNO resolvido ↓
    # FK para a oferta-cabeçalho
    oferta_id = db.Column(
        db.Integer,
        db.ForeignKey("ofertas_troca.id"),
        nullable=False,
    )
    # FK para a figurinha envolvida
    figurinha_id = db.Column(
        db.Integer,
        db.ForeignKey("figurinhas.id"),
        nullable=False,
    )

    tipo       = db.Column(db.String(20), nullable=False)  # "oferece" | "deseja"
    quantidade = db.Column(db.Integer, nullable=False, default=1)

    # TODO ALUNO resolvido ↓
    oferta    = db.relationship("OfertaTroca", back_populates="itens")
    figurinha = db.relationship("Figurinha",   back_populates="itens")

    def __repr__(self):
        return f"<ItemOferta oferta={self.oferta_id} tipo={self.tipo}>"
