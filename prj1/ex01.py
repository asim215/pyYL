a: int = 5
print(a, "is of type", type(a))
# 5 is of type <class 'int'>
b: float = 2.0
print(b, "is of type", type(b))
# 2.0 is of type <class 'float'>
c: complex = 1 + 2j
print(c, "is complex number?", isinstance(1 + 2j, complex))
# (1+2j) is complex number? True
# d: int = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# print(f"Very long number: {d+1}")

# Lists
a: list = [1, 2.2, "python"]

a: list = [5, 10, 15, 20, 25, 30, 35, 40]
print("a[2] =", a[2])
# a[2] = 15
print("a[0:3] =", a[0:3])
# a[0:3] = [5, 10, 15]
print("a[5:] =", a[5:])
# a[5:] = [30, 35, 40]

a: list = [1, 2, 3]
a[2] = 4
print(a)
# [1, 2, 4]
