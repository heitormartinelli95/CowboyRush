from PPlay import scenemanager
import assets
from PPlay.physics import Physics
from PPlay.object_group import ObjectGroup
from PPlay import sprite
from PPlay import mouse
import time
import random

from assets import dificuldade


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
    def __init__(self, janela, rato, dificuldade):
        super().__init__()
        self.janela = janela
        self.rato = rato
        self.dificuldade = dificuldade
        self.fundo1 = sprite.Sprite("assets/fundo.png")
        self.fundo2 = sprite.Sprite("assets/fundo.png")
        self.fundo1.set_position(0, 0)
        self.fundo2.set_position(self.fundo1.width, 0)
        self.velocidade_fundo = 100
        self.velocidade_base = 250 + 75 * self.dificuldade

        for obs in list(obstaculos.get_all()):
            obstaculos.remove(obs)
        for tir in list(tiro.get_all()):
            tiro.remove(tir)


        self.motor = Physics(gravidade=1800)
        assets.cowboy.setup_physics(self.motor)
        assets.cowboy.set_total_duration(100000000000000)

        self.vida = 3
        self.coracoes = []
        for i in range(3):
            c = sprite.Sprite("assets/coracoes.png",1)
            c.set_total_duration(100000000000000)
            c.set_curr_frame(0)
            c.set_position(self.janela.width - (c.width + 8) * (i + 1) - 10, 5)
            self.coracoes.append(c)

        cowboy_x = 20
        cowboy_y = self.janela.height - assets.cowboy.height - 50
        self.tiro_y = 0

        self.cowboy_armado = sprite.Sprite("assets/arma.png")
        
        assets.cowboy.set_position(cowboy_x, cowboy_y)
        assets.chao.set_position(0, cowboy_y + assets.cowboy.height)

        self.lista_solidos = [assets.chao]
        self.cooldown = 0.5
        self.ultimo_tiro=0
        self.ultimo_powerup = 0
        self.powerup_coletado = False
        self.ultimo_spawn = 0
        self.intervalo_minimo = 1.5 - 0.25 * self.dificuldade
        self.intervalo_spawn = 2.5


        self.score = 0
        self.ponto_base = 15 * self.dificuldade
        self.str_score = ""

    def loop(self):
        self.cowboy_armado.set_position(assets.cowboy.x+25, assets.cowboy.y+40)
        from cenas.Menu import Menu
        from cenas.rank_escrita import rnk_cria
        dt = self.janela.delta_time()
        self.score += dt * self.ponto_base
        self.str_score = str(int(self.score))

        self.fundo1.x -= (self.velocidade_fundo * dt) * self.dificuldade
        self.fundo2.x -= (self.velocidade_fundo * dt) * self.dificuldade

        if self.fundo1.x <= -self.fundo1.width:
            self.fundo1.x = self.fundo2.x + self.fundo2.width
        if self.fundo2.x <= -self.fundo2.width:
            self.fundo2.x = self.fundo1.x + self.fundo1.width

        if self.janela.keyboard.key_pressed('ESC'):
            scenemanager.SceneManager.change_scene(Menu(self.janela, self.rato))
            return

        if (self.janela.keyboard.key_pressed('SPACE')) and (assets.cowboy.y == self.janela.height - assets.cowboy.height - 50):  
            assets.cowboy.pular(2200)
        if assets.cowboy.y > 400:
            assets.cowboy.set_total_duration(500)
        self.tiro_y = assets.cowboy.y + assets.cowboy.height *0.3

        if time.time() - self.ultimo_spawn > self.intervalo_spawn:
            escolha = random.choices(["cacto", "cacto2", "inimigo", "arma"], weights = [8, 8, 4, 2], k=1)[0]
            obstaculos.add(Obstaculo(f"assets/{escolha}.png", 850, self.janela.height - assets.cowboy.height - 21, (self.velocidade_base + self.score * 0.01), escolha))
            self.ultimo_spawn = time.time()
            self.intervalo_spawn = max(self.intervalo_minimo, self.intervalo_spawn - 0.05)

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
                if obs.tipo != "inimigo" and obs.tipo != "arma":
                    self.vida -= 1
                    obstaculos.remove(obs)
                if obs.tipo == "inimigo":
                    self.vida = 0


        if self.vida == 0:
            scenemanager.SceneManager.change_scene(rnk_cria(int(self.score), self.janela, self.rato))
            return

        assets.cowboy.update_physics(self.lista_solidos)


        if abs(self.ultimo_powerup- time.time())>5:
            self.powerup_coletado = False
            self.cooldown = 0.7 * self.dificuldade
        if self.powerup_coletado == True:
            self.cooldown = 0.25 * self.dificuldade

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
                    if obs.tipo == "inimigo":
                        obstaculos.remove(obs)
                        tiro.remove(tir)
                    if obs.tipo != "inimigo":
                        tiro.remove(tir)
                    break

    def draw(self):
            self.fundo1.draw()
            self.fundo2.draw()
            assets.cowboy.draw()
            if self.powerup_coletado:
                self.cowboy_armado.draw()
            obstaculos.draw()
            tiro.draw()
            for c in self.coracoes[:self.vida]:
                c.draw()
            self.janela.draw_text(self.str_score, 0, 0, size = 36,color = (0,0,0), bold = True)

