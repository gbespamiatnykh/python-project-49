import prompt

ROUND_COUNT = 3


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def start_game(game: callable) -> None:
    name = welcome_user()
    game.show_description()
    for _ in range(ROUND_COUNT):
        question, correct_answer = game.generate_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if correct_answer == user_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'. \n"
                f"Let's try again, {name}!"
            )
            break
    else:
        print(f"Congratulations, {name}!")
