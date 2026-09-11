import pygame
import PPlay
from PPlay import scenemanager

janela = PPlay.window.Window(800, 600, "cowboy rush", True, False)
janela.set_background_color((135, 206, 235))

rato = PPlay.mouse.Mouse()

titulo = PPlay.gameimage.GameImage("assets/titulo.png")
botao_jogar = PPlay.sprite.Sprite("assets/jogar.png")
botao_sair = PPlay.sprite.Sprite("assets/sair.png")
botao_dificuldade = PPlay.sprite.Sprite("assets/dificuldade.png")

cowboy = PPlay.sprite.Sprite("assets/cowboy.png")
inimigo = PPlay.sprite.Sprite("assets/inimigo.png")
arma = PPlay.sprite.Sprite("assets/arma.png")
fundo = PPlay.gameimage.GameImage("assets/fundo.png")
cacto1 = PPlay.sprite.Sprite("assets/cacto.png")
cacto2 = PPlay.sprite.Sprite("assets/cacto.png")


class Menu(PPlay.scenemanager.Scene):
    def __init__(self):
        super().__init__()
    def loop(self):
        if rato.is_over_object(botao_sair) and rato.button_pressed(1):
            janela.close()
        if rato.is_over_object(botao_jogar) and rato.button_pressed(1):
            PPlay.scenemanager.SceneManager.change_scene(Jogo())            
    def draw(self):

        esp = botao_jogar.height + 30

        botao_sair.set_position(botao_jogar.x, botao_jogar.y + 2*esp)
        botao_jogar.set_position(janela.width/2 - botao_jogar.width/2, 300)
        botao_dificuldade.set_position(botao_jogar.x, botao_jogar.y + esp)

        titulo_x = janela.width/2 - titulo.width/2
        titulo_y = 100

        titulo.set_position(titulo_x, titulo_y )

        botao_sair.draw()
        botao_sair.update()
        botao_dificuldade.draw()

        titulo.draw()
        botao_jogar.draw()
        botao_jogar.update()

class Jogo(scenemanager.Scene):
    def __init__(self):
        super().__init__()
    def loop(self):
        if janela.keyboard.key_pressed('ESC'):
            PPlay.scenemanager.SceneManager.change_scene(Menu())


    def draw(self):
        cowboy_x = 20
        cowboy_y = janela.height - cowboy.height - 50

        cacto_x = cowboy_x + 500
        cacto_y = cowboy_y

        fundo.set_position(0,0)
        cowboy.set_position(cowboy_x, cowboy_y)
        inimigo.set_position(cowboy_x + 300, cowboy_y)
        cacto1.set_position(cacto_x, cacto_y)
        arma.set_position(cacto_x, cacto_y - 100)


        fundo.draw()
        cowboy.draw()
        inimigo.draw()
        cacto1.draw()
        arma.draw()



PPlay.scenemanager.SceneManager.change_scene(Menu())
while True:

    PPlay.scenemanager.SceneManager.run()
    janela.update()