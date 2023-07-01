name = ['Вася', 'Миша', 'Саша']
salary = [500, 600, 700]
bonus = ['15%', '10.25%', '25%']
print({key: i / 100 * float(j[0:-1]) for key, i, j in zip(name, salary, bonus)})