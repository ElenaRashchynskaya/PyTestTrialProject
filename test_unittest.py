import unittest
import allure
import pytest


@allure.feature('Calculate')
@allure.story('Calculate two numbers')
def calculate(a, b, operator):
    with allure.step('Selected operator: ' + operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b != 0:
                return a / b
            else:
                return "Division by zero is not allowed"
        else:
            return "Unsupported operator"


class TestCalculate(unittest.TestCase):
    @pytest.mark.critical
    def test_addition(self):
        self.assertEqual(calculate(5, 3, '+'), 8)

    @pytest.mark.critical
    def test_subtraction(self):
        self.assertEqual(calculate(5, 3, '-'), 2)

    @pytest.mark.critical
    def test_multiplication(self):
        self.assertEqual(calculate(5, 3, '*'), 15)

    @pytest.mark.normal
    def test_division(self):
        self.assertEqual(calculate(6, 3, '/'), 2)
        self.assertEqual(calculate(5, 0, '/'), "Division by zero is not allowed")

    @pytest.mark.minor
    def test_invalid_operator(self):
        self.assertEqual(calculate(5, 3, '%'), "Unsupported operator")
