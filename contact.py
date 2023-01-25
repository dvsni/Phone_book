from csv_create import creating
from csv_write import csv_writing

def greeting():
    print("Телефонный справочник!")
def get_info():
    info = []
    Last_name = input('Введите фамилию: ')
    info.append(Last_name)
    Name = input('Введите имя: ')
    info.append(Name)
    phone_number = input('Укажите телефон: ')
    info.append(phone_number)
    Comment = input('Укажите комментарий: ')
    info.append(Comment)
    return [Last_name, Name, phone_number, Comment]