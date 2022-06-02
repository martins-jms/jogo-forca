import os     

import random

nome = input ('Digite seu nome:') 
print (f'\nOlá seja bem vindo {nome} ! Vamos jogar?')
input ('\nPressione enter para iniciar')
os.system ('cls')

lista_de_palavras = ['maria', 'antonio', 'jose', 'carlos', 'paulo', 'drusyla', 'thomas', 'pedro', 'aparecido', 'flavia', 'matheus']    
palavra_selecionada = random.choice(lista_de_palavras).upper()  
tamanho_palavra = len(palavra_selecionada)      
palavra_codificada = ['_'] * tamanho_palavra      
quantidade_de_erros = 0      

while '_' in palavra_codificada and quantidade_de_erros <6:     
    print (f'\nSua palavra tem {tamanho_palavra} letras')       
    print (f'Erros: {quantidade_de_erros} de 6')
    for letra in palavra_codificada:
        print (letra, end = ' ' )
    print ()

    letra_escolhida = input ('Digite uma letra:').upper()
    acertou = False
    for i in range(len(palavra_selecionada)):
        if letra_escolhida == palavra_selecionada [i]:
            palavra_codificada [i] = letra_escolhida
            acertou = True 

    if acertou == True:
        print ('Parabéns, acertou.')
    else: 
        print('Errou, essa letra não existe na palavra.')
        quantidade_de_erros = quantidade_de_erros + 1

if quantidade_de_erros == 6:
    print ('QTA, VOCÊ PERDEU.')
else: print ("PARABÉNS! VOCÊ GANHOU")

print (f'A palava correta era: {palavra_selecionada}')




    




