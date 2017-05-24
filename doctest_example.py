def compare_numbers(a,b):

    """
    :param a: 
    :param b: 
    :return: 
    
    >>> compare_numbers(3,2)
    1
    >>> compare_numbers(2,2)
    0
    >>> compare_numbers(2,3)
    -1
    """

    if a > b: return 1
    elif a<b :return -1
    else: return 0

print(1)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    assert compare_numbers(3,2) == 1
    assert compare_numbers(2, 2) == 0
    assert compare_numbers(3, 2) == -1



