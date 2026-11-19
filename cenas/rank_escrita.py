import pygame
import PPlay
from cenas.Menu import Menu
from PPlay import scenemanager


janela = PPlay.window.Window(800,600,"",True,True)
def sort_mult(lista1,lista2):
    n = len(lista1)
    for i in range(n-1):
        for j in range(n-i-1):
            if lista1[j+1] > lista1[j]:
                lista1[j], lista1[j+1] = lista1[j+1], lista1[j]
                lista2[j],lista2[j+1] = lista2[j+1], lista2[j]
    return lista1,lista2
def sort_arq(arquivo):
    nomes = []
    pontos = []
    with open(arquivo , "r+" ) as ler_arq:
        linhas = ler_arq.readlines()
        for i in range (len(linhas)):
            separacao = linhas[i].split()
            nomes.append(separacao[0])
            pontos.append(int(separacao[-1]))
        ler_arq.truncate(0)
    ler_arq.close()
    pontos_sort , nomes_sort = sort_mult(pontos,nomes)
    with open(arquivo, "a") as escrever_arq:
        if len(nomes_sort) <= 5:
            for g in range (len(nomes_sort)):
                escrever_arq.writelines(f'{nomes_sort[g]} {pontos_sort[g]}\n')
        else:
            for g in range (5):
                escrever_arq.writelines(f'{nomes_sort[g]} {pontos_sort[g]}\n')
    escrever_arq.close()

class rnk_cria(PPlay.scenemanager.Scene):
    def __init__(self,pontuacao, janela, rato):
        super().__init__()
        self.pontuacao = pontuacao
        self. janela = janela
        self.rato = rato
        self.fundo = (255, 255, 255)
        self.lista1 = []
        self.lista2 = []
        self.nome = ''
        sort_arq("cenas/rankeamento.txt") 
    def loop(self):
        if self.nome == '':
            self.nome = input('me diga seu nome ')
        with open('cenas/rankeamento.txt', "a") as add_pontos:
            add_pontos.writelines(f'{self.nome} {self.pontuacao}')
            add_pontos.close()
        sort_arq("cenas/rankeamento.txt")
        scenemanager.SceneManager.change_scene(Menu(self.janela, self.rato))
    def draw(self):
             janela.draw_text('escreva seu nome no terminal', janela.width/3, janela.height/2, size=20, color="white")