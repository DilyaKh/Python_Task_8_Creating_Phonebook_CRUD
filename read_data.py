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


# ----------------------------------------------------------------