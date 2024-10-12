import random # Модуль, дозволяє створювати випадкові числа

# Загадуємо число від 1 до 100
secret_number = random.randint(1,100)
# print(secret_number)

# Отримуємо введення від користувача
guess = int(input("Введіть число від 1 до 100: \n"))

if guess < secret_number:
    print("Загадане число більше!")
elif guess > secret_number:
    print("Загадане число меньше!")
else:
    print("Вітаю ви виграли!")
