# If-elif-else

my_age: int = 19
if my_age < 18:
    print("Ты ещё не взрослый")
elif 17 < my_age < 60:
    print("Добро пожаловать в наш клуб :)")
else:
    print("Боюсь! Вы слишком старый")

# Ternar Operator
my_age: int = 14
is_adult: str = "Взрослый" if my_age >= 18 else "Не взрослый"
print(is_adult)  # Взрослый

my_age: int = 19
my_gender: str = "female"
if my_age >= 18 and my_gender == "male":
    print("Взрослый")
elif my_age >= 18 and my_gender == "female":
    print("Взрослая")
else:
    print("В каком роде к вам обращаться?")

# All, Any
my_age: int = 19
my_gender: str = "male"
if all((my_age >= 18, my_gender == "male")):
    print("Взрослый")
elif all((my_age >= 18, my_gender == "female")):
    print("Взрослая")
else:
    print("В каком роде к вам обращаться?")
