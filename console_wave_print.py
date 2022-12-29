import time
from math import pi, sin
from random import uniform
from typing import Any, Callable, Dict, List


def get_word_position_sin_wave(x: int, period: int) -> float:
    # returns word position in string to be printed as a % of its maximum length
    y_percentage_of_max = ((sin(pi * 2 * x / period) + 1)) / 2

    return y_percentage_of_max


def generate_string(word: str, full_str: List[str], *s_norm: int) -> str:
    full_str = full_str.copy()

    for s in s_norm:
        full_str[s] = word

    return "".join(full_str)


def colorize_str(word: str) -> str:

    r = uniform(0, 0.5)
    g = uniform(0, 0.5)
    b = 1 - (r + g)

    max_value = 400

    r = round(r * max_value)
    g = round(g * max_value)
    b = round(b * max_value)

    return f"\x1b[38;2;{r};{g};{b}m{word}\x1b"


def start_console_printing(
    word: str,
    console_length: int,
    arguments: Dict[str, Any],
    functions: List[Callable[[int, Dict[str, Any]], float]],
) -> None:

    full_str_spaces = [" " for _ in range(console_length + 1)]
    current_loop = 0
    while True:
        current_loop += 1

        word_positions = [func({"x": current_loop, **arguments}) for func in functions]

        current_full_str = generate_string(word, full_str_spaces, *word_positions)

        current_full_str = colorize_str(current_full_str)

        print(current_full_str)

        time.sleep(0.00000001)


def main() -> None:
    console_length = 90
    period = 80
    word = "your word here"

    get_first_word_position = lambda kwargs: round(
        get_word_position_sin_wave(**kwargs) * console_length
    )
    get_second_word_position = lambda kwargs: console_length - round(
        get_word_position_sin_wave(**kwargs) * console_length
    )

    start_console_printing(
        word, # any string
        console_length, # the width of your console terminal
        {"period": period}, # the extra arguments passed to your functions (first one will be the current "x"/"current_loop")
        [get_first_word_position, get_second_word_position], # list of functions that return the "y" based on your arguments, function calculus and current "x"
    )


if __name__ == "__main__":
    main()
