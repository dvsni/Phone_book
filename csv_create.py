def creating():
    file = 'Phone_book.csv'
    with open(file, 'w', encoding = 'UTF-8') as data:
        data.write(f'Фамилия; Имя; Телефон; Описание\n')