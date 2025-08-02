import tkinter as tk
import pygame
import os

pygame.init()
pygame.mixer.init()

def tocar_som_mp3(caminho):
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

def tecla_pressionada(event):
    tecla = event.keysym.lower()
    if tecla in botoes_associados and tecla not in teclas_ativas:
        teclas_ativas.add(tecla)
        btn = botoes_associados[tecla]
        btn.config(relief='sunken', bg='d8c2ff')

        if tecla in caminhos_som:
            tocar_som_mp3(caminhos_som[tecla])

def tecla_solta(event):
    tecla = event.keysym.lower()
    if tecla in teclas_ativas:
        teclas_ativas.remove(tecla)
        btn = botoes_associados[tecla]
        btn.config(relief='raised', bg='white')

janela = tk.Tk()
janela.title('Piano Simples')

teclas_ativas = set()
botoes_associados = {}
caminhos_som = {}

# Corrigido com caminhos válidos para os seus arquivos MP3
"""
info_teclas_brancas = [
    {'tecla': ['z'], 'som': 'mp3 Notes/c3.mp3'},#funciona
    {'tecla': ['x'], 'som': 'mp3 Notes/d3.mp3'},
    {'tecla': ['c'], 'som': 'mp3 Notes/e3.mp3'},
    {'tecla': ['v'], 'som': 'mp3 Notes/f-3.mp3'},
    {'tecla': ['b'], 'som': 'mp3 Notes/g-3.mp3'},
    {'tecla': ['n'], 'som': 'mp3 Notes/a3.mp3'},  # corrigido
    {'tecla': ['m'], 'som': 'mp3 Notes/b3.mp3'}#funciona
]
"""

info_teclas_brancas = [
    {'tecla': ['z'], 'som': 'mp3 Notes/c3.mp3'},
    {'tecla': ['x'], 'som': 'mp3 Notes/d3.mp3'},  # <--- sem hífen
    {'tecla': ['c'], 'som': 'mp3 Notes/e4.mp3'},
    {'tecla': ['v'], 'som': 'mp3 Notes/f3.mp3'},
    {'tecla': ['b'], 'som': 'mp3 Notes/g3.mp3'},
    {'tecla': ['n'], 'som': 'mp3 Notes/a3.mp3'},
    {'tecla': ['m'], 'som': 'mp3 Notes/b3.mp3'}
]

print("\nVerificando arquivos...")
for item in info_teclas_brancas:
    caminho = item['som']
    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
    else:
        print(f"✅ OK: {caminho}")


for posicao, item in enumerate(info_teclas_brancas):
    som = item['som']
    botao = tk.Button(janela,
                      font=('Arial', 12),
                      width=5,
                      height=9,
                      background='white',
                      bd=4,
                      relief='raised',
                      anchor=tk.S,
                      command=lambda n=som: tocar_som_mp3(n))
    botao.grid(row=0, column=posicao)
    for t in item['tecla']:
        botoes_associados[t] = botao
        caminhos_som[t] = som

janela.bind_all('<KeyPress>', tecla_pressionada)
janela.bind_all('<KeyRelease>', tecla_solta)

janela.mainloop()
#source venv/bin/activate
