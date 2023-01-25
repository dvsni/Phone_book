from contact import get_info as gi

info = gi()
def csv_writing():
    file = 'Phone_book.csv'
    with open(file, 'a', encoding = 'UTF-8') as data:
        data.write(f'{info[0]}; {info[1]}; {info[2]}; {info[3]}\n')