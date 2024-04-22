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


# -----------------------------------------------------