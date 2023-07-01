def path_file(data: str):
    *path, file = data.split('\\')
    name, extension = file.split('.')
    path = '\\'.join(path)
    return path, name, extension

print(path_file(input('Введите абслолютный путь к файлу: ')))