from ask_parameters import find_parameters
from show_contact import show_contact


def delete_contacts(phone_book_list):
    '''
    Функция осуществляет удаление контактов 
    по заданным параметрам.
    '''

    print('Сначала осуществим поиск контакта(ов) \
по заданному параметру.')

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

        for i in enumerate(contacts_found, 1):
            print(i[0], end = '')
            print('.', end = ' ')
            show_contact(list(i[1].values()))
        

        num_to_delete = -1
        len_to_check = len(contacts_found)

        while True:

            if len_to_check == 0:
                print('Все найденные значения были удалены.')
                break
        
            num_to_delete = input('\nВведите порядковый номер контакта, \
который нужно удалить.\nЕсли нужно удалить несколько контактов сразу,\n\
то введите их в строку через пробел\n(Для завершения удалений нажмите 0): ')
            
            if num_to_delete == '0':
                break

            num_to_delete_list = map(int, num_to_delete.split())


            for num in num_to_delete_list:

                contact_to_delete = contacts_found[num - 1]
            
                print('\nВыбрано:')
                show_contact(list(contact_to_delete.values()))
                
                phone_book_list.remove(contact_to_delete)
                len_to_check -= 1
                
                print('\nКонтакт удален.')


# ---------------------------------------------------------------------