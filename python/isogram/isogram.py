def is_isogram(string):
    alt = string.lower().replace(" ", "").replace("-", "")
    if (len(set(alt)) == len(alt)):
        return True
    return False
