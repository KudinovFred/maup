"""
from ctypes import windll

beep = windll.kernel32.Beep(500,1000)
beep
print(beep)


numlock = 0x90
x = windll.kernel32.GetKeyState(numlock)
print(x)
"""


def add(a,b):
    '''
    my function ololo  
    
    :param a: 1 st arg 
    :param b: 2 nd arg
    :return: summa
    '''
    print (__name__)
    return a+b


if __name__ == "__main__":
    print(add(2,4))
    print("aloha")