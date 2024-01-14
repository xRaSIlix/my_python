#Import's

import time

###CONDICIONAIS E RECURSVIDADE

##O operador módulo permite que seja possível verificar se um número é divisível por outro

#Exemplo de código com operador módulo: 👇

def operador_do_modulo():
    num_1 = int(input("Insira número 1: "))
    num_2 = int(input("Insira número 2: "))
    if num_1 % num_2 == 0:
        print(f"{num_1} é divisível por {num_2}")
    else:
        print(f"{num_1} não é divisível por {num_2}")

###EXPREÇÕES BOOLEANAS

##Uma expressão booleana é uma expressão que pode ser verdadeira ou falsa
        
##True e False são valores especiais que pertencem ao tipo bool; (não são strings)

##Segue alguns exemplos dos operadores relacionais:
# x == y (operador de igualdade)
# x!= y (operador de diferença)
# x > y (operador de maior que)
# x < y (operador de menor que)
# x >= y (operador de maior igual que)
# x <= y (operador de menor igual que)

#Exemplo de código com os operadores relacionais:

def operadores_relacionais():
    x = int(input("Insira o valor de x: "))
    y = int(input("Insira o valor de y: "))
    if x == y:
        print("x e y têem o mesmo valor")
    if x > y:
        print("x é maior que y")
    if x < y:
        print("x é menor que y")

###RECURSIVIDADE

def countdown():
    n = 15
    if n > 0:
        print(n)
        for i in range(n - 1):
            time.sleep(1)
            n = (n - 1)
            print(n)
        print("Blastoff!")

operadores_relacionais()