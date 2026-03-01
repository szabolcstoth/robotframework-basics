import random

from robot.api.deco import keyword


@keyword(tags=["random"])
def generate_random_number(minimum: int, maximum: int):
    """Generates a random number between `minimum` and `maximum`.

    Example:
    | ${random_number}= | Generate Random Number | ${0} | ${100} |
    =>
    | ${random_number}= 87
    """
    return random.randint(minimum, maximum)
