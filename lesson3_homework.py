
def multiplication_function(number):
    """
    :param number:
    :return:

    >>> multiplication_function(1234)
    8

    >>> multiplication_function(2234)
    6
    """

    result = 1
    while True:
        while number :
            number, x = divmod(number,10)
            if x:
                result*= x

        if result >=10:
            number,result=result,1
            continue

        return result


def factorial(n):
    """
    >>> factorial(5)
    120
    >>> factorial(6)
    720
    """
    result = 1
    for i in range(n):
        result*=i+1
    return result

def some_generator(n):
    for i in range(n):
        yield i*i

for i in some_generator(10):
    print (i)

def polinom(x, some_list):
    """
    >>> polinom(5,[3,4])
    19

    >>> polinom(5,[1,4,6])
    51

    >>> polinom(1,[1,1,1,1])
    4

    >>> polinom(5,[4])
    4

    >>> polinom(0,[5,7,8,4])
    4
    """

    result=0
    stepen=len(some_list)-1

    for i in some_list:
        result+=i*(x**stepen)
        stepen-=1
    return result


def text_modifier(function):
    def decorator(text):

        text = text+"!!!!!!!!"
        function(text)

        print("some more")

    return decorator



@text_modifier
def simple_function(text):
    print(text)


simple_function("hollaa")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)






