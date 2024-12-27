def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    result = sum(num for num in range (1,number) if number % num == 0)
    
    if result == number:
        return "perfect"
    elif result < number:
        return "deficient"
    else:
        return "abundant"
