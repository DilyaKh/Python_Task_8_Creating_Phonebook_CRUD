from read_data import read_txt
from show_all_contacts import show_all_contacts


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


# ----------------------------------------------------------