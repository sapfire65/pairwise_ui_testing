from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from os.path import join, abspath


def working_with_table(file_name, tabs_number, string_tabl, column_tabl):
    add_files = abspath(join('.', file_name))
    # Настраиваем опции документа
    file_option = load_workbook(filename=add_files, data_only=True, read_only=True)

    # Получаем список с вкладками документа - sheetnames
    tabs = list(file_option.sheetnames)
    # Определяем нужную вкладку, икорректируем номер указания в функции. Зачем нам начинать с нуля? :)
    target_tabs = tabs[tabs_number - 1]

    # Обращаемся к нужной вкладке
    employees_sheet = file_option[f'{target_tabs}']

    list_value = list()
    while employees_sheet.cell(string_tabl, column_tabl).value is not None:
        list_value.append(employees_sheet.cell(string_tabl, column_tabl).value)
        string_tabl += 1
    return list_value


class ParsingTabs:
    car_type = working_with_table('ExLab_task.xlsx', 2, 3, 2)
    body_type = working_with_table('ExLab_task.xlsx', 2, 3, 3)
    car_brand = working_with_table('ExLab_task.xlsx', 2, 3, 4)
    fuel_for_car = working_with_table('ExLab_task.xlsx', 2, 3, 5)
    transmission = working_with_table('ExLab_task.xlsx', 2, 3, 6)
    car_color = working_with_table('ExLab_task.xlsx', 2, 3, 7)


for i in range(len(ParsingTabs.car_type)):
    print(ParsingTabs.car_type[i], '|', ParsingTabs.body_type[i], '|', ParsingTabs.car_brand[i], '|', ParsingTabs.fuel_for_car[i], '|', ParsingTabs.transmission[i], '|',
          ParsingTabs.car_color[i])
