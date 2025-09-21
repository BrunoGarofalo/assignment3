
class Operations():

    @staticmethod
    def addition(a: float, b: float) -> float: #what comes in is a decimal, what is return is a decimal
        return a+b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def division(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")  # This sends an error message when someone tries to divide by zero.
        return a / b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        return a * b