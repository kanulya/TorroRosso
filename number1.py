string = input('Введите слово или предложение на ангилийском: ')

def delete():
    _str = string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for vowel in vowels:
        _str = _str.replace(vowel, "")
    print(_str)
    return _str
if __name__ == '__main__':
    delete()
    print()
