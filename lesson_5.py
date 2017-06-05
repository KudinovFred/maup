class Person(object):
    pass

obj1=Person()


def some():
    print("any")
    pass

Person.some = some


obj2=Person()
print(obj2)



class Vector(list):

    def __mul__(self, other):
        return sum([x*y for x,y in zip (self,other)])



l1 = Vector([1,2,3])
print(l1)


m = [[0.5,0,0,0,0],
     [1,0.5,0,0,0],
     [1,1,0.5,0,0,],
     [1,1,1,0.5,0],
     [1,1,1,1,0.5,]]

n = [[1,-1,-1,-1,-1],
     [1,1,-1,-1,-1],
     [1,1,1,-1,-1],
     [1,1,1,1,-1],
     [1,1,1,1,1]]

class Matrix(list):

    def transp(self):
        return Matrix(list(zip(*self)))

    def __MxV(self, lst):
        return [Vector(l1)*Vector(lst) for lst in self]

    def __mul__(self, other):
        return Matrix([self.__MxV(lst) for lst in other.transp()])


M = Matrix(m)
N = Matrix(n)
print(N)
print(N.transp())

c = N*M
print(c)