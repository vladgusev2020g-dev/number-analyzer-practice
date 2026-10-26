# Практическая работа 1. Номер в списке: 7. Вариант задания: 3.
# Проверка характеристик целого числа.

def main():
    # Повторяем ввод, пока пользователь не введёт целое число.
    while True:
        try:
            number = int(input("Введите целое число: "))
            break
        except ValueError:
            print("Ошибка: нужно ввести целое число, например 13, -6 или 0.")

    print(f"\nВаше число: {number}")

    if number > 0:
        print("Знак: положительное")
    elif number < 0:
        print("Знак: отрицательное")
    else:
        print("Знак: ноль")

    if number % 2 == 0:
        print("Чётное: да")
    else:
        print("Чётное: нет")

    if number % 3 == 0:
        print("Делится на 3: да")
    else:
        print("Делится на 3: нет")

    if number % 5 == 0:
        print("Делится на 5: да")
    else:
        print("Делится на 5: нет")

    # Простое число больше 1 и имеет только два натуральных делителя.
    is_prime = number > 1
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print("Простое: да")
    else:
        print("Простое: нет")

    digit_count = len(str(abs(number)))
    print(f"Количество цифр: {digit_count}")


if __name__ == "__main__":
    main()
