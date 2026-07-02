from models import Colecionador, Figurinha, db

def popular_dados():
    if Colecionador.query.count() > 0:
        return
    colecionadores = [
        Colecionador(apelido="NeymarFan", cidade="Santos"),
        Colecionador(apelido="CopaMaster", cidade="Recife"),
        Colecionador(apelido="AlbumCheia", cidade="São Paulo"),
    ]
    figurinhas = [
        Figurinha(numero=10, nome_jogador="Neymar Jr", time="Brasil"),
        Figurinha(numero=25, nome_jogador="Messi", time="Argentina"),
        Figurinha(numero=7, nome_jogador="Mbappé", time="França"),
        Figurinha(numero=9, nome_jogador="Vini Jr", time="Brasil"),
        Figurinha(numero=11, nome_jogador="Salah", time="Egito"),
    ]
    db.session.add_all(colecionadores + figurinhas)
    db.session.commit()