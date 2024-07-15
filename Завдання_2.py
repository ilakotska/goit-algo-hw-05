import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Використовуємо регулярний вираз для пошуку всіх дійсних чисел, відокремлених пробілами
    pattern = re.compile(r'\b\d+\.\d+\b')
    # Ітеруємося по всіх знайдених збігах у тексті
    for match in pattern.findall(text):
        # Перетворюємо знайдене число на float і повертаємо його як частину генератора
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # Викликаємо функцію для створення генератора чисел та обчислюємо їхню суму
    return sum(func(text))

# Приклад використання функцій
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")
