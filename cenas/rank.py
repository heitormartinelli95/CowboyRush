import pygame
import PPlay
from PPlay import scenemanager
from cenas.Menu import Menu

    

janela = PPlay.window.Window(800,600,"invasores",True,True)

class Rnk(PPlay.scenemanager.Scene):
    def __init__(self):
        super().__init__()
        self.fundo= ((255,255,255))
        
    def loop(self):
        ler_placar = open("cenas/rankeamento.txt", 'r') 
        janela.draw_text(f'{ler_placar.read()}', janela.width/2-20 , janela.height/2-20, tamanho = 20 ,cor="black")

        if janela.keyboard.key_down("ESC"):
            scenemanager.SceneManager.change_scene(Menu())
