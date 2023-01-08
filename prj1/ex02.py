# Tuples
t: tuple = (5, "program", 1 + 3j)
# Мы можем использовать оператор извлечения среза []
# для извлечения элементов, но мы не можем менять их значения:
print("t[1] = ", t[1])
# t[1] = program
print("t[0:3] =", t[0:3])
# t[0:3] = (5, 'program', (1+3j))

# Strings
s1: str = "Простая строка"
s2: str = """многострочная строка"""

# Sets
a: set = {5, 2, 3, 1, 4}
# вывод переменной множества
print(f"{type(a)}a =", a)
# a = {1, 2, 3, 4, 5}

# Dicts
d: dict = {1: "value", "key": 2}
print(type(d))
# <class 'dict'>
d: dict = {1: "value", "key": 2}
print("d[1] =", d[1])
# d[1] = value
print("d['key'] =", d["key"])
# d['key'] = 2
print("d[2] =", d[2])  # Приводит к ошибке

float(5)  # 5.0
int(10.6)  # 10
float("2.5")  # 2.5
str(25)  # '25'
int("1p")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '1p'
set([1, 2, 3])  # {1, 2, 3}
tuple({5, 6, 7})  # (5, 6, 7)
list("hello")  # ['h', 'e', 'l', 'l', 'o']
dict([[1, 2], [3, 4]])  # {1: 2, 3: 4}
dict([(3, 26), (4, 44)])  # {3: 26, 4: 44}
