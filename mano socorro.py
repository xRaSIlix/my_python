import turtle
import math

num_l = 5
tamanho = 100
angulo = 360 / num_l

def polygon():
    polygon = turtle.Turtle()
    for i in range(num_l):
        polygon.fd(tamanho)
        polygon.lt(angulo)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

circle()
        