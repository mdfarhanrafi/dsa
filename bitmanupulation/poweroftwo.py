def powerOfTwo(n: int) -> bool:
    """
    Check if a number is a power of two.

    A number is a power of two if it is greater than zero and has only one bit set in its binary representation.

    :param n: The number to check.
    :return: True if n is a power of two, False otherwise.
    """
    return n > 0 and (n & (n - 1)) == 0
