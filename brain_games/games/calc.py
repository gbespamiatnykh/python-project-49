from random import choice, randint

from brain_games.scripts.constants import MATH_SIGNS, MAX_NUMBER, MIN_NUMBER


def show_description() -> None:
    print("What is the result of the expression?")


def calculate_expression(
    left_operand: int, right_operand: int, operator: str
) -> int:
    match operator:
        case "+":
            return left_operand + right_operand
        case "-":
            return left_operand - right_operand
        case "*":
            return left_operand * right_operand


def generate_question_answer() -> tuple[str, str]:
    left_operand, right_operand = (
        randint(MIN_NUMBER, MAX_NUMBER),
        randint(MIN_NUMBER, MAX_NUMBER),
    )
    math_sign = choice(MATH_SIGNS)
    question = f"{left_operand} {math_sign} {right_operand}"
    answer = calculate_expression(left_operand, right_operand, math_sign)
    return question, str(answer)
