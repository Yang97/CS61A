""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    temp = b
    while a % b != 0:
        temp = a % b
        a = b
        b = temp
    return temp

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    def ret(n, number):
        print(n)
        if n == 1:
            return number
        elif n % 2 == 0:
            return ret(n // 2, number + 1)
        else:
            return ret(3*n + 1, number + 1)
    return ret(n, 1)