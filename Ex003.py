dic_iter = iter({i: ord(i) for i in input('Введите текст: ')}.items())
for i in range(5):
    print(next(dic_iter))