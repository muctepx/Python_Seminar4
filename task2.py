# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

from os import system
system("cls")
print("Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")
def Simple_mplication(n:int, uniq: bool = False):

    i = 2
    mass = []
    while n != 1:
        while n % i == 0:
            mass.append(i)
            n = n // i
        i+=1
    if uniq:
        return list(set(mass)) 
    else:
        return Simple_mplication
a = int(input("Введите число: "))
print(f"Простые делители числа: {Simple_mplication(a, True)}")