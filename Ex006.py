gen = (print(f'{i} x {j} = {i*j}') for i in range(2, 11) for j in range(2, 10))
for i in gen:
    next(gen)