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


# ----------------------------------------------------------