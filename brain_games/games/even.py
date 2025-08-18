from random import randint

from brain_games.scripts.constants import MAX_NUMBER, MIN_NUMBER


def show_description() -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number: int) -> bool:
    return number % 2 == 0


def generate_question_answer() -> tuple[str, str]:
    question = randint(MIN_NUMBER, MAX_NUMBER)
    answer = "yes" if is_even(question) else "no"
    return str(question), answer
