from os import system

def teste(v="Teste..."):
    print(v)
    
def limpar():
    system("clear")

def pause():
    system("pause")

def espaco(tam=1):
    for i in range(tam):
        print()

def linha(tam):
    for i in range(tam):
        print("-", end="")
    print()

def colorir(texto, cor):
    return f"\033[1;{cor}m{texto}\033[m"
