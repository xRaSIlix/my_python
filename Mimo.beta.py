###import's
import random
import turtle
import time
import math
###funções
#primeiro código
def primeiro_codigo():
    print("Hello, world!")

#gerador de senha aleatória
def gerador_de_senha():

    print('Olá, eu sou o mimo gerador de senhas.')
    resposta_gerador = input('Deseja prosseguir? ')

    if resposta_gerador in ['sim', 'Sim', 's', 'ss']:
        digitos_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        digito_1 = random.choice(digitos_1)
        digito_2 = random.choice(digitos_1)
        digito_3 = random.choice(digitos_1)
        digito_4 = random.choice(digitos_1)
        digito_5 = random.choice(digitos_1)
        senha_a = (f'{digito_1}{digito_2}{digito_3}{digito_4}{digito_5}')
        print(f'sua senha é: {senha_a}, lembre dela!')

    if resposta_gerador in ['não', 'nao', 'Não', 'Nao', 'n', 'N', 'nn', "Nn"]:
      print('Certo, geração aleatória cancelada.')

#comparador de senhas
def criador_ou_comparador_de_senha():
    print("Aqui você irá criar sua senha")
    senha_b = input("Crie sua senha")

    print("Certo, agora iremos comparar sua senha para ver se está correta.")
    print("coloque a seguir sua senha👇 ")
    senha_comparada = input("senha: ")
    while senha_b != senha_comparada:
        print("epa, tem coisa errrada aí mermão")
        senha_comparada = input("senha: ")
    if senha_b == senha_comparada:
        print("tá bom, pode entrar")

#primeira versão dos dados
def dados_primeira_versao():
    dado = input("dado: ")

    if dado in ['D4', 'd4']:
        dado_d4 = [1, 2, 3, 4]
        resultado_d4 = random.choice(dado_d4)
    if resultado_d4 == 4:
        print(f"você tirou {resultado_d4} no dado, foi crítico!")
    if resultado_d4 == 1:
        print(f"você tirou {resultado_d4} no dado, foi um desastre crítico!")
    elif resultado_d4 != ['1', '4']:
        print(f"você tirou {resultado_d4} no dado")

    #dado de seis lados

    if dado in ['D6', 'd6']:
        dado_d6 = [1, 2, 3, 4, 5, 6]
        resultado_d6 = random.choice(dado_d6)
    if resultado_d6 == 6:
        print(f"você tirou {resultado_d6} no dado, foi crítico!")
    if resultado_d6 == 1:
        print(f"você tirou {resultado_d6} no dado, foi um desastre crítico!")
    elif resultado_d6 != ['1', '6']:
        print(f"você tirou {resultado_d6} no dado")

    #dado de oito lados

    if dado in ['D8', 'd8']:
        dado_d8 = [1, 2, 3, 4, 5, 6, 7, 8]
        resultado_d8 = random.choice(dado_d8)
    if resultado_d8 == 8:
        print(f"você tirou {resultado_d8} no dado, foi crítico!")
    if resultado_d8 == 1:
        print(f"você tirou {resultado_d8} no dado, foi um desastre crítico!")
    elif resultado_d8 != ['1', '8']:
        print(f"você tirou {resultado_d8} no dado")

    #dado de dez lados

    if dado in ['D10', 'd10']:
        dado_d10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        resultado_d10 = random.choice(dado_d10)
    if resultado_d10 == 10:
        print(f"você tirou {resultado_d10} no dado, foi crítico!")
    if resultado_d10 == 1:
        print(f"você tirou {resultado_d10} no dado, foi um desastre crítico!")
    elif resultado_d10 != ['1', '10']:
        print(f"você tirou {resultado_d10} no dado")

    #dado de doze lados

    if dado in ['D12', 'd12']:
        dado_d12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        resultado_d12 = random.choice(dado_d12)
    if resultado_d12 == 12:
        print(f"você tirou {resultado_d12} no dado, foi crítico!")
    if resultado_d12 == 1:
        print(f"você tirou {resultado_d12} no dado, foi um desastre crítico!")
    elif resultado_d12 != ['1', '12']:
        print(f"você tirou {resultado_d12} no dado")

    #dado de vinte lados

    if dado in ['D20', 'd20']:
        dado_d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        resultado_d20 = random.choice(dado_d20)
    if resultado_d20 == 20:
        print(f"você tirou {resultado_d20} no dado, foi crítico!")
    if resultado_d20 == 1:
        print(f"você tirou {resultado_d20} no dado, foi um desastre crítico!")
    elif resultado_d20 != ['1', '20']:
        print(f"você tirou {resultado_d20} no dado")

