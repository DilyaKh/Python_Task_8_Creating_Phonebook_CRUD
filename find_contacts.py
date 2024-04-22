from ask_parameters import find_parameters
from show_all_contacts import show_all_contacts


def find_contacts(phone_book_list):
    '''
    Функция осуществляет поиск по заданному параметру
    и выводит на печать контакты, если они были найдены.
    Если же контакты не были найдены,
    об этом выводится соответствующее оповещение.
    '''

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


# ----------------------------------------------------