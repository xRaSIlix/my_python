import math

def comparador_de_numeros():
    num_input_1 = input("Insira número um.")
    num_input_2 = input("Insira número dois.")

    num_1 = int(num_input_1)
    num_2 = int(num_input_2)

    if num_1 > num_2:
        print(f"O número {num_1} é maior que {num_2}.")
    else:
        print(f"O número {num_2} é maior que {num_1}.")

def calculador_de_raiz_quadrada():
    num_input = input("Qual será o número utilizado para calcular a raiz quadrada?")
    num = int(num_input)
    if num > 0:
        num_r = num**(1/2)
        num_f = "{:.2f}".format(num_r)
        print(num_f)
    if num < 0:
        print("inválido, tente novamente.") 
        calculador_de_raiz_quadrada()
    elif num == 0:
        print("o número não pode ser igual a zero")
        calculador_de_raiz_quadrada()

def leitor_de_numero():
    num_r = input("Insira um número real.")
    num_r = int(num_r)
    if num_r > 0:
        raiz = int(num_r**(1/2))
        raiz_f = "{:.2f}".format(raiz)
        print(raiz_f)
    else:
        potencia = num_r**2
        print(potencia)

calculador_de_raiz_quadrada()