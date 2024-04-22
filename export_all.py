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


# ----------------------------------------------------------