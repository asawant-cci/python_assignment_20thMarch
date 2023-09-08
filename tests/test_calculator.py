import pytest
from calculator import Calculator


@pytest.mark.math
@pytest.mark.math_add
def test_add_single_digit_nums():
    result = Calculator().add_two_numbers(2, 3)
    assert result == 5, "Sum of 2+3 should be 5"


@pytest.mark.math
@pytest.mark.math_add
def test_add_two_digit_nums():
    result = Calculator().add_two_numbers(12, 10)
    assert result == 22, "Sum of 12+10 should be 22"


@pytest.mark.math
@pytest.mark.math_multiply
def test_multiply_single_digit_nums():
    result = Calculator().multiply_two_numbers(2, 3)
    assert result == 6, "result of 2*3 should be 22"


@pytest.mark.math
@pytest.mark.math_multiply
def test_multiply_two_digit_nums():
    result = Calculator().multiply_two_numbers(20, 30)
    assert result == 600, "result of 20*30 should be 600"
