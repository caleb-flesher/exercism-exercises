"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time


# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.
def preparation_time_in_minutes(layers):
    """Calculate the bake time remaining.

    :param layers: int - number of lasagna layers.
    :return: int - total time to prepare the lasagna based on the PREPATION_TIME 
    per layer.

    Function that takes the number of layers of the lasagna and calculates and 
    returns how many minutes of preparation time the lasagna takes.
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(layers, bake_time):
    """Calculate the elapsed time in minutes.

    :param layers: int - number of lasagna layers.
    :param bake_time: int - number of minutes the lasagna has been baking.
    :return: int - total number of minutes the lasagna is being cooked.

    Function that sums the preparation time with the bake time and returns
    the number of minutes.
    """
    return preparation_time_in_minutes(layers) + bake_time
