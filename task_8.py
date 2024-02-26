# -------------------------------------------------------------------
# Task_8

import os



def work_with_phonebook():

    # Проверка, существует ли файл 'phonebook.txt':
    if not os.path.exists('phonebook.txt'):
        phone_book = []
        print('''
Файл с телефонным справочником пока не создан.\n
Добавьте в телефонный справочник хотя бы один контакт\n.
Для этого введите команду 2.
              ''')
    else:
        phone_book = read_txt('phonebook.txt')


    while True:

        choice = show_menu()

        if choice == '1':
            show_all_contacts(phone_book, is_sorted = 'yes')
        elif choice == '2':
            add_contact(phone_book)
            write_txt('phonebook.txt', phone_book) 
        elif choice == '3':
            find_contacts(phone_book)
        elif choice == '4':
            modify_contacts(phone_book)
            write_txt('phonebook.txt', phone_book)
        elif choice == '5':
            delete_contacts(phone_book)
            write_txt('phonebook.txt', phone_book)
        elif choice == '6':
            file_to_export = input('Введите название файла для экспорта \
(например, phonebook_copy.txt): ')
            export_contacts(file_to_export, 'phonebook.txt')
        elif choice == '7':
            file_to_import = input('Введите название файла для импорта \
(например, phonebook_from.txt): ')
            import_contacts(file_to_import, 'phonebook.txt')
        elif choice == '0':
            print('''
Работа программы завершена.\n\
----------------------------\n\
----------------------------\n
                  ''')
            break
        else:
            print('\nНекорректно введен номер действия!\
                  \nВведите номер действия заново.')



def show_menu():
    '''
    Функция отображает меню - 
    соответствие между цифрами и действиями,
    которые может выбрать пользователь,
    и возвращет введенное пользователем значение.
    '''

    print('''
------------------------------------------\n
Выберите необходимое действие:\n
1 - Отобразить весь телефонный справочник\n
2 - Добавить новый контакт\n
3 - Найти контакт(ы) по выбранному параметру\n
4 - Изменить контакт(ы) по выбранным параметрам\n
5 - Удалить контакт(ы) по выбранным параметрам\n
6 - Экспорт контактов в другой файл c выбором параметров\n
7 - Импорт контактов из другого файла c выбором параметров\n
0 - Завершить работу программы\n
          ''')
    
    # Не переводится в целочисленный тип данных,
    # т.к. пользователь может ошибочно ввести, например,
    # текст, и тогда это повлечет ошибку.
    # Программа выведет оповещение, если номер действия 
    # не будет соответствовать предлагаемым в меню номерам. 
    choice = input()
    print()

    return choice



def read_txt(filename):
    '''
    Функция считывает построчно содержимое 
    файла 'phonebook.txt'
    и сохраняет данные контактов в виде списка словарей.
    Возвращает список словарей.
    '''
 
    phone_book_list = []

    headers = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']

    with open(filename,'r', encoding = 'utf-8') as phb:

        for line in phb:

            record = dict(zip(headers, line.strip().split(',')))          
            phone_book_list.append(record)	
    
    return phone_book_list



def show_contact(values):
    '''
    Функция выводит на печать один контакт
    в удобном для восприятия виде.
    Т.е. именно при помощи этой функции можно 
    задать единообразное для всей программы
    визуальное отображение контакта
    для вывода его при запросе пользователя.
    '''

    return print(f'👤 {values[0]} {values[1]} {values[2]}  \
📞 {values[3]}  📝 {values[4]}')



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
            
    

def write_txt(filename, phone_book_list):
    '''
    Функция позволяет осуществить перезапись 
    с сохранением в файл 'phonebook.txt' 
    содержимого списка словарей с данными контактов.
    '''

    with open(filename, 'w', encoding = 'utf-8') as phout:

        for i in phone_book_list:
            s = ''

            for v in i.values():
                s = s + v + ','

            phout.write(f'{s[:-1]}\n')



