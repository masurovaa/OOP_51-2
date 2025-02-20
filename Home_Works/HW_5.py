# HW 5
def power(x, n):
    result = 1
    while n > 0:
        if n % 2 == 1:  # Если степень нечетная
            result *= x
        x *= x  # Увеличиваем основание в квадрат
        n //= 2  # Деляем степень пополам
    return result

print(power(2, 10))  # 1024
print(power(3, 7))   # 2187