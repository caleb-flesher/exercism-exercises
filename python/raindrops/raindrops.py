def convert(number):
    result = ""
    if not number % 3:
        result += "Pling"
    if not number % 5:
        result += "Plang"
    if not number % 7:
        result += "Plong"
    if len(result) < 1:
        result += str(number)
    return result