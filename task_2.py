

import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b[-+]?\d+(?:\.\d+)?\b'
    for float_number in re.findall(pattern, text):
        yield float(float_number)

def sum_profit(text: str, operation: Callable[[str], float]) -> float:
    return sum(operation(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
