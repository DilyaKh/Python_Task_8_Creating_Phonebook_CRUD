from ask_parameters import find_parameters
from show_contact import show_contact


def modify_contacts(phone_book_list):
    '''
    Функция осуществляет изменение контактов 
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
        
        num_to_modify = -1


        while True:

            num_to_modify = int(input('\nВведите порядковый номер контакта, \
который нужно изменить.\n(Для завершения изменений нажмите 0): '))
            
            if num_to_modify == 0:
                break

            contact_to_change = contacts_found[num_to_modify - 1]
        
            print('\nВыбрано:')
            show_contact(list(contact_to_change.values()))
            

            
            parameter_num = None

            while parameter_num != 's':

                print('\nВыберите параметр для изменения.\n(Для завершения выбора параметров нажмите s): ')

                parameter_num = input('1 - изменение по фамилии\
                                \n2 - изменение по имени\
                                \n3 - изменение по отчеству\
                                \n4 - изменение по номеру телефона\
                                \n5 - изменение по описанию\
                                \ns - завершить изменение\n')
                print()
            
                parameter_input = None

                if parameter_num == '1':
                    parameter_input = input('Введите фамилию для изменения: ')
                elif parameter_num == '2':
                    parameter_input = input('Введите имя для изменения: ')
                elif parameter_num == '3':
                    parameter_input = input('Введите отчество для изменения: ')
                elif parameter_num == '4':
                    parameter_input = input('Введите телефонный номер для изменения: ')
                elif parameter_num == '5':
                    parameter_input = input('Введите содержание описания для изменения: ')
                elif parameter_num == 's':
                    break
                print()

                headers_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Отчество', \
                                    '4': 'Телефон' , '5': 'Описание'}
                    

                phone_book_list.remove(contact_to_change)

                contact_to_change[headers_dict[parameter_num]] = parameter_input

                phone_book_list.append(contact_to_change)


# ------------------------------------------------------------------