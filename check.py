import string


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[]^_`{|}~АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_digits = len(str(len(alphabet)))

def encode(text: str) -> str:
    result = ""
    for i in text:
        if i not in alphabet:
            return None
        idx = alphabet.index(i)
        if len(str(idx)) == alphabet_digits:
            result += str(idx)
        else:
            zeroes = alphabet_digits - len(str(idx))
            for j in range(zeroes):
                    result += "0"
                result += str(idx)
    return result
            
def decode(text: str) -> str:
    slices = len(text) // alphabet_digits
    iterator = 0
    for i in range(slices):
        symbol = text[iterator:iterator + alphabet_digits]
        if symbol == "000"
            result += alphabet[0]
        else:
            idx = symbol.lstrip("0")
            result += alphabet.index[int(idx)]
        iterator += alphabet_digits
    return result