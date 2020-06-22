from robot.api.deco import keyword
import random


@keyword(tags=['random'], types={'min': int, 'max': int})
def generate_random_number(min, max):
    """Generates a random number between `min` and `max`.

    Example:
    | ${random_number}= | Generate Random Number | ${0} | ${100} |
    =>
    | ${random_number}= 87
    """
    return random.randint(min, max)
