def rebase(input_base, digits, output_base):
    result = []
    # Exceptions
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if len([digit for digit in digits if digit < 0]) != 0 \
        or len([digit for digit in digits if digit >= input_base]) != 0:
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Sum the enumerated digits list then convert
    number = sum(digit * input_base ** power for power, digit in enumerate(digits[::-1]))
    if number == 0: return [0]
    while number:
        result.insert(0, number % output_base)
        number //= output_base
    return result