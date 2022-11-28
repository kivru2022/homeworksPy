import random

# 1.  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# a = float(input())
# sum = 0


# while a > 0:
#     sum += a % 10
#     a /= 10
#     print(int(sum))
   
    
# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# b = int(input("Ваше число: "))
# res = 1

# for i in range(res,  b + 1):
#     res = res * i
#     print(res)
    


# 3. Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
# a = int(input('Ваше число '))
# lst = []

# for i in range (1, a + 1):
#     lst.append(pow((1 + 1 / i), i))
#     print(lst)
 
# summa = 0
# for element in lst:
#     summa += element
#     print(summa)
    
# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры
# N = int(input('Ваше число  '))
# lst = []
# for i in range(-N, N+1):
#     lst.append(i)        
#     print(lst)

# one_pos = int(input('Позиция 1 '))
# two_pos = int (input('Позиция 2 '))

# proizv = lst[one_pos] * lst[two_pos]
# print(proizv)

# 5. Реализуйте алгоритм перемешивания списка.
lst = [random.randint(0, 10) for i in range(random.randint(4, 10))]
print (lst)
numb = random.randint(0, 10)

for i in range (len(lst)):
    lst[k], lst[i] = lst[i], lst[k]
    numb -= 1
    print(f'Новый {lst}')
