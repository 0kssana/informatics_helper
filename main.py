from itertools import product
from prettytable import PrettyTable
import re


class CalculatorError(Exception):
    """
    Base exception class for errors that may occur during calculations.

    This class inherits from the built-in `Exception` class.

    :return: An instance of CalculatorError.
    :rtype: CalculatorError
    """
    pass


class InvalidInputError(CalculatorError):
    """
    Exception raised when an invalid input is detected in the calculator.

    :param message: The error message (default is "Invalid input").
    :type message: str

    :ivar message: The error message that can be provided when creating an object.
    :type message: str

    .. note::
       This exception is inherited from `CalculatorError`.

    """
    def __init__(self, message="Некорректный ввод"):
        """
        Initializes the InvalidInputError object.

        :param message: The error message (default is "Invalid input").
        :type message: str
        """
        self.message = message
        super().__init__(self.message)



class CalculationError(CalculatorError):
    """
    Exception raised when an error occurs during calculations in the calculator.

    :param message: The error message (default is "Error during calculations").
    :type message: str

    :ivar message: The error message that can be provided when creating an object.
    :type message: str

    .. note::
       This exception is inherited from `CalculatorError`.
    """
    def __init__(self, message="Ошибка во время вычислений."):
        """
        Initializes the CalculationError object.

        :param message: The error message (default is "Error during calculations").
        :type message: str
        """
        self.message = message
        super().__init__(self.message)
   

class Calculator:
    """
    Utility class providing various mathematical and binary operations.

    """
    
    class LogicExpressionParser:
        """
        Parses logic expressions, extracting variables and their relationships.

        :ivar operators: Set of supported logical operators {'and', 'or', 'not'}.
        :type operators: set

        :ivar variables: Set of variables encountered in the logic expression.
        :type variables: set

        :ivar expression_structure: List representing the structure of the logic expression.
                                Each element is a tuple ('Type', 'Value').
                                Type can be 'Оператор' for operators or 'Скобка' for parentheses.
        :type expression_structure: list

        """
        def __init__(self):
            """
            Initializes a LogicExpressionParser object.
            """
            self.operators = {'and', 'or', 'not'}
            self.variables = set()
            self.expression_structure = []

        def analyze_logic_expression(self, expression):
            """
            Analyzes the provided logic expression, extracting variables and expression structure.

            :param expression: The logic expression to be analyzed.
            :type expression: str

            :return: A tuple containing the set of variables and the expression structure.
            :rtype: tuple
            """
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
            """
            Processes a token in the logic expression.

            :param token: The token to be processed.
            :type token: str
            """
            if token.lower() in self.operators:
                self.expression_structure.append(('Оператор', token.lower()))
            else:
                self.variables.add(token)

        def process_char(self, char):
            """
            Processes a character in the logic expression.

            :param char: The character to be processed.
            :type char: str
            """
            if char in {'(', ')'}:
                self.expression_structure.append(('Скобка', char))

    @staticmethod
    def convert_number_step_by_step(num, from_base, to_base):
        """
        Converts a number from one base to another with step-by-step display.

        :param num: The number to be converted.
        :type num: int
        :param from_base: The base of the original number.
        :type from_base: int
        :param to_base: The desired base for the result.
        :type to_base: int

        :return: A list of tuples representing the conversion steps.
                 Each tuple has the format (current_number, quotient, remainder).
        :rtype: list of tuples

        :raises InvalidInputError: If the input bases are not within the supported range (2 to 36).
        """
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
        """
        Displays the steps of a conversion process.

        :param steps: List of tuples representing conversion steps.
                      Each tuple has the format (dividend, quotient, remainder).
        :type steps: list of tuples
        :param result_base: The base of the result.
        :type result_base: int

        :return: The result of the conversion.
        :rtype: str
        """
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
        """
        Builds a truth table for a logical expression.

        :param expression: The logical expression to build the truth table for.
        :type expression: str

        :return: A tuple containing the header (variable names and expression) and rows of the truth table.
        :rtype: tuple
        """
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
        """
        Prints a truth table.

        :param header: List of column headers.
        :type header: list
        :param rows: List of rows in the truth table.
        :type rows: list
        """
        table = PrettyTable(header)
        table.align = "c"

        for row in rows:
            table.add_row(row)

        print(table)

    @staticmethod
    def binary_multiply_with_steps(a, b):
        """
        Performs binary multiplication with step-by-step display.

        :param a: The first binary number.
        :type a: int
        :param b: The second binary number.
        :type b: int

        :return: The result of the binary multiplication.
        :rtype: int
        """
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
        """
        Performs binary division with step-by-step display.

        :param dividend: The dividend in binary.
        :type dividend: int
        :param divisor: The divisor in binary.
        :type divisor: int

        :return: The quotient of the binary division.
        :rtype: int

        :raises CalculationError: If there is an error during the division.
        """
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
        """
        Converts a binary number to direct code.

        :param binary_number: The binary number to be converted.
        :type binary_number: int
        :param bit_length: The desired bit length of the direct code.
        :type bit_length: int

        :return: The direct code representation of the binary number.
        :rtype: str
        """
        binary = bin(binary_number)[2:]
        return binary.zfill(bit_length)

    @staticmethod
    def convert_to_inverse_code(binary_number):
        """
        Converts a binary number to inverse code.

        :param binary_number: The binary number to be converted.
        :type binary_number: str

        :return: The inverse code representation of the binary number.
        :rtype: str
        """
        ones_complement = ''.join('1' if bit == '0' else '0' for bit in binary_number[1:])
        return binary_number[0] + ones_complement

    @staticmethod
    def convert_to_additional_code(binary_number):
        """
        Converts a binary number to additional code.

        :param binary_number: The binary number to be converted.
        :type binary_number: str

        :return: The additional code representation of the binary number.
        :rtype: str
        """
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
