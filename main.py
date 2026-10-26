from math import isqrt


def main():
    while True:
        # Ввод целого числа с обработкой ошибок.
        while True:
            try:
                number = int(input("Введите целое число: "))
                break
            except ValueError:
                print("Ошибка: введите целое число.")

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

        # Проверка простоты.
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

        # Проверка полного квадрата.
        if number < 0:
            print("Полный квадрат: нет")
        else:
            root = isqrt(number)

            if root * root == number:
                print("Полный квадрат: да")
            else:
                print("Полный квадрат: нет")

        # Вопрос о продолжении с проверкой ответа.
        while True:
            answer = input(
                "\nПроверить ещё одно число? (да/нет): "
            ).strip().lower()

            if answer == "да" or answer == "нет":
                break

            print("Введите «да» или «нет».")

        if answer == "нет":
            print("Работа программы завершена.")
            break

        print()


if __name__ == "__main__":
    main()
