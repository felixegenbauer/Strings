# Characters and Unicode points
# Author: TODO: ???


def print_ord_range(a_start, a_stop):
    """
    >>> print_ord_range("Z", "a")
    Z [ \ ] ^ _ ` a
    >>> print_ord_range("9", "A")
    9 : ; < = > ? @ A
    >>> print_ord_range(57, 65)
    9 : ; < = > ? @ A
    >>> print_ord_range(57, 35)
    <BLANKLINE>
    >>> print_ord_range(57.0, 65)
    Traceback (most recent call last):
      ...
    ValueError: Range variable must be string (char) or integer.
    """
    text = ""
    print(text.strip())


def print_chr_matrix(a_start, a_stop):
    """
    >>> print_chr_matrix(101, 120)
    100 e f g h i j k l m n
    110 o p q r s t u v w x
    >>> print_chr_matrix("G", "Z")
    70 G H I J K L M N O P
    80 Q R S T U V W X Y Z
    >>> print_chr_matrix(32, 126)
    030     ! " # $ % & ' (
    040 ) * + , - . / 0 1 2
    050 3 4 5 6 7 8 9 : ; <
    060 = > ? @ A B C D E F
    070 G H I J K L M N O P
    080 Q R S T U V W X Y Z
    090 [ \ ] ^ _ ` a b c d
    100 e f g h i j k l m n
    110 o p q r s t u v w x
    120 y z { | } ~
    """

    text = ""
    print(text.strip())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
