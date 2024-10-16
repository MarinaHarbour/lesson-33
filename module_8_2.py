def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in numbers:
            if isinstance(i, int):
                result += i
            else:
                incorrect_data += 1
                print(f"Некорректный тип данных для подсчёта суммы - {i}")

    except TypeError as exc:
        incorrect_data += 1
        print(f"Некорректный тип данных для подсчёта суммы {incorrect_data}")

    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError("В numbers записан некорректный тип данных.")

        collection = personal_sum(numbers)
        total_sum = collection[0]
        total_count = len(numbers) - collection[1]

        if total_count == 0:
            return 0

        arithmetic_mean = total_sum / total_count
        return arithmetic_mean

    except ZeroDivisionError as exc:
        return 0
    except TypeError as exc:
        print(exc)
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
