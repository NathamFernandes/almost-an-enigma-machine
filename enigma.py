## Hi! Enjoy it :D
## Discord: @natham.fr (natham#0347)

## Libraries to get the alphabet on a list, random the rotors letters and colorize the command prompt :')

import string
import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

## Declaring variables

alfabeto = list(string.ascii_lowercase)
rotor_inicial_1 = random.sample(alfabeto, len(alfabeto))
rotor_inicial_2 = random.sample(alfabeto, len(alfabeto))
rotor_inicial_3 = random.sample(alfabeto, len(alfabeto))
rotor_1 = list(rotor_inicial_1)
rotor_2 = list(rotor_inicial_2)
rotor_3 = list(rotor_inicial_3)
mensagem_cripto = []
mensagem_uncripto = []

## Functions to encrypt and decrypt the message.

def digitarPalavraCripto(palavra):
        for n in palavra:
            index_alfabeto = alfabeto.index(n)
            primeira_letra_cripto = rotor_1[index_alfabeto]
            index_rotor_2 = rotor_2.index(primeira_letra_cripto)
            letra_cripto_final = rotor_3[index_rotor_2]
            mensagem_cripto.append(letra_cripto_final)
            letra_rotada_1 = rotor_1.pop(25)
            rotor_1.insert(0, letra_rotada_1)
            if letra_rotada_1 == rotor_inicial_1[0]:
                letra_rotada_2 = rotor_2.pop(25)
                rotor_2.insert(0, letra_rotada_2)
                if letra_rotada_2 == rotor_inicial_2[0]:
                    letra_rotada_3 = rotor_3.pop(25)
                    rotor_3.insert(0, letra_rotada_3)

def digitarPalavraUncripto(palavra):
        for n in palavra:
            index_rotor_3 = rotor_3.index(n)
            primeira_letra_uncripto = rotor_2[index_rotor_3]
            index_rotor_1 = rotor_1.index(primeira_letra_uncripto)
            letra_uncripto_final = alfabeto[index_rotor_1]
            mensagem_uncripto.append(letra_uncripto_final)
            letra_rotada_1 = rotor_1.pop(25)
            rotor_1.insert(0, letra_rotada_1)
            if letra_rotada_1 == rotor_inicial_1[0]:
                letra_rotada_2 = rotor_2.pop(25)
                rotor_2.insert(0, letra_rotada_2)
                if letra_rotada_2 == rotor_inicial_2[0]:
                    letra_rotada_3 = rotor_3.pop(25)
                    rotor_3.insert(0, letra_rotada_3)

## Program loop. The three options are shown here. 

while True:
    opcao = int(input("Insira o número correspondente ao que deseja. Caso deseje encerrar o programa, digite qualquer outro número. \n \n1 - Criptografar mensagem \n2 - Descriptografar mensagem \n3 - Trocar criptografia \n \nResposta: "))
    rotor_1 = list(rotor_inicial_1)
    rotor_2 = list(rotor_inicial_2)
    rotor_3 = list(rotor_inicial_3)
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
        ## Rebuilding the rotors. 
        rotor_inicial_1 = random.sample(alfabeto, len(alfabeto))
        rotor_inicial_2 = random.sample(alfabeto, len(alfabeto))
        rotor_inicial_3 = random.sample(alfabeto, len(alfabeto))
        rotor_1 = list(rotor_inicial_1)
        rotor_2 = list(rotor_inicial_2)
        rotor_3 = list(rotor_inicial_3)
        print(Fore.GREEN + '\nCriptografia trocada com sucesso! \n' + Style.RESET_ALL)

    else:
        print("Programa encerrado.")
        Style.RESET_ALL
        break
            
