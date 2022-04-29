# Задание 5:
# Вам дан SET значений:

# uniques = {3,13,15,27,1,4,8,23,19,12,9,2,17}

# Создайте функцию которая:
# Удалите все чётные значения внутри SET, а оставшиеся отсортирует по убыванию.
# В результате, ваша функция должна вернуть отсортированный SET и неважно, каким будет SET растопленным или замороженным.
uniques = {3,13,15,27,1,4,8,23,19,12,9,2,17}
uniques_clone = set()
reverse_uniques = frozenset()
def get_chet():
    for i in uniques:
        if i % 2 == 0:
            uniques_clone.add(i)

    uni = uniques ^ uniques_clone
    for _ in range(len(uni)):
        elem = max(uni)
        uni.remove(elem)

if __name__ == '__main__':
    get_chet()
