from find_import_all import find_import_all
from find_import_chosen import find_import_chosen
from import_all import import_all
from import_chosen import import_chosen


def import_contacts(file_to_import, filename):
    '''
    Функция осуществляет импорт контактов из другого файла,
    исходя из выбранных пользователем параметров.
    '''


    while True:
        print('\nВыберите режим для импорта контактов: ')
        import_choice = input('''
1 - Перенести все контакты из другого файла\
\n2 - Из всего файла выбрать контакты \
для переноса по их номерам\
\n3 - Сначала задать поиск по параметрам, \
а потом перенести все найденные контакты\
\n4 - Сначала задать поиск по параметрам, \
а потом перенести только выбранные по номерам контакты\
\n00 - Выйти из режима импорта данных\n
''')


        if import_choice == '1':
            import_all(file_to_import, filename)
        elif import_choice == '2':
            import_chosen(file_to_import, filename)
        elif import_choice == '3':
            find_import_all(file_to_import, filename)
        elif import_choice == '4':
            find_import_chosen(file_to_import, filename)
        elif import_choice == '00':
            print('Работа в режиме импорта данных завершена.')
            break


# -----------------------------------------------------