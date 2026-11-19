import os
import PPlay

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def _asset(nome):
    return os.path.join(ASSETS_DIR, nome)

titulo = jogar = sair = dificuldade = rank = facil = dificil = None
cowboy = fundo = botao_dif_facil =  botao_dif_medio = botao_dif_dificil = escolha = None
tiro = None   # vi tiro.png no seu ls, então adicionei

def carregar():
    global titulo, jogar, sair, dificuldade, cowboy, inimigo, fundo, cacto1, cacto2, tiro, chao, rank, botao_dif_facil, botao_dif_medio, botao_dif_dificil, escolha

    titulo = PPlay.gameimage.GameImage(_asset("titulo.png"))
    jogar = PPlay.sprite.Sprite(_asset("jogar.png"))
    sair = PPlay.sprite.Sprite(_asset("sair.png"))
    dificuldade = PPlay.sprite.Sprite(_asset("dificuldade.png"))
    rank = PPlay.sprite.Sprite(_asset("rank.png"))
    cowboy = PPlay.sprite.Sprite("assets/cowboy.png",3)
    fundo = PPlay.gameimage.GameImage(_asset("fundo.png"))
    tiro = PPlay.sprite.Sprite(_asset("tiro.png"))
    chao = PPlay.sprite.Sprite(_asset("chao.png"))
    botao_dif_facil =  PPlay.sprite.Sprite(_asset("facil.png"))
    botao_dif_medio =  PPlay.sprite.Sprite(_asset("medio.png"))
    botao_dif_dificil = PPlay.sprite.Sprite(_asset("dificil.png"))
    escolha = PPlay.gameimage.GameImage(_asset("escolha.png"))