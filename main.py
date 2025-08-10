"""
Minigame de matemática onde o jogador
vai ter 3 chances para passar por uma 
série de perguntas.
"""

from time import sleep
from funcoes import verifica_resposta
from funcoes import verifica_acerto
from funcoes import fabrica_nivel
import os

print("~" * 25)
print("  DESAFIO DE MATEMÁTICA")
print("~" * 25)
sleep(2)

acertos = erros = 0
nivel = 1
chances = 3
ganhou = None

while True:
    if chances == 0:
        print("Você esgotou suas chances.")
        ganhou = False
        break
    
    if nivel == 1:
        print(f"Nível {nivel}")
        
        resultado = fabrica_nivel("+")
        
        if resultado:
            acertos += 1
        
        else:
            chances -= 1
            erros += 1
        
        if acertos == 5:
            nivel += 1
            print(f"Nível {nivel}")
            sleep(1.5)
        
        os.system("clear")
    
    if nivel == 2:
        print(f"Nível {nivel}")
        
        resultado = fabrica_nivel("-")
        
        if resultado:
            acertos += 1
        
        else:
            chances -= 1
            erros += 1
        
        if acertos == 10:
            nivel += 1
            print(f"Nível {nivel}")
            sleep(1.5)
        
        os.system("clear")
    
    if nivel == 3:
        print(f"Nível {nivel}")
        
        resultado = fabrica_nivel("*")
        
        if resultado:
            acertos += 1
        
        else:
            chances -= 1
            erros += 1
        
        if acertos == 15:
            ganhou = True
            break
        
        os.system("clear")

if ganhou:
    print("Parabéns, você completou o desafio.")
    print(f"Você acertou {acertos} questões.")
    
    if erros == 1:
        print(f"Errou {erros} questão.")
    
    else:
        if erros == 2:
            print("Com mais um erro teria perdido, foi por pouco.")
        
        print(f"Errou {erros} questões.")
    
    if chances == 1:
        print("Você finalizou com uma chance restante.")
    
    else:
        print(f"Você finalizou com {chances} chances restantes.")
