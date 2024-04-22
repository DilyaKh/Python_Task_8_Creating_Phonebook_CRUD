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


# ----------------------------------------------------------