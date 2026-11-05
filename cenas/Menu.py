from PPlay import scenemanager
import assets


class Menu(scenemanager.Scene):
    def __init__(self, janela, rato):
        super().__init__()
        self.janela = janela
        self.rato = rato

    def loop(self):
        from cenas.Jogo import Jogo

        if self.rato.is_over_object(assets.botao_sair) and self.rato.button_pressed(1):
            self.janela.close()
        if self.rato.is_over_object(assets.botao_jogar) and self.rato.button_pressed(1):
            scenemanager.SceneManager.change_scene(Jogo(self.janela, self.rato))

    def draw(self):

        esp = assets.botao_jogar.height + 30

        assets.botao_sair.set_position(assets.botao_jogar.x, assets.botao_jogar.y + 2 * esp)
        assets.botao_jogar.set_position(self.janela.width / 2 - assets.botao_jogar.width / 2, 300)
        assets.botao_dificuldade.set_position(assets.botao_jogar.x, assets.botao_jogar.y + esp)

        titulo_x = self.janela.width / 2 - assets.titulo.width / 2
        titulo_y = 100

        assets.titulo.set_position(titulo_x, titulo_y)

        assets.botao_sair.draw()
        assets.botao_sair.update()
        assets.botao_dificuldade.draw()
        assets.titulo.draw()
        assets.botao_jogar.draw()
        assets.botao_jogar.update()

