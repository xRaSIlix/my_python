#import's
import turtle

#variáveis
num_l = 5
tamanho = 100
angulo = 360 / num_l

#função
def polygon():
    polygon = turtle.Turtle()
    for i in range(num_l):
        polygon.fd(tamanho)
        polygon.lt(angulo)

polygon()