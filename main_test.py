import pytest
import builtins
import builtins
from main import Calculator, CalculationError


def test_convert_number_step_by_step():
    conversion_steps = Calculator.convert_number_step_by_step(int("1011", 2), 2, 8)
    result = Calculator.display_conversion_steps(conversion_steps, 8)
    assert result == "13"

    conversion_steps = Calculator.convert_number_step_by_step(int("FF", 16), 16, 10)
    result = Calculator.display_conversion_steps(conversion_steps, 10)
    assert result == "255"

    conversion_steps = Calculator.convert_number_step_by_step(int("11001", 2), 2, 16)
    result = Calculator.display_conversion_steps(conversion_steps, 16)
    assert result == "19"

    conversion_steps = Calculator.convert_number_step_by_step(int("35", 8), 8, 10)
    result = Calculator.display_conversion_steps(conversion_steps, 10)
    assert result == "29"

    conversion_steps = Calculator.convert_number_step_by_step(int("101", 2), 2, 10)
    result = Calculator.display_conversion_steps(conversion_steps, 10)
    assert result == "5"

    conversion_steps = Calculator.convert_number_step_by_step(int("123", 10), 10, 8)
    result = Calculator.display_conversion_steps(conversion_steps, 8)
    assert result == "173"

    conversion_steps = Calculator.convert_number_step_by_step(int("ABC", 16), 16, 10)
    result = Calculator.display_conversion_steps(conversion_steps, 10)
    assert result == "2748"

    conversion_steps = Calculator.convert_number_step_by_step(int("2748", 10), 10, 16)
    result = Calculator.display_conversion_steps(conversion_steps, 16)
    assert result == "ABC"

    conversion_steps = Calculator.convert_number_step_by_step(int("100", 2), 2, 8)
    result = Calculator.display_conversion_steps(conversion_steps, 8)
    assert result == "4"

    conversion_steps = Calculator.convert_number_step_by_step(int("40", 10), 10, 2)
    result = Calculator.display_conversion_steps(conversion_steps, 2)
    assert result == "101000"

    conversion_steps = Calculator.convert_number_step_by_step(int("101000", 2), 2, 10)
    result = Calculator.display_conversion_steps(conversion_steps, 10)
    assert result == "40"


def test_convert_to_direct_code():
    bit_length = len("1010")
    direct_code = Calculator.convert_to_direct_code(int("1010", 2), bit_length)
    inverse_code = Calculator.convert_to_inverse_code(direct_code)
    additional_code = Calculator.convert_to_additional_code(direct_code)
    assert direct_code == "1010"
    assert inverse_code == "1101"
    assert additional_code == "1110"

    bit_length = len("10001000")
    direct_code = Calculator.convert_to_direct_code(int("10001000", 2), bit_length)
    inverse_code = Calculator.convert_to_inverse_code(direct_code)
    additional_code = Calculator.convert_to_additional_code(direct_code)
    assert direct_code == "10001000"
    assert inverse_code == "11110111"
    assert additional_code == "11111000"

    bit_length = len("10001011")
    direct_code = Calculator.convert_to_direct_code(int("10001011", 2), bit_length)
    inverse_code = Calculator.convert_to_inverse_code(direct_code)
    additional_code = Calculator.convert_to_additional_code(direct_code)
    assert direct_code == "10001011"
    assert inverse_code == "11110100"
    assert additional_code == "11110101"

    bit_length = len("10000000")
    direct_code = Calculator.convert_to_direct_code(int("10000000", 2), bit_length)
    inverse_code = Calculator.convert_to_inverse_code(direct_code)
    additional_code = Calculator.convert_to_additional_code(direct_code)
    assert direct_code == "10000000"
    assert inverse_code == "11111111"
    assert additional_code == "100000000"  # На самом деле не существует, и это учтено в main

    bit_length = len("11111111")
    direct_code = Calculator.convert_to_direct_code(int("11111111", 2), bit_length)
    inverse_code = Calculator.convert_to_inverse_code(direct_code)
    additional_code = Calculator.convert_to_additional_code(direct_code)
    assert direct_code == "11111111"
    assert inverse_code == "10000000"
    assert additional_code == "10000001"


