def steps(number):
    result = number
    count = 0

    if result < 1:
        raise ValueError("Only positive integers are allowed")
    
    while result != 1:
        result = result / 2 if result % 2 == 0 else result * 3 + 1
        count += 1
    return count
