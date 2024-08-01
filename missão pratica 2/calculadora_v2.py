saida = ""


def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if (a == 0 or b == 0):
        print("Não é possivel realizar a divisão por 0")
    else:
        return a / b


def calculadora(x, y, mat):
    if (mat == "+" or mat == "adição" or mat == "mais"):
        resultado = adicao(x, y)
    elif (mat == "-" or mat == "subtração" or mat == "menos"):
        resultado = subtracao(x, y)
    elif (mat == "*" or mat == "multiplicação" or mat == "vezes"):
        resultado = multiplicacao(x, y)
    elif (mat == "/" or mat == "divisão" or mat == "dividir"):
        resultado = divisao(x, y)
    else:
        print("não foi possivel realizar a operação")
    return resultado


while saida.lower() != "n":
    n1 = float(input("insira o primeiro numero"))
    n2 = float(input("insira o segundo numero"))
    op = input("insira o nome ou simbolo da operação matematica")
    resultado = calculadora(n1, n2, op)
    print(f"resultado da operação {resultado}")
    saida = input("deseja continuar com outra operação? S/N")
    if(saida.lower() == "n"):
        print("operação foi encerrada")

