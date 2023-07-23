import string
import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

alfabeto = list(string.ascii_lowercase)
rotor_inicial = random.sample(alfabeto, len(alfabeto))
rotor = list(rotor_inicial)
mensagem_cripto = []
mensagem_uncripto = []

def digitarPalavraCripto(palavra):
        for n in palavra:
            index = alfabeto.index(n)
            letra_cripto = rotor[index]
            mensagem_cripto.append(letra_cripto)
            letra_rotada = rotor.pop(25)
            rotor.insert(0, letra_rotada)

def digitarPalavraUncripto(palavra):
        for n in palavra:
            index = rotor.index(n)
            letra_uncripto = alfabeto[index]
            mensagem_uncripto.append(letra_uncripto)
            letra_rotada = rotor.pop(25)
            rotor.insert(0, letra_rotada)

while True:
    opcao = int(input("Insira o número correspondente ao que deseja. Caso deseje encerrar o programa, digite qualquer outro número. \n \n1 - Criptografar mensagem \n2 - Descriptografar mensagem \n3 - Trocar criptografia \n \nResposta: "))
    rotor = list(rotor_inicial)
    mensagem_cripto = []
    mensagem_uncripto = []
    
    if opcao == 1:
        digitarPalavraCripto(str(input("\nDigite a palavra a ser criptografada: ")))
        mensagem = ''.join(mensagem_cripto)
        print('Mensagem criptografada:', Fore.CYAN + mensagem + Style.RESET_ALL, '\n')

    elif opcao == 2:
        digitarPalavraUncripto(str(input("\nDigite a palavra a ser descriptografada: ")))
        mensagem = ''.join(mensagem_uncripto)
        print('Mensagem descriptografada:', Fore.CYAN + mensagem + Style.RESET_ALL, '\n')

    elif opcao == 3:
        rotor_inicial = random.sample(alfabeto, len(alfabeto))
        rotor = list(rotor_inicial)
        print(Fore.GREEN + '\nCriptografia trocada com sucesso! \n' + Style.RESET_ALL)

    else:
        print("Programa encerrado.")
        Style.RESET_ALL
        break
    














