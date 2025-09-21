from app.operations import Operations
import pytest
from typing import Union  # Import Union for type hinting multiple possible types


# Define a type alias for numbers that can be either int or float
Number = Union[int, float]

# ---------------------------------------------
# Unit Tests for the 'addition' Method
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),           # Test adding two positive integers
        (0, 0, 0),           # Test adding two zeros
        (-3, 1, -2),          # Test adding a negative and a positive integer
        (3.5, 3.5, 7.0),     # Test adding two positive floats
        (-2.5, 0.5, -2.0),    # Test adding a negative float and a positive float
        (0, 1.0, 1.0)           # Test adding a zero and a positive float
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_zeros",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
        "add_zero_and_positive_float",
    ]
)


def test_addition(a: Number, b: Number, expected: Number) -> None:
    result = Operations.addition(a, b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'subtraction' Method
# --------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 3, 0),           # Test subtracting a smaller positive integer from a larger one
        (0, 0, 0),           # Test subtracting two zeros
        (-1, -2, 1),        # Test subtracting a negative integer from another negative integer
        (8.5, 5.5, 3.0),    # Test subtracting two positive floats
        (-10.5, -5.5, -5.0), # Test subtracting two negative floats
        (0, -1.0, 1.0)      # Test subtracting zero from negative float
    ],
    ids=[
        "subtract_smaller_positive_integer_from_larger",
        "subtract_two_zeros",
        "subtract_negative_integer_from_negative_integer",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_zero_negative_floats",
    ]
)

def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    result = Operations.subtraction(a, b)
    assert result == expected, f"Expected subtraction({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'division' Method
# --------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Test dividing two positive integers
        (-6, -3, 2.0),         # Test dividing two negative integers
        (-6.0, 3.0, -2.0),     # Test dividing a negative float by a positive float
        (0, 5, 0.0),            # Test dividing zero by a positive integer
        (6.0, 3.0, 2.0),       # Test dividing two positive floats
        (-1, 2, -0.5)           # Test dividing a negative integer by a positive integer
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_two_negative_integers",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
        "divide_two_positive_floats",
        "divide_negative_integer_positive_integer",
    ]
)

def test_division(a: Number, b: Number, expected: Number) -> None:
    result = Operations.division(a, b)
    assert result == expected, f"Expected division({a}, {b}) to be {expected}, but got {result}"




# ---------------------------------------------
# Negative Test Case: Division by Zero
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),    # Test dividing by zero with positive dividend
        (-1, 0),   # Test dividing by zero with negative dividend
        (0, 0),    # Test dividing zero by zero
    ],
    ids=[
        "divide_positive_dividend_by_zero",
        "divide_negative_dividend_by_zero",
        "divide_zero_by_zero",
    ]
)

def test_division_by_zero(a: Number, b: Number) -> None:
    # Use pytest's context manager to check for a ValueError when dividing by zero
    with pytest.raises(ValueError, match="Division by zero is not allowed.") as excinfo:
        # Attempt to divide 'a' by 'b', which should raise a ValueError
        Operations.division(a, b)

    # Assert that the exception message contains the expected error message
    assert "Division by zero is not allowed." in str(excinfo.value), \
        f"Expected error message 'Division by zero is not allowed.', but got '{excinfo.value}'"


# ---------------------------------------------
# Unit Tests for the 'multiplication' Method
# --------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 1, 0),          # Test multiplying zero with a positive integer
        (2, 2, 4),           # Test multiplying two positive integers
        (-2, -4, 8),         # Test multiplying two negative integers
        (2.5, 1.0, 2.5),    # Test multiplying two positive floats
        (-2.5, 1.0, -2.5),  # Test multiplying a negative float with a positive float
        (0, -1.5, 0)        #Test multiplying 0 with negative float
    ],
    ids=[
        "multiply_zero_with_positive_integer",
        "multiply_two_positive_integers",
        "multiply_two_negative_integers",
        "multiply_two_positive_floats",
        "multiply_negative_float_with_positive_float",
        "multiply_zero_with_negative_float",
    ]
)

def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    result = Operations.multiplication(a, b)
    assert result == expected, f"Expected multiplication({a}, {b}) to be {expected}, but got {result}"