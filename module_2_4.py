# Список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебираем числа из списка numbers
for number in numbers:
    if number < 2:  # Числа меньше 2 не являются простыми
        continue

    is_prime = True  # Предполагаем, что число простое

    # Проверяем делимость числа
    for i in range(2, int(number ** 0.5) + 1):  # Проверяем до корня из числа
        if number % i == 0:  # Если число делится на i
            is_prime = False  # Устанавливаем флаг is_prime в False
            not_primes.append(number)  # Добавляем в список не простых чисел
            break  # Выходим из цикла, так как нашли делитель

    if is_prime:  # Если число простое
        primes.append(number)  # Добавляем в список простых чисел

# Выводим списки на экран
print("Primes:", primes)
print("Not Primes:", not_primes)