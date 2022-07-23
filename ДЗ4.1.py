#1- Вычислить число c заданной точностью d.
#  Число Пи не просто обрезать с math.pi,
#  а вычислить, используя формулы: Нилаканта, 
# ряды Тейлора, серию Ньютона или серию Чудновских.
#Пример:
#- при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

from math import log10
def pi_count(d: float) -> float:
    pi = 0
    pi_nach = 1
    k = 0
    while abs(pi_nach - pi) > d:
        pi_nach = pi
        pi += (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6)) / (16**k)
        k += 1
    return round(pi, -int(log10(d)))

try:
    d = float(input("Введите точность 1e-10 до 1e-1: "))
    if (d < 1e-10 or d > 1e-1):
        raise
except:
    print("Неверный ввод")
else:
    print(pi_count(d))

