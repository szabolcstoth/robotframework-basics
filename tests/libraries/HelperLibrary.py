from robot.api.deco import keyword
import random


@keyword(tags=['random'])
def generate_random_number(min: int, max: int):
    """Generates a random number between `min` and `max`.

    Example:
    | ${random_number}= | Generate Random Number | ${0} | ${100} |
    =>
    | ${random_number}= 87
    """
    return random.randint(min, max)
