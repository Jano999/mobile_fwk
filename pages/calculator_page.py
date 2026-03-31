from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CalculatorPage(BasePage):
    """
    Page Object for Motorola Calculator.

    Attributes:
        DIGIT (str): Template for digit button IDs (0-9).
        OPERATOR (dict): Mapping of operator symbols to their resource IDs.
        EQUALS (tuple): Locator for the "=" button.
        RESULT (tuple): Locator for the display showing calculation result.
    """

    # Basic selectors
    DIGIT = "com.motorola.cn.calculator:id/digit_{}"  # digits 0-9
    OPERATOR = {
        "+": "com.motorola.cn.calculator:id/op_add",
        "-": "com.motorola.cn.calculator:id/op_sub",
        "*": "com.motorola.cn.calculator:id/op_mul",
        "/": "com.motorola.cn.calculator:id/op_div"
    }
    EQUALS = (AppiumBy.ID, "com.motorola.cn.calculator:id/eq")
    RESULT = (AppiumBy.ID, "com.motorola.cn.calculator:id/formula_or_result")

    def click_digit(self, number: int):
        """
        Clicks on a digit button.

        Args:
            number (int): A digit from 0 to 9.
        """
        locator = (AppiumBy.ID, self.DIGIT.format(number))
        self.click(locator)

    def click_operator(self, operator: str):
        """
        Clicks on an operator button.

        Args:
            operator (str): One of '+', '-', '*', '/'.

        Raises:
            ValueError: If the operator is not recognized.
        """
        if operator not in self.OPERATOR:
            raise ValueError(f"Unknown operator: {operator}")
        locator = (AppiumBy.ID, self.OPERATOR[operator])
        self.click(locator)

    def click_equals(self):
        """Clicks the '=' button."""
        self.click(self.EQUALS)

    def enter_number(self, number: int):
        """
        Enters a number by clicking its digits sequentially.

        Args:
            number (int): The number to enter.
        """
        for digit in str(number):
            self.click_digit(int(digit))

    def calculate(self, a: int, operator: str, b: int):
        """
        Performs a calculation with two numbers and an operator.

        Args:
            a (int): The first number.
            operator (str): Operator '+', '-', '*', or '/'.
            b (int): The second number.
        """
        self.enter_number(a)
        self.click_operator(operator)
        self.enter_number(b)
        self.click_equals()

    def get_result(self) -> str:
        """
        Gets the result of the last calculation.

        Returns:
            str: The calculation result as text.
        """
        return self.get_text(self.RESULT)