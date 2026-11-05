import os
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

print("ASSETS_DIR:", ASSETS_DIR)
print()

# --- teste 1: arquivo legível? ---
for f in sorted(os.listdir(ASSETS_DIR)):
    caminho = os.path.join(ASSETS_DIR, f)
    try:
        with open(caminho, "rb") as fh:
            head = fh.read(12)
        print(f"{f!r:30} legível, {os.path.getsize(caminho):>8} bytes, assinatura={head[:8]!r}")
    except Exception as e:
        print(f"{f!r:30} ERRO: {e}")
print()

# --- teste 2: pygame carrega SEM display? ---
pygame.init()
caminho = os.path.join(ASSETS_DIR, "titulo.png")
try:
    surf = pygame.image.load(caminho)
    print("pygame.image.load (sem display) OK, tamanho:", surf.get_size())
except Exception as e:
    print("pygame.image.load (sem display) FALHOU:", repr(e))

# --- teste 3: pygame carrega COM display + convert_alpha? ---
pygame.display.set_mode((1, 1))
try:
    surf = pygame.image.load(caminho).convert_alpha()
    print("pygame.image.load + convert_alpha (com display) OK, tamanho:", surf.get_size())
except Exception as e:
    print("pygame.image.load + convert_alpha (com display) FALHOU:", repr(e))