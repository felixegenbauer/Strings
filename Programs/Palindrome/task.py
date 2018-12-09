# Palindrome
# Author: TODO ???


def is_palindrome(a_text):
    """
    >>> is_palindrome("a")
    True
    >>> is_palindrome("madam")
    True
    >>> is_palindrome("Anna")
    True
    >>> is_palindrome("race car")
    True
    >>> is_palindrome(1)
    True
    >>> is_palindrome(10201)
    True
    >>> is_palindrome(10.01)
    True
    >>> is_palindrome("A man, a plan, a canal? Panama!")
    True
    >>> is_palindrome([1, 0, 2, 0, 1])  # list
    True
    >>> is_palindrome((1, 0, 1))  # tuple, a constant list
    True

    >>> is_palindrome("te")
    False
    >>> is_palindrome("A man, a plan, a canal? O Panama!")
    False
    >>> is_palindrome(True)
    False
    >>> is_palindrome(None)
    False

    >>> is_palindrome({1: 2, 2: 0, 3: 2})  # dictionary, unordered
    Traceback (most recent call last):
        ...
    TypeError: Dictionary is not ordered and can not be used the argument
    >>> is_palindrome({1, 0, 1})  # set, unordered
    Traceback (most recent call last):
        ...
    TypeError: Set not ordered and can not be used the argument
    """
    return True  # TODO: replace this with your code


if __name__ == '__main__':
    import doctest
    doctest.testmod()
