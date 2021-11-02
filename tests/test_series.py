from math_series.series import fibonacci_series
from math_series.series import lucas_series
from math_series.series import sum_series

def test_fibonacci_series_3():
    excepted = 1
    actual = fibonacci_series(3)
    assert excepted == actual

def test_lucas_series_5():
    excepted = 7
    actual = lucas_series(5)
    assert excepted == actual

def test_sum_series_5():
    excepted = 12
    actual = sum_series(5,3,2)
    assert excepted == actual