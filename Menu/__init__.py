from Functions import *
from chamar import chamar

def titulo(title: str, tam=30):
    linha(tam)
    print(f"{title.center(tam, " ")}") # Centraliza o Título
    linha(tam)

def listarOpcoes(options):
    for i, opt in options.:
        if opt == "Sair":
            print(f"{colorir(i, 31)} - {colorir(opt, 31)}") # Deixar o "Sair" vermelho
            continue
        print(f"{colorir(i, 35)} - {colorir(opt, 32)}") # Deixar as opcoes verdes

def perguntarEscolha(options):
    res = input("Escolha: ")
    if res in 

def menu(title, options):
    limpar()
    titulo(title, len(title) + 20)
    espaco()
    listarOpcoes(options)
    espaco(2)
    res = perguntarEscolha(options)
    chamar(res)