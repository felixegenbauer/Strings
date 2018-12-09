# Substring search
# Author: TODO: ???

BOOKS = "Some books are to be tasted, others to be swallowed, and some few to be chewed and digested."


def naive_search(a_pattern, a_text):
    """
    >>> naive_search("to", BOOKS)
    15
    >>> naive_search(".", BOOKS)
    91
    >>> naive_search("!", BOOKS)

    """
    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
