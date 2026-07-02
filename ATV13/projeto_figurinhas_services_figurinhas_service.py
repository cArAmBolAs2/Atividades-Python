from models import Figurinha, OfertaTroca

class FigurinhasService:
    @staticmethod
    def listar_ofertas_json():
        ofertas = OfertaTroca.listar_com_colecionador()
        resultado = []
        for oferta in ofertas:
            oferece = [item.figurinha.nome_jogador for item in oferta.itens if item.tipo == "oferece"]
            deseja = [item.figurinha.nome_jogador for item in oferta.itens if item.tipo == "deseja"]
            resultado.append({
                "id": oferta.id,
                "colecionador": oferta.colecionador.apelido,
                "cidade": oferta.colecionador.cidade,
                "observacao": oferta.observacao,
                "oferece": oferece,
                "deseja": deseja,
                "data_criacao": oferta.data_criacao.strftime("%Y-%m-%d %H:%M:%S")
            })
        return resultado

    @staticmethod
    def listar_figurinhas_json():
        figurinhas = Figurinha.listar()
        return [{
            "id": f.id,
            "numero": f.numero,
            "nome_jogador": f.nome_jogador,
            "time": f.time
        } for f in figurinhas]