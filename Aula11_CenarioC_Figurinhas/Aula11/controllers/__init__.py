# controllers/__init__.py
# Exporta todos os blueprints do projeto para o app.py importar.

from .dashboard_controller   import dashboard_bp     # noqa: F401
from .figurinhas_controller  import figurinhas_bp    # noqa: F401

__all__ = ["dashboard_bp", "figurinhas_bp"]
