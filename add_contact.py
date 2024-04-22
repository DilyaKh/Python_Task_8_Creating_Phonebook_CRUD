from get_data import get_data


def add_contact(phone_book_list):
    '''
    Функция добавляет к списку словарей,
    содержащих данные контактов,
    новый словарь (с данными нового контакта).
    '''
    headers = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    record = dict(zip(headers, get_data()))
    phone_book_list.append(record)


# ---------------------------------------------------