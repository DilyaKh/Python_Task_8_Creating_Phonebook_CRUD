from read_data import read_txt
from show_all_contacts import show_all_contacts


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


# --------------------------------------------------