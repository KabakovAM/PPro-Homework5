def feb_gen(num):
    a = 0
    b = 1
    yield a
    while num - 1 != 0:
        a, b = b, a + b
        yield a
        num -= 1

print(list(feb_gen(int(input('Введите количество чисел Фибоначчи: ')))))