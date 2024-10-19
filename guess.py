import random # Модуль, дозволяє створювати випадкові числа

attempts = 0 # Додаємо лічильник спроб

# Загадуємо число від 1 до 100
secret_number = random.randint(1,100)
# print(secret_number)

guess = None # Порожнє значення для старту

while guess != secret_number: # Цикл повтоюється, доки не вгадано число

    attempts += 1

    # Отримуємо введення від користувача
    guess = int(input("Введіть число від 1 до 100: \n"))

    if guess < secret_number:
        print("Загадане число більше!")
    elif guess > secret_number:
        print("Загадане число меньше!")
    else:
        print(f"Вітаю ви вгадали за {attempts} спроб!")
