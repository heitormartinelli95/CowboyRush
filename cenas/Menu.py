from PPlay import scenemanager
import assets


class Menu(scenemanager.Scene):
    def __init__(self, janela, rato):
        super().__init__()
        self.janela = janela
        self.rato = rato
        self.pode_clicar = False

    def loop(self):
        from cenas.Jogo import Jogo
        from cenas.dificuldade import Dif
        from cenas.rank import Rnk
        if not self.pode_clicar:
            self.pode_clicar = True
            return

        if self.rato.is_over_object(assets.sair) and self.rato.button_pressed(1):
            self.janela.close()
        if self.rato.is_over_object(assets.jogar) and self.rato.button_pressed(1):
            self.dificuldade = 1
            scenemanager.SceneManager.change_scene(Jogo(self.janela, self.rato, self.dificuldade))
        if self.rato.is_over_object(assets.dificuldade) and self.rato.button_pressed(1):
             scenemanager.SceneManager.change_scene(Dif(self.janela, self.rato))
        if self.rato.is_over_object(assets.rank) and self.rato.button_pressed(1):
                     scenemanager.SceneManager.change_scene(Rnk(self.janela, self.rato))
                 

    def draw(self):

        esp = assets.jogar.height + 30

        titulo_x = self.janela.width / 2 - assets.titulo.width / 2
        titulo_y = 50
        assets.titulo.set_position(titulo_x, titulo_y)
        assets.sair.set_position(assets.jogar.x, assets.jogar.y + 3 * esp)
        assets.jogar.set_position(self.janela.width / 2 - assets.jogar.width / 2, assets.titulo.y + assets.titulo.height + 10)
        assets.dificuldade.set_position(assets.jogar.x, assets.jogar.y + esp)
        assets.rank.set_position(assets.jogar.x, assets.jogar.y + 2 * esp)





        assets.sair.draw()
        assets.sair.update()
        assets.dificuldade.draw()
        assets.titulo.draw()
        assets.jogar.draw()
        assets.rank.draw()
        assets.jogar.update()