def get_data():
    '''
    Функция запрашивает у пользователя параметры контакта
    и возвращает список, содержащий эти параметры.
    '''

    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    surname = input('Введите отчество: ')
    phone_number = input('Введите номер телефона (в формате +79123456789): ')
    phone_descr = input('Введите описание контакта: ')
    print('\nКонтакт сохранен')
    
    data_list = [last_name, first_name, surname, phone_number, phone_descr]
    return data_list



def add_contact(phone_book_list):
    '''
    Функция добавляет к списку словарей,
    содержащих данные контактов,
    новый словарь (с данными нового контакта).
    '''
    headers = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    record = dict(zip(headers, get_data()))
    phone_book_list.append(record)



def find_parameters():
    '''
    Функция запрашивает у пользователя,
    по каким параметрам совершить поиск.
    Возвращает переменные с названием параметра
    и номером параметра.
    '''

    print('Выберите параметр для поиска:')
    parameter_num = input('1 - по фамилии\
                            \n2 - по имени\
                            \n3 - по отчеству\
                            \n4 - по номеру телефона\
                            \n5 - по описанию\n')
    print()

    parameter_input = None

    if parameter_num == '1':
        parameter_input = input('Введите фамилию для поиска: ')
    elif parameter_num == '2':
        parameter_input = input('Введите имя для поиска: ')
    elif parameter_num == '3':
        parameter_input = input('Введите отчество для поиска: ')
    elif parameter_num == '4':
        parameter_input = input('Введите телефонный номер для поиска: ')
    elif parameter_num == '5':
        parameter_input = input('Введите содержание описания для поиска: ')
        print()
    return parameter_input, parameter_num



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



def export_all(file_to_export, filename):
    '''
    Функция осуществляет перенос всех контактов 
    в другой файл.
    Данные записываются в другой файл 
    в режиме добавления новых записей.
    '''

    with open(file_to_export, 'a', encoding = 'utf-8') as new_file, \
        open(filename, 'r', encoding = 'utf-8') as main_file:
        contacts_to_add = main_file.readlines()
        new_file.writelines(contacts_to_add)
    
    print('Экспорт данных завершен.')



def export_chosen(file_to_export, filename):
    '''
    Функция осуществляет перенос контактов в другой файл:
    Из всего телефонного справочника пользователь
    выбирает контакты для переноса по их номерам.
    Данные записываются в другой файл
    в режиме добавления новых записей.
    '''

    phone_book_list = read_txt(filename)

    show_all_contacts(phone_book_list)
    print()

    while True:
        num_to_export = input('\nВведите порядковый номер контакта, \
который нужно экспортировать.\nЕсли нужно экспортировать несколько контактов сразу,\n\
то введите их в строку через пробел\n(Для завершения экспорта нажмите d): ')
            
        if num_to_export == 'd':
            break

        num_to_export_list = map(int, num_to_export.split())

        contacts_export = []

        for i in num_to_export_list:
            contacts_export.append(phone_book_list[i - 1])

        with open(file_to_export, 'a', encoding = 'utf-8') as new_file:
            for i in contacts_export:
                s = ''

                for v in i.values():
                    s = s + v + ','

                new_file.write(f'{s[:-1]}\n')

        print('Экспорт данных завершен.')



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



def find_export_chosen(file_to_export, filename):
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


    while True:
        num_to_export = input('\nВведите порядковый номер контакта, \
который нужно экспортировать.\nЕсли нужно экспортировать несколько контактов сразу,\n\
то введите их в строку через пробел\n(Для завершения экспорта нажмите d): ')
            
        if num_to_export == 'd':
            break

        num_to_export_list = map(int, num_to_export.split())

        contacts_found_export = []

        for i in num_to_export_list:
            contacts_found_export.append(contacts_found[i - 1])

        with open(file_to_export, 'a', encoding = 'utf-8') as new_file:
            for i in contacts_found_export:
                s = ''

                for v in i.values():
                    s = s + v + ','

                new_file.write(f'{s[:-1]}\n')

        print('Экспорт данных завершен.')

    

