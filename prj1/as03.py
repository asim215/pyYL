# Задача №3. Секция статьи "Задача №3."
# Написать метод zeros, который принимает на вход целое число (integer)
# и возвращает количество конечных нулей в факториале
# (N! = 1 * 2 * 3 * ... * N) заданного числа:

# Будьте осторожны 1000! имеет 2568 цифр.

# Доп. инфо: http://mathworld.wolfram.com/Factorial.html

# zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

# zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros


import math


def zeros(n):
    fact = math.factorial(n)
    end = False
    z = 0
    fa = fact
    while not end:
        # Check by div
        if fa % 10 == 0:
            fa //= 10
            z += 1
        else:
            end = True
    print(f"Integer {n} with factorial {fact} has {z} trailing zero(s)")
    return z


print(zeros(6))
print(zeros(12))

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
