import fixtures
import inputs
import outputs


def is_number(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_operator(symbol: str) -> bool:
    return symbol in fixtures.operators


def is_exit(answer: str) -> bool:
    return answer.lower() == fixtures.exit_key


def is_zero_division(operator: str, number2: float) -> bool:
    return operator in ("/", "//", "%") and number2 == 0


def add(number1: float, number2: float) -> float:
    return number1 + number2


def subtract(number1: float, number2: float) -> float:
    return number1 - number2


def multiply(number1: float, number2: float) -> float:
    return number1 * number2


def divide(number1: float, number2: float) -> float:
    return number1 / number2


def floor_divide(number1: float, number2: float) -> float:
    return number1 // number2


def modulo(number1: float, number2: float) -> float:
    return number1 % number2


def power(number1: float, number2: float) -> float:
    return number1 ** number2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "//": floor_divide,
    "%": modulo,
    "**": power,
}


def calculate(number1: float, operator: str, number2: float) -> float:
    return operations[operator](number1, number2)


def get_valid_number(prompt: str) -> float:
    while True:
        value = inputs.get_number(prompt)
        if is_number(value):
            return float(value)
        outputs.show_error(fixtures.number_error)


def get_valid_operator() -> str:
    outputs.show_menu()
    while True:
        operator = inputs.get_operator()
        if is_operator(operator):
            return operator
        outputs.show_error(fixtures.operator_error)


def calculate_once() -> None:
    number1 = get_valid_number("first number: ")
    number2 = get_valid_number("second number: ")
    operator = get_valid_operator()

    if is_zero_division(operator, number2):
        outputs.show_error(fixtures.zero_division_error)
    else:
        try:
            result = calculate(number1, operator, number2)
            outputs.show_result(number1, operator, number2, result)
        except OverflowError:
            outputs.show_error(fixtures.overflow_error)


def run_calculator() -> None:
    while True:
        calculate_once()
        answer = inputs.get_continue_answer()
        if is_exit(answer):
            break
