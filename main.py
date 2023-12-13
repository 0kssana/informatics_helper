<<<<<<< HEAD
from converterMain import converter_interface
from binOperMain import binary_operations_interface
from tableMain import truth_table_interface
>>>>>>> converter


class CalculatorError(Exception):
    pass


class InvalidInputError(CalculatorError):

    def __init__(self, message="Некорректный ввод"):
        self.message = message
        super().__init__(self.message)



class CalculationError(CalculatorError):

    def __init__(self, message="Ошибка во время вычислений."):
        self.message = message
        super().__init__(self.message)
   

class Calculator:
    class LogicExpressionParser:
        def __init__(self):
            self.operators = {'and', 'or', 'not'}
            self.variables = set()
            self.expression_structure = []

        def analyze_logic_expression(self, expression):
            current_token = ''

            for char in expression:
                if char.isalpha() or char.isdigit():
                    current_token += char
                elif char == ' ':
                    if current_token:
                        self.process_token(current_token)
                        current_token = ''
                else:
                    if current_token:
                        self.process_token(current_token)
                        current_token = ''
                    self.process_char(char)

            if current_token:
                self.process_token(current_token)

            return self.variables, self.expression_structure

        def process_token(self, token):
            if token.lower() in self.operators:
                self.expression_structure.append(('Оператор', token.lower()))
            else:
                self.variables.add(token)

        def process_char(self, char):
            if char in {'(', ')'}:
                self.expression_structure.append(('Скобка', char))

    @staticmethod
    def convert_number_step_by_step(num, from_base, to_base):

        if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
            raise InvalidInputError("Ошибка: Неподдерживаемая система счисления.")

        steps = []

        while num > 0:
            quotient = num // to_base
            remainder = num % to_base
            steps.append((num, quotient, remainder))
            num = quotient

        return steps[::-1]


    @staticmethod
    def display_conversion_steps(steps, result_base):
        for step in steps:
            print(f"{step[0]} // {result_base} = {step[1]}, остаток = {step[2]}")

        string = ''.join(map(str, [step[2] for step in steps]))
        if result_base >= 16:
            result = ""
            for i in range(len(string) - 2, -2, -2):
                num = int(string[i:i + 2]) if i >= 0 else int(string[:-i])
                if 10 <= num <= result_base:
                    letter = chr(ord('A') + num - 10)
                else:
                    letter = str(num)

                result = letter + result

            print(f"Результат в системе счисления {result_base}: {result}")
            return result
        else:
            print(f"Результат в системе счисления {result_base}: {string}")
            return string

    @staticmethod
    def build_truth_table(expression):
        variables = sorted(set(re.findall(r'\b[A-Za-z]\b', expression)))
        table_header = variables + [expression]
        table_rows = []

        for values in product([0, 1], repeat=len(variables)):
            row = list(values)
            assignment_dict = dict(zip(variables, values))
            result = int(eval(expression, assignment_dict))
            row.append(result)
            table_rows.append(row)

        return table_header, table_rows

    @staticmethod
    def print_truth_table(header, rows):
        table = PrettyTable(header)
        table.align = "c"

        for row in rows:
            table.add_row(row)

        print(table)

    @staticmethod
    def binary_multiply_with_steps(a, b):
        result = 0
        shift = 0

        print(f"{bin(a)[2:]:>5}   ({a})")
        print(f"x {bin(b)[2:]:>3}   ({b})")
        print("-" * 11)

        while b > 0:
            if b % 2 == 1:
                partial_product = a << shift
                result += partial_product
                print(f"{bin(partial_product)[2:]:>5}   ({partial_product}), Shift: {shift}")

            b >>= 1
            shift += 1

        print("-" * 11)
        print(f"{bin(result)[2:]:>5}   ({result} в десятичной)")

        return result

    @staticmethod
    def binary_divide_with_steps(dividend, divisor):
        try:
            if divisor == 0:
                raise ZeroDivisionError("Нельзя делить на ноль")

            quotient = 0
            remainder = 0
            position = len(bin(dividend)[2:])

            print(f"{bin(dividend)[2:]}   ({dividend})")
            print(f"/ {bin(divisor)[2:]:>{position}}   ({divisor})")
            print("-" * (position + 3))

            while position >= 0:
                remainder <<= 1
                remainder |= (dividend >> position) & 1
                if remainder >= divisor:
                    remainder -= divisor
                    quotient |= (1 << position)

                position -= 1

                print(f"{bin(quotient)[2:]:>{position + 3}} R:{bin(remainder)[2:]}")

            print("-" * (position + 3))
            print(f"{bin(quotient)[2:]:>{position + 3}}   ({quotient} в десятичной)")
            return quotient

        except ZeroDivisionError as e:
            raise CalculationError(f"Ошибка во время деления: {e}")
        except Exception as e:
            raise CalculationError(f"Ошибка во время деления: {e}")

    @staticmethod
    def convert_to_direct_code(binary_number, bit_length):
        binary = bin(binary_number)[2:]
        return binary.zfill(bit_length)

    @staticmethod
    def convert_to_inverse_code(binary_number):
        ones_complement = ''.join('1' if bit == '0' else '0' for bit in binary_number[1:])
        return binary_number[0] + ones_complement

    @staticmethod
    def convert_to_additional_code(binary_number):
        ones_complement = Calculator.convert_to_inverse_code(binary_number)
        twos_complement = bin(int(ones_complement, 2) + 1)[2:]
        return twos_complement.zfill(len(binary_number[1:]))


