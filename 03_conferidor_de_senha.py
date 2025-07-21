# Faça um programa que leia uma senha. 
# Caso o usuário digite a senha errada, a mensagem  “Senha incorreta. Digite novamente” deve ser mostrada. 
# Porém, se o usuário digitar a senha errada 3 vezes, a seguinte mensagem deve ser mostrada: “Senha bloqueada.” 

senha = 5121999
entrada_senha = int( input("Digite a senha: "))

tentativas = 0

if (senha != entrada_senha):
    print("Senha incorreta. Digite novamente.")
    tentativas += 1
    while (tentativas < 3):
        entrada_senha= int( input("Digite a senha: "))
        if (senha != entrada_senha):
            print("Senha incorreta. Digite novamente.")
            tentativas += 1
        if (tentativas == 3):
            print("Senha bloqueada.")