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


# --------------------------------------------------------