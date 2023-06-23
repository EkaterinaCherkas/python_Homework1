# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

i = input("Write three-digit number: ")
sum = int(i[0]) + int(i[1]) + int(i[2])
print(sum) 

# i = int(input("Write three-digit number: "))
# a = int(i/100)
# b = int(i/10%10)
# c = int(i%10)
# print(a, '+' , b , '+', c , '=' , a+b+c)
