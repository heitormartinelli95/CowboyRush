from PPlay import scenemanager


def carregar_rank():
    entradas = []
    try:
        with open("cenas/rankeamento.txt", "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split()
                if len(partes) < 2:
                    continue
                nome = partes[0]
                try:
                    pontos = int(partes[-1])
                except ValueError:
                    continue
                entradas.append({"nome": nome, "pontuacao": pontos})
    except FileNotFoundError:
        pass
    return entradas


class Rnk(scenemanager.Scene):
    def __init__(self, janela, rato):
        super().__init__()
        self.janela = janela
        self.rato = rato

    def loop(self):
        from cenas.Menu import Menu

        if self.janela.keyboard.key_down("ESC"):
            scenemanager.SceneManager.change_scene(Menu(self.janela, self.rato))

    def draw(self):
        j = self.janela
        j.screen.fill((135, 206, 235))

        j.draw_text(
            "TOP 5 - RANK",
            j.width / 2 - 150, 30,
            tamanho=50, cor="YELLOW", fonte="Arial"
        )

        rank = carregar_rank()
        rank.sort(key=lambda e: e["pontuacao"], reverse=True)
        top5 = rank[:5]

        # cabeçalho
        j.draw_text("POS",    135, 150, tamanho=35, cor="BLACK")
        j.draw_text("NOME",   300, 150, tamanho=35, cor="BLACK")
        j.draw_text("PONTOS", 610, 150, tamanho=35, cor="BLACK")

        if not top5:
            j.draw_text(
                "Nenhuma pontuacao registrada ainda...",
                j.width / 2 - 350, j.height / 2,
                tamanho=35, cor="GRAY"
            )
        else:
            for i, e in enumerate(top5):
                y = 220 + i * 60
                cor = "GOLD" if i == 0 else "BLACK"
                j.draw_text(f"{i + 1}º",              150, y, tamanho=35, cor=cor)
                j.draw_text(e["nome"],                300, y, tamanho=35, cor=cor)
                j.draw_text(str(e["pontuacao"]),      650, y, tamanho=35, cor=cor)