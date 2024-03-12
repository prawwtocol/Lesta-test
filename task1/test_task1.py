"""
This module contains unit tests for the functions in the 'task1' module.

The 'test_even' function tests the 'isEvenRemainder'
and 'isEvenBitwise' functions
for even numbers, while the 'test_odd' function tests them for odd numbers.
"""

import task1


def test_even() -> None:
    assert task1.isEvenRemainder(2) == task1.isEvenBitwise(2)
    assert task1.isEvenRemainder(4) == task1.isEvenBitwise(4)
    assert task1.isEvenRemainder(0) == task1.isEvenBitwise(0)
    assert task1.isEvenRemainder(-6) == task1.isEvenBitwise(-6)
    assert task1.isEvenRemainder(236748) == task1.isEvenBitwise(236748)


def test_odd() -> None:
    assert task1.isEvenRemainder(3) == task1.isEvenBitwise(3)
    assert task1.isEvenRemainder(5) == task1.isEvenBitwise(5)
    assert task1.isEvenRemainder(-12347) == task1.isEvenBitwise(-12347)
    assert task1.isEvenRemainder(1234449) == task1.isEvenBitwise(1234449)
