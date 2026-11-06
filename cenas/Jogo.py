from PPlay import scenemanager
import assets
from PPlay.physics import Physics
from PPlay.object_group import ObjectGroup
from PPlay import sprite
from PPlay import mouse
import time

def calc_equacao():
    rx,ry = mouse.Mouse.get_position(mouse.Mouse)
    a = (ry-433)/(rx-98)
    b = 433 - a*98
    return a,b

class Tiro(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__("assets/tiro.png")
        self.set_position(x, y)
        self.velocidade_x = 0.5 
        self.a , self.b = calc_equacao()
    def update(self):
        self.x += self.velocidade_x
        self.y = self.a*self.x+self.b
tiro = ObjectGroup()

class Jogo(scenemanager.Scene):
    def __init__(self, janela, rato):
        super().__init__()
        self.janela = janela
        self.rato = rato

        self.motor = Physics(gravidade=2500)
        assets.cowboy.setup_physics(self.motor)

        cowboy_x = 20
        cowboy_y = self.janela.height - assets.cowboy.height - 50

        cacto_x = cowboy_x + 500
        cacto_y = cowboy_y

        assets.fundo.set_position(0, 0)
        assets.cowboy.set_position(cowboy_x, cowboy_y)
        assets.inimigo.set_position(cowboy_x + 300, cowboy_y)
        assets.cacto1.set_position(cacto_x, cacto_y)
        assets.arma.set_position(cacto_x, cacto_y - 100)
        assets.chao.set_position(0, cowboy_y + assets.cowboy.height)

        self.lista_solidos = [assets.chao]

        self.cooldown = 0.7
        self.ultimo_tiro=0
        self.ultimo_powerup = 0
        self.powerup_coletado = False

    def loop(self):
        from cenas.Menu import Menu

        if self.janela.keyboard.key_pressed('ESC'):
            scenemanager.SceneManager.change_scene(Menu(self.janela, self.rato))

        if (self.janela.keyboard.key_pressed('SPACE')) and (assets.cowboy.y == self.janela.height - assets.cowboy.height - 50):
            assets.cowboy.pular(900)

        assets.cowboy.update_physics(self.lista_solidos)

        if self.janela.keyboard.key_down("down"):#TODO fazer o powerup ativar quando o player colidir com a arma
            self.powerup_coletado= True
            self.ultimo_powerup = time.time()

        if abs(self.ultimo_powerup- time.time())>5:
            self.powerup_coletado = False
            self.cooldown = 0.7
        if self.powerup_coletado == True:
            self.cooldown = 0.35

        if self.rato.button_pressed(1) and abs(time.time() - self.ultimo_tiro) > self.cooldown:
            rx,ry = self.rato.get_position()
            if rx> 150:
                tiro.add(Tiro(98,433))
                self.ultimo_tiro = time.time()
        
        for tir in tiro.get_all():
            if tir.x>800 or tir.y<0:
                tiro.remove(tir)
    def draw(self):
            assets.fundo.draw()
            assets.cowboy.draw()
            assets.inimigo.draw()
            assets.cacto1.draw()
            assets.arma.draw()
            tiro.draw()
            tiro.update()
