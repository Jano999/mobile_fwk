import pytest
from pages.calculator_page import CalculatorPage


@pytest.mark.parametrize(
    "a, operator, b, expected",
    [
        (2, "+", 3, "5"),
        (10, "-", 4, "6"),
        (6, "*", 7, "42"),
        (8, "/", 2, "4"),
        (5, "/", 0, "Cannot divide by zero")
    ]
)
def test_calculator_operations(driver, a, operator, b, expected):
    calc = CalculatorPage(driver)
    calc.calculate(a, operator, b)
    result = calc.get_result()
    assert result == expected