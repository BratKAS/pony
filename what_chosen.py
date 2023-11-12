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

n = len(chosen)
d = []
if_equal = []

for k in range(1, n):
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

