
import functools
import operator

def factorial(n):
    """Factorial of a number.

    >>> factorial(0)
    1

    >>> factorial(1)
    1

    >>> factorial(5)
    120

    >>> factorial(10)
    3628800

    """

    if n == 0:
        return 1

    return functools.reduce(operator.mul, range(1, n+1))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)