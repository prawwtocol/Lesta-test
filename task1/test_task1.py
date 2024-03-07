import task1

# todo test performance on self


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
