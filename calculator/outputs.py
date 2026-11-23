import fixtures


def show_message(value) -> None:
    print(value)


def show_error(message) -> None:
    show_message(f"error: {message}")


def show_menu() -> None:
    show_message(fixtures.menu)


def number_to_text(number) -> str:
    if number.is_integer():
        return str(int(number))
    return str(number)


def show_result(number1, operator, number2, result) -> None:
    first = number_to_text(number1)
    second = number_to_text(number2)
    answer = number_to_text(result)
    show_message(f"{first} {operator} {second} = {answer}")
