import PPlay
from PPlay import scenemanager


def sort_mult(lista1, lista2):
    n = len(lista1)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista1[j + 1] > lista1[j]:
                lista1[j], lista1[j + 1] = lista1[j + 1], lista1[j]
                lista2[j], lista2[j + 1] = lista2[j + 1], lista2[j]
    return lista1, lista2


def sort_arq(arquivo):
    nomes, pontos = [], []
    with open(arquivo, "r") as ler_arq:
        for linha in ler_arq:
            partes = linha.split()
            if len(partes) >= 2:
                nomes.append(partes[0])
                try:
                    pontos.append(int(partes[-1]))
                except ValueError:
                    pass
    pontos_sort, nomes_sort = sort_mult(pontos, nomes)
    with open(arquivo, "w") as escrever_arq:
        for g in range(min(5, len(nomes_sort))):
            escrever_arq.write(f"{nomes_sort[g]} {pontos_sort[g]}\n")


class rnk_cria(PPlay.scenemanager.Scene):
    def __init__(self, pontuacao, janela, rato):
        super().__init__()
        self.pontuacao = pontuacao
        self.janela = janela
        self.rato = rato
        self.fundo = (255, 255, 255)
        self.nome = None
        self.finalizado = False
        sort_arq("cenas/rankeamento.txt")

    def loop(self):
        from cenas.Menu import Menu  # import local, evita ciclo

        if not self.finalizado:
            self.nome = input("me diga seu nome: ")
            with open("cenas/rankeamento.txt", "a") as add:
                add.write(f"{self.nome} {self.pontuacao}\n")
            sort_arq("cenas/rankeamento.txt")
            self.finalizado = True

        scenemanager.SceneManager.change_scene(Menu(self.janela, self.rato))

    def draw(self):
        self.janela.draw_text(
            "escreva seu nome no terminal",
            self.janela.width / 3,
            self.janela.height / 2,
            size=20,
            color=(0, 0, 0),
        )
        self.janela.draw_text(
            "PERDEU COWBOY",
            self.janela.width / 5 - 25,
            50,
            size = 80,
            color = "BLACK"
        )