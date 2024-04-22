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


# -------------------------------------------------------