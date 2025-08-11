from random import randint

import prompt

MIN_NUMBER = 1
MAX_NUMBER = 100
ROUND_COUNT = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def is_even(number):
    return number % 2 == 0


def get_question():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    print(f"Question: {question}")
    return question


def get_correct_answer(question):
    correct_answer = "yes" if is_even(question) else "no"
    return correct_answer


def start_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(ROUND_COUNT):
        question = get_question()
        user_answer = prompt.string("Your answer: ")
        correct_answer = get_correct_answer(question)
        if correct_answer == user_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. \n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
