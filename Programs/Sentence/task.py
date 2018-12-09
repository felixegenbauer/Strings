# Word counter
# Author: TODO: ???

import doctest


def word_counter(a_text):
    """
    Counting words in a given text.

    :param a_text: text to inspect
    :type a_text: str

    :return: number of words
    :rtype: int

    >>> word_counter("")
    0
    >>> word_counter("single")
    1
    >>> word_counter(" single ")
    1
    >>> word_counter("one two three")
    3
    >>> word_counter(" one two three ")
    3
    >>> word_counter("one  two   three")
    3
    """

    return None


if __name__ == '__main__':
    doctest.testmod()

