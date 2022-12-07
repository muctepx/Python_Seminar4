# 1'. Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415

from os import system
system("cls")
print("Вычислить число Пи c заданной точностью d")
import math

def fixedNum(f: float, n=0):
    a, b = str(f).split('.')
    return '{}.{}{}'.format(a, b[:n], '0'*(n-len(b)))

d = int(input('Задайте точность числа pi: '))
print(f'Округленное число pi: {fixedNum(math.pi, d)}')