'''
Crie um programa para gerenciar uma conta bancária, apresentando o seguinte menu para 
o usuário: 
<1> Depositar 
<2> Sacar 
<3> Consultar saldo 
<4> Sair 
Digite o valor da opção:  
O menu deve ser exibido repetidamente até que o usuário digite 4, que é o valor da opção 
para sair do programa. Caso o usuário tente sacar um valor maior do que o saldo atual da 
conta, uma mensagem deve informá-lo que ele não possui saldo suficiente para a 
operação.
'''

saldo = 10000

while True:

    entrada = int( input("<1> Depositar \n<2> Sacar \n<3> Consultar saldo \n<4> Sair \nDigite o valor da opção: "))
    if (entrada == 1):
        depositar = float( input("Digite quanto deve depositar: "))
        saldo = depositar + saldo
    elif (entrada == 2):
        sacar = float( input("Digite quanto quer sacar: "))
        if (sacar <= saldo):
            saldo = saldo - sacar
        else:
            print("Saldo insuficiente.")
    elif(entrada == 3):
        print(f'Seu saldo é R${saldo}')
    elif(entrada == 4):
        break
    else:
        print("Valor inválido")