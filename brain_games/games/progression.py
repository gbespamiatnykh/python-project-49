from random import randint

from brain_games.constants import MAX_NUMBER, MIN_NUMBER

MAX_STEP = 10
MAX_PROGRESSION_LENGTH = 10
MIN_PROGRESSION_LENGTH = 5


def show_description() -> None:
    print("What number is missing in the progression?")


def create_progression(start: int, step: int, length: int) -> list:
    progression = []
    for index in range(length):
        currentElement = start + index * step
        progression.append(str(currentElement))
    return progression


def hide_number(progression: list, index: int) -> str:
    progression[index] = '..'
    return ' '.join(progression)


def generate_question_answer() -> tuple[str, str]:
    start, step, length = (
        randint(MIN_NUMBER, MAX_NUMBER),
        randint(MIN_NUMBER, MAX_STEP),
        randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    )
    progression = create_progression(start, step, length)
    hidden_number_index = randint(0, length - 1)
    answer = progression[hidden_number_index]
    question = hide_number(progression, hidden_number_index)
    return question, answer
