
"""
+
-
*
/  divide  as float
// divide to int
%  left from division 
divmod(a,b)  -  return   //  , %


**  stepen
math.sqrt()  koren

floor()
Decimal()


"""
'''
print(divmod(15,4))


def sum_of_numbers(a):
    summa = 0

    while a >0:

        a, x = divmod(a,10)
        summa+=x

    print(summa)
    return summa

sum_of_numbers(12345)


def factorial(x,n):
    res = 1
    n = 0
    
    while True:
        n+=1
'''

def fact(n):
    """
    vicislenie factoriala
    :param n: 
    :return: 
    """
    f = 1
    while n:
        f *= n
        n-=1
    print(f)
    return f

fact(4)





