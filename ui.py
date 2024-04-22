from read_data import read_txt
from show_contact import show_contact
from show_all_contacts import show_all_contacts
from overwrite import write_txt
from get_data import get_data
from add_contact import add_contact
from ask_parameters import find_parameters
from find_contacts import find_contacts
from modify_contacts import modify_contacts
from delete_contacts import delete_contacts
from export_contacts import export_contacts
from export_all import export_all
from export_chosen import export_chosen
from find_export_all import find_export_all
from find_export_chosen import find_export_chosen
from import_contacts import import_contacts
from import_all import import_all
from import_chosen import import_chosen
from find_import_all import find_import_all
from find_import_chosen import find_import_chosen



import os


def work_with_phonebook():

    # Проверка, существует ли файл 'phonebook.txt':
    if not os.path.exists('data\phonebook.txt'):
        phone_book = []
        print('''
Файл с телефонным справочником пока не создан.\n
Добавьте в телефонный справочник хотя бы один контакт\n.
Для этого введите команду 2.
              ''')
    else:
        phone_book = read_txt('data\phonebook.txt')


    while True:

        choice = show_menu()

        if choice == '1':
            show_all_contacts(phone_book, is_sorted = 'yes')
        elif choice == '2':
            add_contact(phone_book)
            write_txt('data\phonebook.txt', phone_book) 
        elif choice == '3':
            find_contacts(phone_book)
        elif choice == '4':
            modify_contacts(phone_book)
            write_txt('data\phonebook.txt', phone_book)
        elif choice == '5':
            delete_contacts(phone_book)
            write_txt('data\phonebook.txt', phone_book)
        elif choice == '6':
            file_to_export = 'data\\' + input('Введите название файла для экспорта \
(например, phonebook_copy.txt): ')
            export_contacts(file_to_export, 'data\phonebook.txt')
        elif choice == '7':
            file_to_import = 'data\\' + input('Введите название файла для импорта \
(например, phonebook_from.txt): ')
            import_contacts(file_to_import, 'data\phonebook.txt')
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


# -----------------------------------------------------