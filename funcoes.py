
from time import sleep
from random import randint


def verifica_acerto(
    resposta: int, 
    resultado: int
    ) -> bool:
    if resposta == resultado:
        print("Acertou!")
        sleep(1.5)
        return True
        
    else:
        print("Errou")
        sleep(1.5)
        return False


def fabrica_nivel(operador: str) -> bool:
    numero_1 = randint(1, 20)
    numero_2 = randint(1, 20)
    
    while numero_2 == numero_1:
        numero_2 = randint(1, 20)
    
    if operador == "+":
        resultado = numero_1 + numero_2
      
    elif operador == "-":
        resultado = numero_1 - numero_2
    
    elif operador == "*":
        resultado = numero_1 * numero_2
    
    print(f"  {numero_1} {operador} {numero_2}")
        
    while True:
        resposta = input("Digite aqui: ")
        resposta = verifica_resposta(resposta)
            
        if verifica_resposta(resposta):
            break
        
    verificacao_acerto = verifica_acerto(
                            resposta, resultado)
    
    return verificacao_acerto

def verifica_resposta(valor: int) -> int | bool:
    try:
        resposta = int(valor)
        return resposta
            
    except ValueError:
        print("Digite apenas números.")
        return False
