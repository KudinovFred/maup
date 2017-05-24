"""

1. Программа тестирования факториала
- важно знать doctest

2. Найти функцию синус и косинус аргумента (представить вместо x)
- важно знать комплексную часть

3. Фукнкция, анализирующая беззнаковое число и формурует новое число, (вместо цифры исходного числа ставит квадрат исходного числа)

Пример: если число 1 2 3 4, то целью вашей программы должно быть 1 4 12 16


4. Оберните число
Пример: 1234 -> 4321
"""

def numb_factorial(number):
    """
    >>> numb_factorial(4)
    24

    >>> numb_factorial(5)
    120
    """
    result=1
    while number:
        result*=number
        number-=1
    return result


def square_numbers(number):
    """
    >>> square_numbers(1234)
    14916

    >>> square_numbers(1186)
    116436
    """

    new_number = ""

    for i in str(number):
        new_number += str(int(i)**2)

    return int(new_number)

def reverse_2(number):

    """
    >>> reverse_2(1234)
    14916

    >>> reverse_2(1186)
    116436
    """
    # todo  this function - is reverse

    result=""
    while number:
        number,y = divmod(number,10)
        result+=str(y)

    return result


def reverse(number):
    """
    :param number:
    :return:

    >>> reverse(1234)
    4321

    """
    return int(str(number)[::-1])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
