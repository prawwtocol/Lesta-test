
def isEvenRemainder(value: int) -> bool:
    """
    Check if the given value is even using remainder.

    Args:
        value: An integer value.

    Returns:
        True if the value is even, False otherwise.
    """
    return value % 2 == 0


def isEvenBitwise(value: int) -> bool:
    """
    Check if the given value is even using bitwise operations.

    Args:
        value: An integer value.

    Returns:
        True if the value is even, False otherwise.
    """
    return not (value & 1)