def test_binary_multiply_with_steps():
    result = Calculator.binary_multiply_with_steps(0b101010, 0b1101)
    assert result == 546

    result = Calculator.binary_multiply_with_steps(0b11100, 0b111)
    assert result == 196

    result = Calculator.binary_multiply_with_steps(0b111111, 0b1001)
    assert result == 567

    result = Calculator.binary_multiply_with_steps(0b1100101, 0b101010)
    assert result == 4242

    result = Calculator.binary_multiply_with_steps(0b11111, 0b1011)
    assert result == 341

    result = Calculator.binary_multiply_with_steps(0b1010101, 0b110110)
    assert result == 4590

    result = Calculator.binary_multiply_with_steps(0b1111000, 0b1101)
    assert result == 1560

    result = Calculator.binary_multiply_with_steps(0b110011, 0b1110)
    assert result == 714

    result = Calculator.binary_multiply_with_steps(0b111110, 0b101)
    assert result == 310

    result = Calculator.binary_multiply_with_steps(0b1101, 0b11011)
    assert result == 351

    result = Calculator.binary_multiply_with_steps(0b1000, 0b101)
    assert result == 40


def test_binary_divide_with_steps():
    result1 = Calculator.binary_divide_with_steps(0b1111, 0b11)
    assert result1 == 5

    result2 = Calculator.binary_divide_with_steps(0b101010, 0b1)
    assert result2 == 42

    result3 = Calculator.binary_divide_with_steps(0b100110, 0b10)
    assert result3 == 19

    result4 = Calculator.binary_divide_with_steps(0b101010101010, 0b11)
    assert result4 == 910

    try:
        Calculator.binary_divide_with_steps(0b1100, 0b0)
    except CalculationError:
        pass
    else:
        assert False, "Expected CalculationError for division by 0"

    result6 = Calculator.binary_divide_with_steps(0b100000000000000000, 0b1001)
    assert result6 == 14563

    result7 = Calculator.binary_divide_with_steps(0b0, 0b101)
    assert result7 == 0

    result8 = Calculator.binary_divide_with_steps(0b101111, 0b11)
    assert result8 == 15

    result9 = Calculator.binary_divide_with_steps(0b1100110010010001111011, 0b100000000000000000)
    assert result9 == 25


def test_build_truth_table():
    header, rows = Calculator.build_truth_table("A and B")
    expected_header = ['A', 'B', 'A and B']
    expected_rows = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    assert header == expected_header
    assert rows == expected_rows

    header, rows = Calculator.build_truth_table("A or B")
    expected_header = ['A', 'B', 'A or B']
    expected_rows = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
    assert header == expected_header
    assert rows == expected_rows

    header, rows = Calculator.build_truth_table("(A and B) or (C and not D)")
    expected_header = ['A', 'B', 'C', 'D', '(A and B) or (C and not D)']
    expected_rows = [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 1, 1, 0],
                     [0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 0, 1], [0, 1, 1, 1, 0],
                     [1, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0],
                     [1, 1, 0, 0, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1]]
    assert header == expected_header
    assert rows == expected_rows


def test_analyze_logic_expression():
    logic_parser = Calculator.LogicExpressionParser()
    variables, expression_structure = logic_parser.analyze_logic_expression("A and B or C or not D")
    assert variables == {'A', 'B', 'C', 'D'}
    assert expression_structure == [('Оператор', 'and'), ('Оператор', 'or'), ('Оператор', 'or'), ('Оператор', 'not')]

    logic_parser = Calculator.LogicExpressionParser()
    variables, expression_structure = logic_parser.analyze_logic_expression("A or B")
    assert variables == {'A', 'B'}
    assert expression_structure == [('Оператор', 'or')]

    logic_parser = Calculator.LogicExpressionParser()
    variables, expression_structure = logic_parser.analyze_logic_expression("(A and not B) or (C or not D) or not E "
                                                                            "and (F or E) and (E and J)")
    assert variables == {'A', 'B', 'C', 'D', 'E', 'F', 'J'}
    assert expression_structure == [('Скобка', '('), ('Оператор', 'and'), ('Оператор', 'not'),
                                    ('Скобка', ')'), ('Оператор', 'or'), ('Скобка', '('), ('Оператор', 'or'),
                                    ('Оператор', 'not'), ('Скобка', ')'), ('Оператор', 'or'), ('Оператор', 'not'),
                                    ('Оператор', 'and'), ('Скобка', '('), ('Оператор', 'or'), ('Скобка', ')'),
                                    ('Оператор', 'and'), ('Скобка', '('), ('Оператор', 'and'),
                                    ('Скобка', ')')]
