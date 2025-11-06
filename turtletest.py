import turtle
from turtle import *

color('blue', 'pink') # голубой цвет карандаша, розовый для заливки
begin_fill() # начать заливку
for i in range (4):
    turtle.fd(80) # вперед на 80 пикселей
    turtle.left(90) # повернуть влево на 90 градусов
end_fill() # закончить заливку
input()