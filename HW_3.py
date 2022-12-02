import random 
from random import randint
import math

# 1. Задайте список из нескольких чисел. Напишите программу, которай найдет сумму нечетных елементов

# def sum_nech(lis):
#     sum = 0
#     for i in range(len(lis)):
#         if lst[i] % 2  != 0:
#             sum += lst[i]
#             print(sum)
           
        
            
# lst = [2, 3, 7, 9, 11, 21]
# sum_nech(lst)

# 2. Напишите программу, которая найдет произведение пар чисел списка

# def neib(lst):
#     lst1 = [lst[i] * lst[len(lst)-i-1] for i in range(len(lst) - len(lst)//2)]
#     print(lst1)
                   
# spisok = [1, 2, 9, 7 , 5 , 6]
# neib(spisok)

# 3. Задайте список вещественных чисел. Напишите программу, которая найдет разницу 
# между максимальным  и минимальным значением дробной части

# def func(lst):
#     min_v = lst[0] % 1
#     max_v = lst[0] % 1
#     for i in range(len(lst)):
#         if min_v > lst[i] % 1:
#             min_v = lst[i] % 1
#         if max_v < lst[i] % 1:
#             max_v = lst[i] % 1
#         j = max_v - min_v
#         print(j)
        
# lst2 = [11.20, 1.03, 3.19, 4.21]
# func(lst2)

# 4. Напишите программу перевода десятичного числа в двоичное
# a = int(input("Ваше число: "))

# def func(n):
#     b = '' 
#     while n > 0:
#         b = str(n % 2) + b #чтобы числа просто записывались в строку
#         n //=2
#         print(b)
# func(a)


        
# 5. Задайте число. Составьте список Фибоначчи

# a = int(input("Задайте число:  "))

# def fib_lst(n):
#     x = 1
#     y = 1
#     lst = []
#     i = 0
#     for i in range (2, n):
#         i = x + y
#         x = y
#         y = i
#         lst.append(y)
#         print(lst)
# fib_lst(a)