def import_contacts(file_to_import, filename):
    '''
    Функция осуществляет импорт контактов из другого файла,
    исходя из выбранных пользователей параметров.
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



def import_all(file_to_import, filename):
    '''
    Функция осуществляет перенос всех контактов 
    из другого файла (file_to_import).
    Данные записываются в файл (filename)
    в режиме добавления новых записей.
    '''

    with open(file_to_import, 'r', encoding = 'utf-8') as new_file, \
        open(filename, 'a', encoding = 'utf-8') as main_file:
        contacts_to_add = [(i.strip() + '\n') for i in new_file.readlines()]
        main_file.writelines(contacts_to_add)
    
    print('Импорт данных завершен.')



def import_chosen(file_to_import, filename):
    '''
    Функция осуществляет перенос контактов 
    из другого файла:
    из всего телефонного справочника пользователь
    выбирает контакты для переноса по их номерам.
    Данные записываются в файл
    в режиме добавления новых записей.
    '''

    phone_book_list = read_txt(file_to_import)

    show_all_contacts(phone_book_list)
    print()

    while True:
        num_to_import = input('\nВведите порядковый номер контакта, \
который нужно импортировать.\nЕсли нужно импортировать несколько контактов сразу,\n\
то введите их в строку через пробел\n(Для завершения импорта нажмите d): ')
            
        if num_to_import == 'd':
            break

        num_to_import_list = map(int, num_to_import.split())

        contacts_import = []

        for i in num_to_import_list:
            contacts_import.append(phone_book_list[i - 1])

        with open(filename, 'a', encoding = 'utf-8') as main_file:
            for i in contacts_import:
                s = ''

                for v in i.values():
                    s = s + v + ','

                main_file.write(f'{s[:-1]}\n')

        print('Импорт данных завершен.')



def find_import_all(file_to_import, filename):
    '''
    Функция осуществляет импорт контактов 
    из другого файла,
    исходя из выбранных пользователем параметров:
    cначала задается поиск по параметрам, \
    а потом переносятся все найденные контакты.
    Данные записываются в файл
    в режиме добавления новых записей.
    '''

    phone_book_list = read_txt(file_to_import)


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


    print('\nПеренести в файл все найденные контакты?: ')
    export_yes_no = input('1 - Да, 2 - Нет: ')

    if export_yes_no == '2':
         return print('Работа в режиме импорта завершена.')
    elif export_yes_no == '1':

        with open(filename, 'a', encoding = 'utf-8') as main_file:
            for i in contacts_found:
                s = ''

                for v in i.values():
                    s = s + v + ','

                main_file.write(f'{s[:-1]}\n')

        print('Импорт данных завершен.')



def find_import_chosen(file_to_import, filename):
    '''
    Функция осуществляет импорт контактов в файл,
    исходя из выбранных пользователем параметров:
    cначала задается поиск по параметрам, \
    а потом переносятся все найденные контакты.
    Данные записываются в файл
    в режиме добавления новых записей.
    '''

    phone_book_list = read_txt(file_to_import)


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


    while True:
        num_to_import = input('\nВведите порядковый номер контакта, \
который нужно импортировать.\nЕсли нужно импортировать несколько контактов сразу,\n\
то введите их в строку через пробел\n(Для завершения импорта нажмите d): ')
            
        if num_to_import == 'd':
            break

        num_to_import_list = map(int, num_to_import.split())

        contacts_found_import = []

        for i in num_to_import_list:
            contacts_found_import.append(contacts_found[i - 1])

        with open(filename, 'a', encoding = 'utf-8') as main_file:
            for i in contacts_found_import:
                s = ''

                for v in i.values():
                    s = s + v + ','

                main_file.write(f'{s[:-1]}\n')

        print('Импорт данных завершен.')



# -------------------------------------------



work_with_phonebook()

# -------------------------------------------------------------------------
