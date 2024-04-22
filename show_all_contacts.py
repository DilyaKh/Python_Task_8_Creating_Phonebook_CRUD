from show_contact import show_contact


def show_all_contacts(phone_book_list, is_sorted = 'no'):
    '''
    Функция выводит на печать все контакты,
    содержащиеся на данный момент в телефонном справочнике,
    в удобном для восприятия виде.
    Есть также дополнительный параметр sorted,
    с помощью которого можно задать сортировку 
    по фамилиям в алфавитном порядке.
    '''

    if is_sorted == 'yes':
        # Сортировка по фамилиям в алфавитном порядке:
        phone_book_list = sorted(phone_book_list, key = lambda x: list(x.values())[0])

    for i in enumerate(phone_book_list, 1):
        print(i[0], end = '')
        print('.', end = ' ')
        show_contact(list(i[1].values()))


# -----------------------------------------------------------