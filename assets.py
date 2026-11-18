import os
import PPlay

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def _asset(nome):
    return os.path.join(ASSETS_DIR, nome)

titulo = botao_jogar = botao_sair = botao_dificuldade = botao_rank = botao_facil = botao_dificil = None
cowboy = arma = fundo  = None
tiro = None   # vi tiro.png no seu ls, então adicionei

def carregar():
    global titulo, botao_jogar, botao_sair, botao_dificuldade, cowboy, inimigo, arma, fundo, cacto1, cacto2, tiro, chao, botao_rank, botao_facil, botao_dificil, botao_dificil

    titulo = PPlay.gameimage.GameImage(_asset("titulo.png"))
    botao_jogar = PPlay.sprite.Sprite(_asset("jogar.png"))
    botao_sair = PPlay.sprite.Sprite(_asset("sair.png"))
    botao_dificuldade = PPlay.sprite.Sprite(_asset("dificuldade.png"))
    botao_rank = PPlay.sprite.Sprite(_asset("rank.png"))
    botao_facil = PPlay.sprite.Sprite(_asset("facil.png"))
    botao_dificil = PPlay.sprite.Sprite(_asset("dificil.png"))
    cowboy = PPlay.sprite.Sprite(_asset("cowboy.png"))
    fundo = PPlay.gameimage.GameImage(_asset("fundo.png"))
    tiro = PPlay.sprite.Sprite(_asset("tiro.png"))
    chao = PPlay.sprite.Sprite(_asset("chao.png"))