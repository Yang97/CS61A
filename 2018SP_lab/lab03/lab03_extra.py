""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def ret(times, number):
        if times == 0:
            return number
        for x in range(1, times+1):
            if x % 3 == 1:
                number = f1(number)
            elif x % 3 == 2:
                number = f2(number)
            else:
                number = f3(number)
        return number
    return lambda x: lambda y: ret(x, y)

## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: 10 * y + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def prime(n, index, number):
        if index == n:
            return True
        elif number >= 2:
            return False
        elif n % index == 0:
            return prime(n, index+1, number+1)
        elif n % index != 0:
            return prime(n, index+1, number)
    return prime(n, 1, 0) 

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    def caculate(n, flag, index, sum):
        if index == n + 1:
            return sum
        elif flag == 0:
            return caculate(n, 1, index+1, sum+even_term(index))
        elif flag == 1:
            return caculate(n, 0, index+1, sum+odd_term(index))
    return caculate(n, 1, 1, 0)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def the_digit_times(digit, current_value, mod, number):
        if current_value == 0:
            if mod == digit:
                return number + 1
            return number
        elif mod == digit:
            return the_digit_times(digit, current_value//10, current_value%10, number+1)
        else:
            return the_digit_times(digit, current_value//10, current_value%10, number)
    def caculate_ten_pairs(number, digit):
        if digit == 5:
            return sum(range(1, the_digit_times(5, number//10, number%10, 0)))
        else:
            return the_digit_times(digit, number//10, number%10, 0) * the_digit_times(10-digit, number//10, number%10, 0)    
    def caculate(number, result, digit):
        if digit == 6:
            return result
        else:    
            return caculate(number, result+caculate_ten_pairs(number, digit), digit+1)
    return caculate(n, 0, 1)        