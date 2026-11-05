import PPlay
import assets
from PPlay import scenemanager
from cenas.Menu import Menu

janela = PPlay.window.Window(800, 600, "cowboy rush", True, False)
janela.set_background_color((135, 206, 235))
rato = PPlay.mouse.Mouse()

assets.carregar()

from cenas.Menu import Menu
PPlay.scenemanager.SceneManager.change_scene(Menu(janela, rato))

while True:

    PPlay.scenemanager.SceneManager.run()
    janela.update()