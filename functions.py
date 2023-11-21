import os
import re
import openpyxl

def get_list():
    # Получаем текущую директорию проекта
    project_directory = os.getcwd()

    # Путь к папке input
    input_directory = os.path.join(project_directory, 'input')

    # Получаем список всех файлов в папке input
    files = os.listdir(input_directory)

    # Фильтруем файлы по расширению xlsx
    xlsx_files = [file for file in files if file.endswith('.xlsx')]

    return xlsx_files


def get_adults(file_names):
    adults = []
    for file in file_names:
        match = re.search(r'\d', file)
        if match:
            firs_number = match.group()

        if firs_number == '2':
            adults.append(file)

    return adults



def get_kids(file_names):
    kids = []
    for file in file_names:
        match = re.search(r'\d', file)
        if match:
            firs_number = match.group()

        if firs_number == '1':
            kids.append(file)

    return kids


def get_table(file_names, input_directory):
    # Выводим список названий файлов
    for file in file_names:

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

        table = [[0, 0, 0], [0, 0, 0]]

        n = len(chosen)

        for k in range(n):
            pair = [picture_1[k], picture_2[k]]
            bright = max(pair)
            bright_index = pair.index(bright)

            if bright_index == int(chosen[k]) - 1:
                j = 0
            else:
                j = 1

            if picture_1[k] <= 0.5 and picture_2[k] <= 0.5:
                i = 0
            elif 0.5 < max([picture_1[k], picture_2[k]]) and min([picture_1[k], picture_2[k]]) <= 0.5:
                i = 1
            elif 0.5 < picture_1[k] and 0.5 < picture_2[k]:
                i = 2
            else:
                print('incorrect data')

            table[j][i] += 1

    return table

def get_table_theor(table):
    table__theor = [[0, 0, 0], [0, 0, 0]]
    overall = sum(table[0]) + sum(table[1])

    for j in range(2):
        for i in range(3):
            table__theor[j][i] = sum(table[j]) * (table[0][i] + table[1][i]) / overall

    return table__theor


def get_chi2_exp(table, table__theor):
    chi2_exp = 0
    for j in range(2):
        for i in range(3):
            chi2_exp += (table__theor[j][i] - table[j][i]) ** 2 / table__theor[j][i]

    return chi2_exp
