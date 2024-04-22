from export_all import export_all
from export_chosen import export_chosen
from find_export_all import find_export_all
from find_export_chosen import find_export_chosen


def export_contacts(file_to_export, filename):
    '''
    Функция осуществляет экспорт контактов в другой файл,
    исходя из выбранных пользователей параметров.
    '''

    while True:
        print('\nВыберите режим для экспорта контактов: ')
        export_choice = input('''
1 - Перенести все контакты в другой файл\
\n2 - Из всего телефонного справочника \
выбрать контакты для переноса по их номерам \
\n3 - Сначала задать поиск по параметрам, \
а потом перенести все найденные контакты\
\n4 - Сначала задать поиск по параметрам, \
а потом перенести только выбранные по номерам контакты\
\n00 - Выйти из режима экспорта данных\n
''')


        if export_choice == '1':
            export_all(file_to_export, filename)
        elif export_choice == '2':
            export_chosen(file_to_export, filename)
        elif export_choice == '3':
            find_export_all(file_to_export, filename)
        elif export_choice == '4':
            find_export_chosen(file_to_export, filename)
        elif export_choice == '00':
            print('Работа в режиме экспорта данных завершена.')
            break


# -----------------------------------------------------