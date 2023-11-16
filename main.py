from converterMain import converter_interface
from binOperMain import binary_operations_interface
from tableMain import truth_table_interface

def main_menu():
    while True:
        choice = input(
            "Выберите опцию:\n1. Конвертация систем счисления\n2. Операции с двоичными числами\n3. Таблица истинности\n4. Выход\nВаш выбор: ")
        if choice == '1':
            converter_interface()
        elif choice == '2':
            binary_operations_interface()
        elif choice == '3':
            truth_table_interface()
        elif choice == '4':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите опцию от 1 до 4.")


if __name__ == '__main__':
    main_menu()
