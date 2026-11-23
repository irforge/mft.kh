def get_text(prompt) -> str:
    return input(prompt).strip()


def get_number(prompt: str = "number: ") -> str:
    return get_text(prompt)


def get_operator(prompt: str = "operator: ") -> str:
    return get_text(prompt)


def get_continue_answer() -> str:
    return get_text("\nenter for a new calculation or X to exit: ")
