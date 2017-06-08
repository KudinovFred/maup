import attr, inspect
from collections import namedtuple
#named tuple
# boilerplate
#  Attrs


x = lambda x : 4*x+1

print(x.__repr__())
print(x.__str__())


@attr.s
class SomeClass(object):
     a_number = attr.ib(default=2)
     list_of_numbers = attr.ib(default=attr.Factory(list))

     def hard_math(self, another_number):
         return self.a_number + sum(self.list_of_numbers) * another_number

y = SomeClass(1,[1,2,3])

y.hard_math(1)


C = attr.make_class("C", ["a", "b"])
C("foo", "bar")




from attr import attrs, attrib

@attr.s
class Coordinates(object):

     y = attr.ib()
     x = attr.ib(default=1)
     z = attr.ib(init=False, default=3)


@attrs
class SeriousCoordinates(object):
     x = attrib()
     y = attrib()

s = Coordinates(y="y", x="x")
print(s.x, s.y, s.z)

class SubClass(Coordinates):
    def __init__(self, f):
        Coordinates.__init__(self, y = "y")
        self.f = f

some = SubClass(f = 123)
print(some.__dict__)

@attrs
class SubClass(Coordinates):
    f = attrib(default="f")


some = SubClass(y = "y")
print(some.y,some.f)

print(attr.asdict(SubClass(y = "y")))
print(SubClass(y = "y").__dict__)
assert attr.asdict(SubClass(y = "y")) == SubClass(y = "y").__dict__





@attrs
class UserList:
     users = attrib()

@attr.s
class User(object):
    email = attrib()
    password = attrib()

users = [
    User("jane@doe.invalid", 1234),
    User("joe@doe.invalid", 4321)
]

filter = lambda attr, val: attr.name != "password"

p = attr.asdict(UserList(users),filter=filter)
print(p)

print({'users': [{'email': 'jane@doe.invalid'}, {'email': 'joe@doe.invalid'}]})

filter = attr.filters.exclude(attr.fields(User).password, str)
filter = attr.filters.exclude(str)

p = attr.asdict(UserList(users),filter=filter)
print(p)


@attr.s
class C(object):
    x = attr.ib(default=1)
    y = attr.ib()

    @y.default
    def name_does_not_matter(self):
        return self.x + 1

    @y.validator
    def check(self, attribute, value):
        if value > 42:
            raise ValueError(attribute.name, value, "y must be smaller or equal to 42")



print(C(x=2, y=2))

try:
    print(C(45))
except ValueError:
    print("ValueError")




def x_smaller_than_y(instance, attribute, value):
    if value >= instance.y:
        raise ValueError("'x' has to be smaller than 'y'!")

@attr.s
class C(object):

    x = attr.ib(
        validator=[
            attr.validators.instance_of(int),
            x_smaller_than_y
        ]
    )

    y = attr.ib()

try:
    C(x=3, y=4)
except ValueError:
    print("ValueError 1")

try:
    C(x="3", y=4)

except TypeError:
    print("ValueError 2 type")

try:
    C(x=4, y=3)
except ValueError:
    print("ValueError 3")

attr.set_run_validators(False)

i = C(4, 5)
i.x = 5  # works, no magic here
try:
    attr.validate(i)
except ValueError:
    print("ValueError 4")

attr.set_run_validators(True)

try:
    attr.validate(i)
except ValueError:
    print("ValueError 5")



@attr.s
class C(object):
    x = attr.ib(convert=int)
o = C("1")
print(o.x)



@attr.s
class C1(object):
    x = attr.ib()
    y = attr.ib()

# named tupple
C2 = attr.make_class("C2", ["x","y"])
assert attr.fields(C1) == attr.fields(C2), (attr.fields(C1) ,"_____", attr.fields(C2))

C3 = attr.make_class("C3", {"x":attr.ib(),"y":attr.ib()})
assert attr.fields(C1) == attr.fields(C3), (attr.fields(C1) ,"_____", attr.fields(C3))


#class and subclass

@attr.s
class D(object):
    z = attr.ib()
    x = attr.ib(default=31)


    def __eq__(self, other):
       return True  # arbitrary example



# create subclass of D,   cmp - false as it is subcass

C = attr.make_class("C", {"y":attr.ib(12)}, bases=(D,), cmp=False)

assert isinstance(C(1, x="x", y=321), D)

c = C(1, x = 789, y =64)













print(inspect.getsource(C.__init__))

"""
@y.default
    def name_does_not_matter(self):
        return self.x + 1
"""


@attr.s
class C(object):
    x = attr.ib()
    y = attr.ib()
    z = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.z = self.x + self.y


obj = C(x=1, y=2)

print(obj)


@attr.s
class C(object):
    user = attr.ib()
    password = attr.ib(repr=False)

x = C("me", "s3kr3t")
print(x)
print(x.user)
print(x.password)



