import export_data
import import_data
import view

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    second_name = input("Введите отчество: ")
    phone_number = input("Введите телефон: ")
    address = input("Введите адрес: ")
    return [last_name, first_name, second_name, phone_number, address]


def choice_separator():
    separator = input("Введите разделитель (, ; :): ")
    if separator == "":
        separator = None
    return separator


def selection_menu():
    print("\nВыберите нужный пункт меню:\n\
        1 - импорт;\n\
        2 - экспорт;\n\
        3 - поиск контакта;\n\
        0 - выход из программы")
    menu_actions()

def menu_actions():
    choice = input("Введите цифру: ")
    if choice == '1':
        separator = choice_separator()
        import_data.import_data(input_data(), separator)
        selection_menu()
    elif choice == '2':
        data = export_data.export_data()
        view.print_data(data)
        selection_menu()
    elif choice == '3':
        data = export_data.export_data()
        item = view.search_data(data)
        if item:
            print("ФАМИЛИЯ".center(15), "ИМЯ".center(15),
                  "ОТЧЕСТВО".center(15),
                  "ТЕЛЕФОН".center(15), "АДРЕС".center(20))
            print("-" * 90)
            print(item[0].ljust(15), item[1].ljust(15), item[2].ljust(15),
                  item[3].ljust(15), item[4].ljust(20))
        else:
            print("Данные не обнаружены")
        selection_menu()
    elif choice == '0':
        exit(0)
    else:
        print("Такого пункта нет!")
        selection_menu()