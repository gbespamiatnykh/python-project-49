import math
from random import randint

from brain_games.constants import MAX_NUMBER, MIN_NUMBER


def show_description() -> None:
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(number) -> bool:
    if number < 2:
        return False
    for divider in range(2, int(math.sqrt(number)) + 1):
        if number % divider == 0:
            return False
    return True


def generate_question_answer() -> tuple[str, str]:
    question = randint(MIN_NUMBER, MAX_NUMBER)
    answer = "yes" if is_prime(question) else "no"
    return str(question), answer
