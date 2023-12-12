def soma():
    x = float(input("Primeiro numero:\n"))
    y = float(input("Segundo numero:\n"))
    soma = x + y
    print("Soma:", soma)


def subtracao():
    x = float(input("Primeiro numero:\n"))
    y = float(input("Segundo numero:\n"))
    subtracao = x - y
    print("Subtração:", subtracao)


def divisao():
    x = float(input("Primeiro numero:\n"))
    y = float(input("Segundo numero:\n"))
    divisao = x / y
    print("Divisão:", divisao)


def multiplicacao():
    x = float(input("Primeiro numero:\n"))
    y = float(input("Segundo numero:\n"))
    multiplicacao = x * y
    print("Multplicação:", multiplicacao)

print("****** Calculadora ******\n")
opcao = 1
while opcao:
    print("0. Sair")
    print("1.Somar")
    print("2.Subtrair")
    print("3.Multiplicação")
    print("4.Divisão")

    opcao = int(input("Digite sua opção?\n"))

    if (opcao == 1):
        soma()
    if(opcao == 2):
        subtracao()
    if (opcao == 3):
        multiplicacao()
    if (opcao == 4):
        divisao()