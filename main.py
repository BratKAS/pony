import openpyxl


wb = openpyxl.load_workbook('input.xlsx')
sheet = wb.active
data = []

i = 0
for column in sheet.iter_cols(values_only=True):
    data.append([])
    for cell in column:
        if cell is not None:
            data[i].append(cell)
    i += 1

picture_1 = data[0]
picture_2 = data[1]
chosen = data[2]
table_1 = [[0, 0], [0, 0]]
table_2 = [[0, 0], [0, 0]]

n = len(chosen)

for k in range(1, n):
    if chosen[k] == 1:
        if 0 <= picture_1[k] <= 0.5:
            i = 0
        elif 0.5 < picture_1[k] <= 1:
            i = 1
        else:
            print('incorrect data picture_1')
            exit()

        if 0 <= picture_2[k] <= 0.5:
            j = 0
        elif 0.5 < picture_2[k] <= 1:
            j = 1
        else:
            print('incorrect data picture_2')
            exit()

        table_1[i][j] += 1

    elif chosen[k] == 2:
        if 0 <= picture_1[k] <= 0.5:
            i = 0
        elif 0.5 < picture_1[k] <= 1:
            i = 1
        else:
            print('incorrect data picture_1')
            exit()

        if 0 <= picture_2[k] <= 0.5:
            j = 0
        elif 0.5 < picture_2[k] <= 1:
            j = 1
        else:
            print('incorrect data picture_2')
            exit()

        table_2[i][j] += 1
    else:
        print('incorrect data')


