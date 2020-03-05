"""
contador de caracteres
"""


def counter_character(string):
    dic = {}
    for ctr in string:
        if not dic.get(ctr):
            dic[ctr] = string.count(ctr)
    return dic


if __name__=='__main__':
    print(counter_character('banana'))