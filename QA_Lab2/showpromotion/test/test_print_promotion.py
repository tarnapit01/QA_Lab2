import pytest
from source.print_promotion import print_promotion


def test_print_promotion_499():
    result = print_promotion(499)
    assert result == "Thank you and see you next time"

def test_print_promotion_630():
    result = print_promotion(630)
    assert result == "Free ice cream cone = 1"

def test_print_promotion_null():
    result = print_promotion("null")
    assert result == "Input must be positive number"

def test_print_promotion_negative():
    result = print_promotion(-1)
    assert result == "Input must be positive number"

def test_print_promotion_703():
    result = print_promotion(703)
    assert result == "Free chocolate cake = 1"

def test_print_promotion_1260():
    result = print_promotion(1260)
    assert result == "Free ice cream cone = 1 and Free chocolate cake = 1"

def test_print_promotion_1899():
    result = print_promotion(1899)
    assert result == "Free ice cream cone = 2 and Free chocolate cake = 1"

def test_print_promotion_2245():
    result = print_promotion(2245)
    assert result == "Free ice cream cone = 1 and Free chocolate cake = 2"

def test_print_promotion_3000():
    result = print_promotion(3000)
    assert result == "Free ice cream cone = 2 and Free chocolate cake = 2"

def test_print_promotion_one_hundred():
    result = print_promotion("one hundred")
    assert result == "Input must be positive number"


def test_print_promotion_1_hundred():
    result = print_promotion("1 hundred")
    assert result == "Input must be positive number"




