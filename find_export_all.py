from ask_parameters import find_parameters
from read_data import read_txt
from show_all_contacts import show_all_contacts


def find_export_all(file_to_export, filename):
    '''
    Функция осуществляет экспорт контактов в другой файл,
    исходя из выбранных пользователем параметров:
    cначала задается поиск по параметрам, \
    а потом переносятся все найденные контакты.
    Данные записываются в другой файл
    в режиме добавления новых записей.
    '''

    phone_book_list = read_txt(filename)


    parameter_input, parameter_num = find_parameters()

    contacts_found = []

    for i in phone_book_list:
        if list(i.values())[int(parameter_num) - 1].lower() == \
            parameter_input.lower():
            contacts_found.append(i)

    if len(contacts_found) == 0:
        print('По заданному параметру контакты не найдены')
    else:
        print('\nНайдено в телефонной книге:')
        show_all_contacts(contacts_found)
    print()


    print('\nПеренести в другой файл все найденные контакты?: ')
    export_yes_no = input('1 - Да, 2 - Нет: ')

    if export_yes_no == '2':
         return print('Работа в режиме экспорта завершена.')
    elif export_yes_no == '1':

        with open(file_to_export, 'a', encoding = 'utf-8') as new_file:
            for i in contacts_found:
                s = ''

                for v in i.values():
                    s = s + v + ','

                new_file.write(f'{s[:-1]}\n')

        print('Экспорт данных завершен.')


# ------------------------------------------------