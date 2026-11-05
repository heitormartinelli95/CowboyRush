from PPlay import scenemanager
import assets
from PPlay.physics import Physics


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



    def draw(self):
        assets.fundo.draw()
        assets.cowboy.draw()
        assets.inimigo.draw()
        assets.cacto1.draw()
        assets.arma.draw()

    def loop(self):
        from cenas.Menu import Menu

        if self.janela.keyboard.key_pressed('ESC'):
            scenemanager.SceneManager.change_scene(Menu(self.janela, self.rato))

        if (self.janela.keyboard.key_pressed('SPACE')) and (assets.cowboy.y == self.janela.height - assets.cowboy.height - 50):
            assets.cowboy.pular(900)

        assets.cowboy.update_physics(self.lista_solidos)