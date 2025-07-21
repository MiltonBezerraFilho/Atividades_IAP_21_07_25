# Elabore um programa que exiba os números de 50 a 10 e a soma dos valores nesse intervalo. 

numero = 50

while (numero > 9):
    print(numero)
    numero -= 1

print("---------------------")

contagem = 10
soma = 0

while (contagem < 51):
    soma += contagem
    contagem += 1
    print(soma)