def main():
    print("Добро пожаловать в Калькулятор для информатики!")
    stay = True
    while stay:
        try:

            while True:
                print("\nВыберите действие:")
                print("1. Перевод между системами счисления.")
                print("2. Преобразование двоичных чисел в прямой, обратный и дополнительный код.")
                print("3. Умножение двоичных чисел.")
                print("4. Деление двоичных чисел.")
                print("5. Построение таблицы истинности.")
                print("6. Анализ логического выражения.")
                print("0. Выход.")

                choice = input("Введите номер действия: ")

                if choice == "0":
                    print("До свидания!")
                    stay = False
                    break

                if choice == "1":
                    source_base = int(input("Введите исходную систему счисления (2, 8, 10, 16, 36): "))
                    target_base = int(input("Введите целевую систему счисления (2, 8, 10, 16, 36): "))

                    number = input(f"Введите число в системе счисления {source_base}: ")

                    decimal_number = int(number, source_base)

                    conversion_steps = Calculator.convert_number_step_by_step(decimal_number, source_base, target_base)
                    Calculator.display_conversion_steps(conversion_steps, target_base)

                elif choice == "2":
                    binary_number = input("Введите двоичное число: ")
                    try:
                        if all(bit in '01' for bit in binary_number):
                            bit_length = len(binary_number)

                            direct_code = Calculator.convert_to_direct_code(int(binary_number, 2), bit_length)

                            if direct_code[0] == '0':
                                inverse_code = direct_code
                                additional_code = direct_code
                            else:
                                inverse_code = Calculator.convert_to_inverse_code(direct_code)
                                additional_code = Calculator.convert_to_additional_code(direct_code)

                            print("Прямой код:", direct_code)
                            print("Обратный код:", inverse_code)
                            if '0' not in inverse_code:
                                print("При -0, дополнительный код не существует.")
                            else:
                                print("Дополнительный код:", additional_code)

                        else:
                            print("Пожалуйста, введите двоичное число")
                    except ValueError:
                        print("Ошибка: Введите корректное двоичное число.")

                elif choice == "3":
                    num1 = int(input("Введите первое двоичное число: "), 2)
                    num2 = int(input("Введите второе двоичное число: "), 2)
                    Calculator.binary_multiply_with_steps(num1, num2)

                elif choice == "4":
                    dividend = int(input("Введите делимое двоичное число: "), 2)
                    divisor = int(input("Введите делитель двоичное число: "), 2)
                    Calculator.binary_divide_with_steps(dividend, divisor)

                elif choice == "5":
                    expression = input("Введите логическое выражение: ")
                    header, rows = Calculator.build_truth_table(expression)
                    Calculator.print_truth_table(header, rows)

                elif choice == "6":
                    expression = input("Введите логическое выражение: ")
                    logic_parser = Calculator.LogicExpressionParser()
                    variables, expression_structure = logic_parser.analyze_logic_expression(expression)
                    print("Переменные:", variables)
                    print("Структура выражения:", expression_structure)
                else:
                    print("Некорректный выбор. Пожалуйста, введите правильный номер действия.")

        except InvalidInputError as inputexept:
            print(f"Некорректный ввод: {inputexept.message}, введите пожалуйста значение корректно.")
        except CalculationError as e:
            print(f"Ошибка во время вычислений: {e.message}. Пожалуйста, проверьте введенные данные.")
        except ValueError as e:
            print(f"Ошибка: {e}. Введите корректные данные.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}. Пожалуйста, проверьте введенные данные.")


if __name__ == "__main__":
    main()
