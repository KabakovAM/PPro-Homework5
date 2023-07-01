def simple_gen(num):
    i = 1
    data = 1
    while num != 0:
        check = 0
        while i <= data:
            if data % i == 0:
                check += 1
            i += 1
        if check == 2:
            yield data
            num -= 1
        i = 1
        data += 1

print(list(simple_gen(int(input('Введите количество простых чисел: ')))))