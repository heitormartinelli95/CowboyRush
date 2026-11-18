from PPlay import scenemanager
import assets
from PPlay.physics import Physics
from PPlay.object_group import ObjectGroup
from PPlay import sprite
from PPlay import mouse
import time
import random


def calc_equacao(x_origem, y_origem):
    rx,ry = mouse.Mouse.get_position(mouse.Mouse)
    if rx == x_origem:
        rx += 1
    a = (ry - y_origem) / (rx - x_origem)
    b = y_origem - a * x_origem
    return a,b

class Tiro(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__("assets/tiro.png")
        self.set_position(x,y)
        self.velocidade_x = 500
        self.a , self.b = calc_equacao(x,y)
    def update(self, dt):
        self.x += self.velocidade_x * dt
        self.y = self.a*self.x+self.b
tiro = ObjectGroup()

class Obstaculo(sprite.Sprite):
    def __init__(self, imagem, x, y, velocidade, tipo):
        super().__init__(imagem)
        self.set_position(x, y)
        self.velocidade = velocidade
        self.tipo = tipo

    def update(self, dt):
        self.x -= self.velocidade * dt
obstaculos = ObjectGroup()

class Jogo(scenemanager.Scene):
    def __init__(self, janela, rato):
        super().__init__()
        self.janela = janela
        self.rato = rato
        self.fundo1 = sprite.Sprite("assets/fundo.png")
        self.fundo2 = sprite.Sprite("assets/fundo.png")
        self.fundo1.set_position(0, 0)
        self.fundo2.set_position(self.fundo1.width, 0)
        self.velocidade_fundo = 100

        for obs in list(obstaculos.get_all()):
            obstaculos.remove(obs)
        for tir in list(tiro.get_all()):
            tiro.remove(tir)

        self.motor = Physics(gravidade=1800)
        assets.cowboy.setup_physics(self.motor)

        cowboy_x = 20
        cowboy_y = self.janela.height - assets.cowboy.height - 50
        self.tiro_y = 0

        assets.cowboy.set_position(cowboy_x, cowboy_y)
        self.cowboy_armado = sprite.Sprite("assets/armado.png")
        self.cowboy_armado.set_position(cowboy_x, cowboy_y)


        assets.chao.set_position(0, cowboy_y + assets.cowboy.height)

        self.lista_solidos = [assets.chao]
        self.cooldown = 0.7
        self.ultimo_tiro=0
        self.ultimo_powerup = 0
        self.powerup_coletado = False
        self.ultimo_spawn = 0
        self.intervalo_spawn = 1.5

        self.vida = 3
        self.score = 0
        self.ponto_base = 15
        self.str_score = ""

    def loop(self):
        from cenas.Menu import Menu
        dt = self.janela.delta_time()
        self.score += dt * self.ponto_base
        self.str_score = str(int(self.score))

        self.fundo1.x -= self.velocidade_fundo * dt
        self.fundo2.x -= self.velocidade_fundo * dt

        if self.fundo1.x <= -self.fundo1.width:
            self.fundo1.x = self.fundo2.x + self.fundo2.width
        if self.fundo2.x <= -self.fundo2.width:
            self.fundo2.x = self.fundo1.x + self.fundo1.width

        if self.janela.keyboard.key_pressed('ESC'):
            scenemanager.SceneManager.change_scene(Menu(self.janela, self.rato))
            return

        if (self.janela.keyboard.key_pressed('SPACE')) and (assets.cowboy.y == self.janela.height - assets.cowboy.height - 50):
            assets.cowboy.pular(2200)

        self.tiro_y = assets.cowboy.y + assets.cowboy.height *0.3

        if time.time() - self.ultimo_spawn > self.intervalo_spawn:
            escolha = random.choices(["cacto", "cacto2", "inimigo", "arma"], weights = [8, 8, 3, 1], k=1)[0]
            obstaculos.add(Obstaculo(f"assets/{escolha}.png", 850, self.janela.height - assets.cowboy.height - 21, 300, escolha))
            self.ultimo_spawn = time.time()
            self.intervalo_spawn = max(0.6, self.intervalo_spawn - 0.02)

        for obs in list(obstaculos.get_all()):
            obs.update(dt)
            if obs.x + obs.width < 0:
                obstaculos.remove(obs)
            if obs.tipo == "inimigo":
                obs.y = assets.cowboy.y
            if assets.cowboy.collided(obs):
                if obs.tipo == "arma":
                    self.powerup_coletado = True
                    self.ultimo_powerup = time.time()
                    obstaculos.remove(obs)
                if obs.tipo != "arma":
                    self.vida -= 1
                    obstaculos.remove(obs)

        if self.vida == 0:
            scenemanager.SceneManager.change_scene(Menu(self.janela, self.rato))
            return

        assets.cowboy.update_physics(self.lista_solidos)

        self.cowboy_armado.set_position(assets.cowboy.x, assets.cowboy.y)

        if abs(self.ultimo_powerup- time.time())>5:
            self.powerup_coletado = False
            self.cooldown = 0.7
        if self.powerup_coletado == True:
            self.cooldown = 0.35

        if self.rato.button_pressed(1) and abs(time.time() - self.ultimo_tiro) > self.cooldown:
            rx,ry = self.rato.get_position()
            if rx> 150:
                tiro.add(Tiro(98,self.tiro_y))
                self.ultimo_tiro = time.time()


        for tir in list(tiro.get_all()):
            tir.update(dt)
            if tir.x>800 or tir.y<0 or tir.y > self.janela.height:
                tiro.remove(tir)
                continue
            for obs in obstaculos.get_all():
                if tir.collided(obs):
                    if obs.tipo == "inimigo" or obs.tipo == "arma":
                        obstaculos.remove(obs)
                        tiro.remove(tir)
                    if obs.tipo != "inimigo" and obs.tipo != "arma":
                        tiro.remove(tir)
                    break

    def draw(self):
            self.fundo1.draw()
            self.fundo2.draw()
            if self.powerup_coletado:
                self.cowboy_armado.draw()
            else:
                assets.cowboy.draw()
            obstaculos.draw()
            tiro.draw()
            self.janela.draw_text(self.str_score, 0, 0, size = 36,color = (0,0,0), bold = True)
            self.janela.draw_text(f"vidas = {str(self.vida)}", self.janela.width - 160, 0, size = 36,color = (0,0,0), bold = True)

