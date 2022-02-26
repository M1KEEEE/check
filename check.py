import string

alphabet = string.ascii_lowercase + string.ascii_uppercase
alphabet += "0123456789_-"


def encode(text: str) -> str:
    result = ""
    for i in text:
        if len(str(alphabet.index(i))) == 1:
            result = result + "0" + str(alphabet.index(i))
        else:
            result += str(alphabet.index(i))
    return result
            
def decode(text: str) -> str:
    """
    пробежать по 2 
    если первй 0, то он откидывается
    ищем индекс в алфавите
    возвращаем по этому индексу из алфавита
    """    