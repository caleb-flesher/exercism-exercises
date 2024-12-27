import string

def is_pangram(sentence):
    result = set()
    for let in sentence.replace(" ", "").lower():
        if let not in string.punctuation and let not in string.digits:
            result.add(let)
    return len(result) == 26
    