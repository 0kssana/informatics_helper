def is_valid_number(number, base):
    """
    Проверяет, является ли введенное число допустимым для данной системы счисления.
    """
    valid_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base]
    return all(digit in valid_digits for digit in number.upper())


def convert_from_base(number, base):
    """
        Convert a number from a given base to decimal with explanation.
        """
    decimal = 0
    explanation = []
    for i, digit in enumerate(reversed(number.upper())):
        value = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(digit) * (base ** i)
        explanation.append(f"{digit} * ({base}^{i}) = {value}")
        decimal += value
    return decimal, explanation
def convert_to_base(number, base):
    """
       Convert a decimal number to a given base with explanation.
       """
    if number < base:
        return "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[number], [f"{number} < {base}, записываем {number}"]
    else:
        next_number, next_explanation = convert_to_base(number // base, base)
        remainder = number % base
        explanation = next_explanation + [
            f"{number} / {base} = {number // base} (остаток {remainder}), записываем {'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[remainder]}"]
        return next_number + "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[remainder], explanation


def is_valid_base(base):
    """
    Проверяет, лежит ли основание системы счисления в диапазоне от 2 до 36.
    """
    return 2 <= base <= 36


def get_valid_base(prompt):
    """
    Запрашивает у пользователя ввод основания системы счисления и проверяет его корректность.
    """
    while True:
        try:
            base = int(input(prompt))
            if is_valid_base(base):
                return base
            else:
                print("Основание системы счисления должно быть в диапазоне от 2 до 36. Пожалуйста, попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")