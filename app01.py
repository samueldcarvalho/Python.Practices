from random import random

print("###########################################")
print("Seja muito bem-vindo ao jogo de advinhação!")    
print("###########################################")
print()

chute_usuario = int(input("Chute um número:"))
print("Você chutou: ", chute_usuario)

numero_aleatorio = 3

print("")

if(numero_aleatorio == chute_usuario) : 
    print("Acertou em cheio!!!")
else :
    if(chute_usuario > numero_aleatorio):
        print("O número chutado é maior que o número secreto!")
    else:
        print("Você chutou um número menor que o número secreto!")

print()

