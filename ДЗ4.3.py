#3- Задайте натуральное число N.
#  Напишите программу, которая составит список 
# простых множителей числа N.
#Пример: при N = 12 -> [2, 3]

n = 24
def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans
print(Factor(n))

# n = 12
# i = 2
# while n > 1:
#     while n % i == 0:
#         print(i, end=' ')
#         n //= i
#     i += 1
