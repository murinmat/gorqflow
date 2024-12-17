import pytest
from gorqflow.playtools import add_one, sub_one, divide


def test_add_one():
    assert add_one(1) == 2


def test_sub_one():
    assert sub_one(1) == 0


def test_divide_ok():
    assert divide(15., 3.) == 5.


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(15., 0.)
