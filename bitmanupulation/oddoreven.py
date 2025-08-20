def oddOReven(n: int) -> bool:
    """
    Function to check if a number is odd or even using bit manipulation.

    :param n: Integer number to check
    :return: True if odd, False if even
    """
    return (n & 1) == 1


n = int(input("Enter a number: "))
if oddOReven(n):
    print(f"{n} is odd")
else:
    print(f"{n} is even")
