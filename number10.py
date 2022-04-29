def get_weight():
    ves = float(input('Введите ваш вес на Земле: '))
    for i in range(16):
        ves += 1
        moon_ves = ves * 0.165
        print(f"Ваш вес на Луне в {i} год - ", '{:.2f}'.format(moon_ves))

get_weight()
