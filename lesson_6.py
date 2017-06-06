class Person:
    def __init__(self, name = "Vasya", sex = "M", age  = 13 ):
        self.name = name
        self.sex=sex
        self.age = age


class Citizen(Person):
    def __init__(self, nation = "Ukrainian", **kwargs):
        self.nation = nation

        #super(Citizen, self).__init__()
        Person.__init__(self)


        self.__dict__.update(kwargs)
        #vars(self).update(kwargs)


        #todo not done till end
        #for key in self.__dict__:
        #   setattr(self, key, self.__dict__[key])




a = Citizen(nation="foo", name="bar", sex = "buzz", some="123")

print(a.name)
print(a.sex)
print(a.age)
print(a.nation)
#print(a.some)


def my_funct(a=2,b=3):
    print(locals())

    return a+b

print("_____________________")

print(my_funct.__dict__)
print(my_funct.__class__)
#print(my_funct.__bases__)


my_funct(1,2)

x= my_funct
x(1,3)
print(x(4,5))




count = 0

def counter(funct):
    def wrapper(*args, **kwargs):
        global count
        count +=1
        print(count)
        return funct(*args, **kwargs)
    return wrapper

@counter
def myname(x = "some"):
    print("Masha", x)

myname("hjkj")
myname("lkju890")
myname("1234")
myname()



print(Citizen.__bases__)
print(Citizen.__dict__)

print(type.__class__)
print(type(a))



# create meta class based on type

class MetaPerson(type):

    def __call__(cls, *args, **kwargs):

        obj= type.__call__(cls, *args)
        obj.__dict__.update(kwargs)

        return obj

# create  class based on metaclass

class Man(metaclass=MetaPerson):
    pass

#єкземпляр класса
m = Man(height = 180, weight = 80)

print(m.__dict__)
print(m.height)







# влияние на метод метакласа prepare
class Meta(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        return super().__prepare__(metacls)

    def __new__(metacls, name, bases, namespace):
        return super().__new__(metacls, name, bases, namespace)

    def __init__(cls, name, bases, namespace):
        print("Init in Metaclsass")

    def __call__(cls, *args, **kwargs):
        return super().__call__()


# распечатать что там находится

class Class (metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.args = args
        self.__dict__.update(kwargs)

a = Class()