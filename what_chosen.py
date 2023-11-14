import openpyxl
import os

# Получаем текущую директорию проекта
project_directory = os.getcwd()

# Путь к папке input
input_directory = os.path.join(project_directory, 'input')

# Получаем список всех файлов в папке input
files = os.listdir(input_directory)

# Фильтруем файлы по расширению xlsx
xlsx_files = [file for file in files if file.endswith('.xlsx')]

# Выводим список названий файлов
for file in xlsx_files:

    path = os.path.join(input_directory, file)
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    data = []

    i = 0
    for column in sheet.iter_cols(values_only=True):
        data.append([])
        for cell in column:
            if cell is not None and cell != 'NaN':
                data[i].append(cell)
        i += 1

    picture_1 = data[0]
    picture_2 = data[1]
    chosen = data[2]

    n = len(chosen)
    d = []
    if_equal = []

    for k in range(n):
        if (picture_1[k] < picture_2[k]) and (chosen[k] == 1):
            d.append(0)
        elif (picture_1[k] < picture_2[k]) and (chosen[k] == 2):
            d.append(1)
        elif (picture_1[k] > picture_2[k]) and (chosen[k] == 1):
            d.append(1)
        elif (picture_1[k] > picture_2[k]) and (chosen[k] == 2):
            d.append(0)
        elif (picture_1[k] == picture_2[k]) and (picture_1[k] < 0.5) and (chosen[k] == 1):
            if_equal.append(1)
        elif (picture_1[k] == picture_2[k]) and (picture_1[k] < 0.5) and (chosen[k] == 2):
            if_equal.append(0)
        elif (picture_1[k] == picture_2[k]) and (picture_1[k] > 0.5) and (chosen[k] == 1):
            if_equal.append(0)
        elif (picture_1[k] == picture_2[k]) and (picture_1[k] > 0.5) and (chosen[k] == 2):
            if_equal.append(1)

        else:
            print(k)
            print('incorrect data')
    # print(d)
    # print(if_equal)

    print(f'\n{file}: {sum(d)}/{len(d)}')
    print(f'{file}: {sum(if_equal)}/{len(if_equal)}')
