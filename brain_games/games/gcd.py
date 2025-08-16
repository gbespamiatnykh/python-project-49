from random import randint

from brain_games.constants import MAX_NUMBER, MIN_NUMBER


def show_description() -> None:
    print("Find the greatest common divisor of given numbers.")


def calculate_gcd(num1: int, num2: int) -> int:
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def generate_question_answer() -> tuple[str, str]:
    number1, number2 = (
        randint(MIN_NUMBER, MAX_NUMBER),
        randint(MIN_NUMBER, MAX_NUMBER),
    )
    answer = calculate_gcd(number1, number2)
    question = f'{number1} {number2}'
    return question, str(answer)
