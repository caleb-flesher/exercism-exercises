def score(x, y):
    pos = ((x ** 2) + (y ** 2)) ** 0.5

    if (pos <= 1):
        return 10
    elif (pos <= 5):
        return 5
    elif (pos <= 10):
        return 1
    return 0
