import string


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[]^_`{|}~АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def encode(text: str) -> str:
    result = ""
    for i in text:
        idx = 
        alphabet_digits = len(str(len(alphabet)))
        if len(str(alphabet_digits)) == alphabet_digits:
            result += str(alphabet_digits)
        else:
            zeroes = alphabet_digits - len(str(idx))
            for j in range(zeroes):
                    result += "0"
                result += str(alphabet_digits)
    return result
            
def decode(text: str) -> str:
    slices = len(text) // 3
    iterator = 0
    for i in range(slices):
        symbol = text[iterator:iterator + 3]
        if symbol == "000"
            result += alphabet[0]
        else:
            idx = symbol.lstrip("0")
            result += alphabet.index[int(idx)]
        iterator += 3
    return result