#dados recentes
def dados_recentes():
    n_d_l = input("qual o numero de lados ")
    la = int(n_d_l)

    lista = list(range(1, la + 1))
    r = random.choice(lista)

    msg = (f"você tirou {r} no dado")
    cmpmt_b = (", foi um desastre crítico!")
    cmpmt_g = (", foi um sucesso crítico!")

    if r == 1:
        print(msg + cmpmt_b)
    elif r == la:
        print(msg + cmpmt_g)
    else:
        print(msg)

#gerador de senha aleatoria
def senha_aleatoria():
    print('Olá, eu sou um código criado pelo Lucas numa tentativa de criar um gerador de senhas aleatórias de cinco dígitos.')
    resposta_gerador = input('Deseja prosseguir? ')

    if resposta_gerador in ['sim', 'Sim', 's', 'ss']:
        digitos_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z']

        digito_1 = random.choice(digitos_1)
        digito_2 = random.choice(digitos_1)
        digito_3 = random.choice(digitos_1)
        digito_4 = random.choice(digitos_1)
        digito_5 = random.choice(digitos_1)

        print(f'a senha gerada é: {digito_1}{digito_2}{digito_3}{digito_4}{digito_5}')

    if resposta_gerador in ['não', 'nao', 'Não', 'Nao', 'n', 'N', 'nn', "Nn"]:
        print('Certo, geração aleatória cancelada.')

#comparador de numeros
def comparador_de_numeros():
    num_input_1 = input("Insira número um.")
    num_input_2 = input("Insira número dois.")

    num_1 = int(num_input_1)
    num_2 = int(num_input_2)

    if num_1 > num_2:
        print(f"O número {num_1} é maior que {num_2}.")
    else:
        print(f"O número {num_2} é maior que {num_1}.")

#calculadora de raiz quadrada
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
#leitor de numero
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

#gerador de polígonos regulares
def poligonos_regulares():
    lados = int(input("Qual o número de lados do seu polígo?"))
    angulo = 360 / lados
    polygon = turtle.Turtle()
    for i in range(lados):
        polygon.fd(100)
        polygon.lt(angulo)
        time.sleep(10)

#poligonos regulares avançados
# Função para calcular a distância até o meio do polígono
def calcular_distancia(lado):
    meio_lado = lado / 2
    angulo_interno_triangulo_div2 = 180 / lado

    # Convertendo para radianos
    angulo_radianos = math.radians(angulo_interno_triangulo_div2)

    # Calculando a distância
    distancia = meio_lado / math.cos(angulo_radianos)
    return distancia

    # Obtendo o número de lados do polígono
    lados = int(input("Qual o número de lados do seu polígono?"))

    # Calculando o ângulo interno do polígono
    angulo = 360 / lados

    # Inicializando a tartaruga
    polygon = turtle.Turtle()

    # Desenhando o polígono
    for i in range(lados):
        polygon.fd(100)
        polygon.lt(angulo)

    # Movendo para o meio do polígono
    polygon.lt(angulo / 2)
    distancia = calcular_distancia(100)
    polygon.fd(distancia)

    # Desenhando linhas até o meio de cada lado
    for i in range(lados):
        polygon.backward(distancia)
        polygon.penup()
        polygon.goto(0, 0)
        polygon.pendown()
        polygon.setheading(angulo * (i + 1) - angulo / 2)
        polygon.forward(distancia)

    # Mantendo a janela aberta
    time.sleep(20)

#diálogo inicial

print("Olá, sou o Mimo, uma junção de todos os mini projetos e códigos do Lucas.")
print("⨀")
print("Você têm algumas opções a seguir:")
print("∘ O meu primeiro código (pc);")
print("∘ O gerador de senha (gs);")
print("∘ O comparador de senha (cs);")
print("∘ A primeira versão do rolador de dados funcional, porém primitiva (dp);")
print("∘ A versão mais recente do rolador de dados (dr)")
print("∘ Um gerador de senha aleatória (sa)")
print("∘ Um comparador de números (cn)")
print("∘ Uma calculadora de raiz quadrada (rq)")
print("∘ Um leitor de números (ln)")
print("∘ Um gerador de polígonos regulares (pr)")
print("∘ O gerador de polígonos avançados (ca)")

#escolha do projeto

projeto = input("Qual será a sua escolha? ")
if projeto == 'pc':
    primeiro_codigo()
if projeto == 'gs':
    gerador_de_senha()
if projeto == 'cs':
    criador_ou_comparador_de_senha()
if projeto == 'dp':
    dados_primeira_versao()
if projeto == 'dr':
    dados_recentes()
if projeto == 'sa':
    senha_aleatoria()
if projeto == 'cn':
    comparador_de_numeros()
if projeto == 'rq':
    calculador_de_raiz_quadrada()
if projeto == 'ln':
    leitor_de_numero()
if projeto == 'pr':
    poligonos_regulares()
if projeto == 'ca':
    calcular_distancia()