# If-elif-else

my_age: int = 19
if my_age < 18:
    print("Ты ещё не взрослый")
elif 17 < my_age < 60:
    print("Добро пожаловать в наш клуб :)")
else:
    print("Боюсь! Вы слишком старый")

# Ternar Operator
my_age: int = 19
is_adult: str = "Взрослый" if my_age >= 18 else "Не взрослый"
print(is_adult)  # Взрослый
