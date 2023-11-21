from functions import *


file_names = get_list()
kids = get_kids(file_names)
adults = get_adults(file_names)

project_directory = os.getcwd()
input_directory = os.path.join(project_directory, 'input')

table_kids = get_table(kids, input_directory)
table_kids_theor = get_table_theor(table_kids)
chi2_kids_exp = get_chi2_exp(table_kids, table_kids_theor)
print('\nKids:')
print(f'Таблица эксп значений: {table_kids}')
print(f'Таблица ожидаемых значений: {table_kids_theor}')
print(f'Эксп значение хи-квадрат: {chi2_kids_exp}')
print(f'Теор значение хи-квадрат: 5.99 (a = 0.05, k = 2)')

table_adults = get_table(adults, input_directory)
table_adults_theor = get_table_theor(table_adults)
chi2_adults_exp = get_chi2_exp(table_adults, table_adults_theor)
print('\nAdults:')
print(f'Таблица эксп значений: {table_adults}')
print(f'Таблица ожидаемых значений: {table_adults_theor}')
print(f'Эксп значение хи-квадрат: {chi2_adults_exp}')
print(f'Теор значение хи-квадрат: 5.99 (a = 0.05, k = 2)')
