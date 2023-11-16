

def converter_interface():
    from_base = get_valid_base("Введите основание исходной системы счисления (между 2 и 36): ")
    to_base = get_valid_base("Введите основание целевой системы счисления (между 2 и 36): ")

    number = input(f"Введите число в системе счисления с основанием {from_base}: ")

    if not is_valid_number(number, from_base):
        print(f"Некорректный ввод: {number} не является числом в системе счисления с основанием {from_base}")
        return

    decimal_number, explanation_from = convert_from_base(number, from_base)
    result, explanation_to = convert_to_base(decimal_number, to_base)

    print("Преобразование в десятичную систему:")
    print("\n".join(explanation_from))
    print("\nПреобразование из десятичной системы:")
    print("\n".join(explanation_to))
    print(f"\nЧисло в системе счисления с основанием {to_base}: {result}")