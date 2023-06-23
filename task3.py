# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет 
# счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

num = input("Write six-digit number: ")
sum1 = int(num[0]) + int(num[1]) + int(num[2])
sum2 = int(num[3]) + int(num[4]) + int(num[5])
if sum1 == sum2:
    print(num[0] ,"+",num[1], "+" , num[2],"=" , sum1)
    print(num[3] ,"+",num[4], "+" , num[5],"=" , sum2) 
    print("yes")
else:
    print("no")

#Решение 2
num = input("Write six-digit number: ")
if len(num) == 6:
    if(int(num[0]) + int(num[1]) + int(num[2])) == (int(num[3]) + int(num[4]) + int(num[5])):
        print("happy ticket! ")
    else:
        print("error,your ticket not happy")
else:
    print("write correct number, repeat please")

#Решение 3
num = input("Write six-digit number: ")
a = num//100000
b = num//10000%10
c = num//1000%10
d = num%1000//100
e = num%100//10
f = num%10

if a + b + c == d+e+f:
    print("yes")
else:
    print("no")
