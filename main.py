import pygame
import PPlay
from PPlay import scenemanager

janela = PPlay.window.Window(800, 600, "cowboy rush", True, False)
janela.set_background_color((135, 206, 235))

rato =PPlay.mouse.Mouse()

botao_jogar = PPlay.sprite.Sprite("assets/botao_jogar.png")
botao_sair = PPlay.sprite.Sprite("assets/botao_sair.png")

class Menu(PPlay.scenemanager.Scene):
    def __init__(self):
        super().__init__()
    def loop(self):
        if rato.is_over_object(botao_sair) and rato.button_pressed(1):
            janela.close()
        if rato.is_over_object(botao_jogar) and rato.button_pressed(1):
            PPlay.scenemanager.SceneManager.change_scene(Jogo())            
    def draw(self):
        self.janela.draw_text("Cowboy", janela.width/3*1.2, 100, size= 40)
        self.janela.draw_text("Rush", janela.width/3*1.28, 135, size =40)
        botao_sair.set_position(janela.width/2 - botao_jogar.width/2, 400)
        botao_jogar.set_position(janela.width/2 - botao_jogar.width/2, 300)

        botao_sair.draw()
        botao_sair.update()

        botao_jogar.draw()
        botao_jogar.update()

class Jogo(scenemanager.Scene):
    def __init__(self):
        super().__init__()
    def loop(self):
        pass
    def draw(self):
        pass

PPlay.scenemanager.SceneManager.change_scene(Menu())
while True:

    PPlay.scenemanager.SceneManager.run()
    janela.update()