a: int = 1

while a < 5:
    print(f"{a} условие верно")
    a = a + 1
    if a == 3:
        break
else:
    print(f"{a} условие неверно")
print("After while")


def newfunc(n):
    def myfunc(x):
        return x + n

    return myfunc


new = newfunc(100)  # new - это функция
print(new(200))
# 300
fun1 = newfunc(444)
for i in range(9):
    print(fun1(i))
