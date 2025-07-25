# Escreva um programa para determinar o número de algarismos de um número inteiro positivo dado.

numero = int( input("Insira um número inteiro e positivo: "))
algarismos = 1

if (numero > -1 and numero < 10):
    print(f'O número de algarismos é {algarismos}.')
else:
    while (numero / 10 >= 1):
        algarismos += 1
        numero = numero / 10
    print(f'O número de algarismos é {algarismos}.')
