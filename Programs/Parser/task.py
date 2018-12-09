# LZK parser
# Author: TODO: ???


def get_course_number(a_text):
    """
    Gets course number from course header in LZK.

    :param a_text: with course number type and name
    :type a_text: str

    :return: course number
    :rtype: int

    >>> get_course_number("703410 VO/1 VO Introduction into Programming with Python")
    703410
    >>> get_course_number(" 703410 VO/1 VO Introduction into Programming with Python")
    703410
    >>> get_course_number("703412 PS/2 PS Introduction into Programming with Python")
    703412
    """
    return


def show_url(a_number, a_semester="18W"):
    """
    Generates web-page address for a course of a given number.

    :param a_number: course number
    :type a_number: int

    :param a_semester: semester, default 18W
    :type a_semester: str

    :return: url of the course
    :rtype: str

    >>> show_url(703410)
    'https://orawww.uibk.ac.at/public_prod/owa/lfuonline_lv.details?sem_id_in=18W&lvnr_id_in=703410'
    >>> show_url(703412)
    'https://orawww.uibk.ac.at/public_prod/owa/lfuonline_lv.details?sem_id_in=18W&lvnr_id_in=703412'
    """
    return


if __name__ == '__main__':
    import doctest
    doctest.testmod()
