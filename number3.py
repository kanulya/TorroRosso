# Задание 3:
# Вам даны 2 листа:

# list_1 = ['a', 'bc', 'de']
# list_2 = ['ab', 'c', 'de']

# Напишите функцию которая их принимает и сравнивает на равность.
# Пример где листы равны:

    # a + bc + de = abcde
    # ab + c + de = abcde

    # list_1 = ['123', 'abc', 'de']
    # list_2 = ['1', '23', 'abcde']


# Пример где листы НЕ равны:

    # a + cb + de = acbde
    # ab + c + de = abcde

    # list_1 = ['123', 'abc', 'de']
    # list_2 = ['123', 'de', 'abc']
import functools

list_1 = ['123', 'abc', 'de']
list_2 = ['123', 'de', 'abc']
c1 = []
c2 = []
def evaluate(a, b):
    for i in a:
        for j in i:
            c1.append(j)
    for i in b:
        for j in i:
            c2.append(j)
    print(c1, c2)
    if c1 == c2:
        print("Эти листы равны")
    else:
        print("Эти листы не равны")
if __name__ == '__main__':
    evaluate(list_1, list_2)
