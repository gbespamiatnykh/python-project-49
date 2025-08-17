import math
from random import randint

from brain_games.constants import MAX_NUMBER, MIN_NUMBER

MIN_PRIME_NUMBER = 2


def show_description() -> None:
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(number: int) -> bool:
    if number < MIN_PRIME_NUMBER:
        return False
    for divider in range(MIN_PRIME_NUMBER, int(math.sqrt(number)) + 1):
        if number % divider == 0:
            return False
    return True


def generate_question_answer() -> tuple[str, str]:
    question = randint(MIN_NUMBER, MAX_NUMBER)
    answer = "yes" if is_prime(question) else "no"
    return str(question), answer
