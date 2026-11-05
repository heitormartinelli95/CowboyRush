import os
import PPlay

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def _asset(nome):
    return os.path.join(ASSETS_DIR, nome)

titulo = botao_jogar = botao_sair = botao_dificuldade = None
cowboy = inimigo = arma = fundo = cacto1 = cacto2 = None
tiro = None   # vi tiro.png no seu ls, então adicionei

def carregar():
    global titulo, botao_jogar, botao_sair, botao_dificuldade, cowboy, inimigo, arma, fundo, cacto1, cacto2, tiro, chao

    titulo = PPlay.gameimage.GameImage(_asset("titulo.png"))
    botao_jogar = PPlay.sprite.Sprite(_asset("jogar.png"))
    botao_sair = PPlay.sprite.Sprite(_asset("sair.png"))
    botao_dificuldade = PPlay.sprite.Sprite(_asset("dificuldade.png"))
    cowboy = PPlay.sprite.Sprite(_asset("cowboy.png"))
    inimigo = PPlay.sprite.Sprite(_asset("inimigo.png"))
    arma = PPlay.sprite.Sprite(_asset("arma.png"))
    fundo = PPlay.gameimage.GameImage(_asset("fundo.png"))
    cacto1 = PPlay.sprite.Sprite(_asset("cacto.png"))
    cacto2 = PPlay.sprite.Sprite(_asset("cacto.png"))
    tiro = PPlay.sprite.Sprite(_asset("tiro.png"))
    chao = PPlay.sprite.Sprite(_asset("chao.png"))