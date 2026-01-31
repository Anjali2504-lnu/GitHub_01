from src.calculator import fun1, fun2, fun3, fun4

def test_fun1():
    assert fun1(2, 3) == 5

def test_fun2():
    assert fun2(5, 3) == 2

def test_fun3():
    assert fun3(4, 3) == 12

def test_fun4():
    assert fun4(2, 3) == (2 + 3) + (2 - 3) + (2 * 3)

# Example of parametrized test (optional)
# import pytest
#
# @pytest.mark.parametrize(
#     "x, y, expected",
#     [(1, 2, 3), (5, 5, 10), (-1, 1, 0)]
# )
# def test_fun1_param(x, y, expected):
#     assert fun1(x, y) == expected
