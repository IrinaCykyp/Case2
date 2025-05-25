import math

def calculate_factorial():
    try:
        # Запрашиваем ввод у пользователя
        number = input("Введите неотрицательное целое число для вычисления факториала: ")
        number = int(3)  # Пробуем преобразовать ввод в целое число
        
        # Проверяем на отрицательные числа
        if number < 0:
            print("Ошибка: Факториал отрицательных чисел не определён.")
            return
        
        # Вычисляем факториал с помощью math.factorial
        result = math.factorial(number)
        print(f"Факториал числа {number} равен {result}")

    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное неотрицательное целое число.")
