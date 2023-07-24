## Hi! Here's a more detailed explanation of how this program works. Hope you enjoy it! :D
## Discord: @natham.fr (natham#0347)

## Libraries to get the alphabet on a list, random the rotors letters and colorize the command prompt :')

import string
import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

## Here we create a list with the lowercase alphabet, sort the initial roters configuration and declare some variables. The
## reason why it has both "rotor_initial" and "rotor" it's because if the user wants to decrypt a message, it needs to reset to
## the intial configuration. For this program, modyfing and storing the rotation with one variable wouldn't make it possible to
## return to the initial configuration.

alfabeto = list(string.ascii_lowercase)
rotor_inicial_1 = random.sample(alfabeto, len(alfabeto))
rotor_inicial_2 = random.sample(alfabeto, len(alfabeto))
rotor_inicial_3 = random.sample(alfabeto, len(alfabeto))
rotor_1 = list(rotor_inicial_1)
rotor_2 = list(rotor_inicial_2)
rotor_3 = list(rotor_inicial_3)
print('Configurações iniciais (initial configs):\n')
print('Alfabeto (Alphabet): ', alfabeto) 
print('Rotor 1 configuration: ', rotor_1)
print('Rotor 2 configuration: ', rotor_2)
print('Rotor 3 configuration: ', rotor_3, '\n')
mensagem_cripto = []
mensagem_uncripto = []

## Functions to encrypt and decrypt the message.

## The functions works in such way that it's pretty similar to the real rotors of Enigma. First of all, at least one of them
## rotates when a character of the word is read by the program. When the complete rotation of the first rotor is done, the
## second rotor rotates once. When the complete rotation of the second rotor is done, the third rotor rotates once. In other
## words, to the full cycle be complete and the default config returns, the program must read 26x26x26 characters! For today
## computers that's not a big deal, but it's stiil fun to see. 
## 
## Now about the path traced by the program to encrypt the word, it can be seen below:
##
##        x = index of letter in alphabet                   y = index of letter "a" in second rotor
##             ______________________                            ___________________________
##            |                      |                          |                           |
##       normal letter          first rotor              second rotor                  third rotor           encrypted letter
##                                   |__________________________|                           |_______________________|
##                              a = letter of "x" index in first rotor                b = letter of "y" index in third rotor
##
## The process to decryption is similar, but it's inverted:
##
##         x = index of letter in third motor                   y = index of letter "a" in first rotor
##             ______________________                            ___________________________
##            |                      |                          |                           |
##     encrypted letter         second rotor               first rotor                   alphabet             normal letter
##                                   |__________________________|                           |_______________________|
##                              a = letter of "x" index in second rotor                b = letter of "y" index in alphabet
##
## I think it is pretty interesting and funny, don't you? Eat it, Alan Turing & friends! Anyway, thanks for your guys jobs. 

def digitarPalavraCripto(palavra):
        for n in palavra:
            print('\nRotor 1: ', rotor_1)
            print('Rotor 2: ', rotor_2)
            print('Rotor 3: ', rotor_3, '\n')
            index_alfabeto = alfabeto.index(n)
            primeira_letra_cripto = rotor_1[index_alfabeto]
            index_rotor_2 = rotor_2.index(primeira_letra_cripto)
            letra_cripto_final = rotor_3[index_rotor_2]
            letra_rotada_1 = rotor_1.pop(25)
            rotor_1.insert(0, letra_rotada_1)
            print('- Have you finished a rotor cycle? ', letra_rotada_1 == rotor_inicial_1[0], '\n')
            if letra_rotada_1 == rotor_inicial_1[0]:
                letra_rotada_2 = rotor_2.pop(25)
                rotor_2.insert(0, letra_rotada_2)
                if letra_rotada_2 == rotor_inicial_2[0]:
                    letra_rotada_3 = rotor_3.pop(25)
                    rotor_3.insert(0, letra_rotada_3)
            mensagem_cripto.append(letra_cripto_final)

def digitarPalavraUncripto(palavra):
        for n in palavra:
            print('\nRotor 1: ', rotor_1)
            print('Rotor 2: ', rotor_2)
            print('Rotor 3: ', rotor_3, '\n')
            index_rotor_3 = rotor_3.index(n)
            primeira_letra_uncripto = rotor_2[index_rotor_3]
            index_rotor_1 = rotor_1.index(primeira_letra_uncripto)
            letra_uncripto_final = alfabeto[index_rotor_1]
            mensagem_uncripto.append(letra_uncripto_final)
            letra_rotada_1 = rotor_1.pop(25)
            rotor_1.insert(0, letra_rotada_1)
            print('- Have you finished a rotor cycle? ', letra_rotada_1 == rotor_inicial_1[0], '\n')
            if letra_rotada_1 == rotor_inicial_1[0]:
                letra_rotada_2 = rotor_2.pop(25)
                rotor_2.insert(0, letra_rotada_2)
                if letra_rotada_2 == rotor_inicial_2[0]:
                    letra_rotada_3 = rotor_3.pop(25)
                    rotor_3.insert(0, letra_rotada_3)

## Program loop. The three options are shown here. 

while True:
    opcao = int(input("Insira o número correspondente ao que deseja. Caso deseje encerrar o programa, digite qualquer outro número. (Insert the number related to what you want) \n \n1 - Criptografar mensagem (Encrypt message) \n2 - Descriptografar mensagem (Decrypt message) \n3 - Trocar criptografia (Change cryptography)\n \nResposta: "))
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
        ## Just rebuilding the rotors. 
        rotor_inicial_1 = random.sample(alfabeto, len(alfabeto))
        rotor_inicial_2 = random.sample(alfabeto, len(alfabeto))
        rotor_inicial_3 = random.sample(alfabeto, len(alfabeto))
        rotor_1 = list(rotor_inicial_1)
        rotor_2 = list(rotor_inicial_2)
        rotor_3 = list(rotor_inicial_3)
        print('Rotor 1: ', rotor_1)
        print('Rotor 2: ', rotor_2)
        print('Rotor 3: ', rotor_3)
        print(Fore.GREEN + '\nCriptografia trocada com sucesso! (Cryptography changed!) \n' + Style.RESET_ALL)

    else:
        print("Programa encerrado. (Script finished)")
        Style.RESET_ALL
        break
    
## A nice footer, don't ask me why. :D
