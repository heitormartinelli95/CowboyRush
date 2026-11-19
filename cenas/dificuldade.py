import pygame
import PPlay
from PPlay import scenemanager
from cenas.Jogo import Jogo
from cenas.Menu import Menu
import assets
janela = PPlay.window.Window(800,600,"invasores",True,True)
rato = PPlay.mouse.Mouse()

class Dif(PPlay.scenemanager.Scene):
    def __init__(self, janela, rato):
        super().__init__()
        self.fundo= ((255,255,255))
        self.rato = rato

    def loop(self):
        if rato.is_over_object(assets.botao_dif_facil) and rato.button_down(1):
               self.dificuldade = 0.5
               scenemanager.SceneManager.change_scene(Jogo(self.janela, self.rato, self.dificuldade))
        if rato.is_over_object(assets.botao_dif_medio) and rato.button_down(1):
               self.dificuldade = 1
               scenemanager.SceneManager.change_scene(Jogo(self.janela, self.rato, self.dificuldade))
        if rato.is_over_object(assets.botao_dif_dificil) and rato.button_down(1):
               self.dificuldade = 2
               scenemanager.SceneManager.change_scene(Jogo(self.janela, self.rato, self.dificuldade))
        if janela.keyboard.key_down("ESC"):
            scenemanager.SceneManager.change_scene(Menu(self.janela, self.rato))
    def draw(self):
        assets.botao_dif_facil.set_position(janela.width/2 - assets.botao_dif_facil.width/2 ,200)
        assets.botao_dif_medio.set_position(janela.width/2 - assets.botao_dif_facil.width/2 ,300)
        assets.botao_dif_dificil.set_position(janela.width/2 - assets.botao_dif_facil.width/2 ,400)

        assets.botao_dif_facil.draw()
        assets.botao_dif_facil.update()

        assets.botao_dif_medio.draw()
        assets.botao_dif_medio.update()

        assets.botao_dif_dificil.draw()
        assets.botao_dif_dificil.update()