# если в классе явно указан параметр, а в объекте нет
# параметр объекта будет меняться при изменении параметра в классе

class Person:
    name = "name_class"
    some = "Some_class"
    def __init__(self):
        self.name = "name_construct"


x = Person()
y = Person()
print(x.name, x.some)
print(y.name, y.some)

x.name = "name_obj_change"
x.some = "some_obj_change"
print(x.name, x.some)
print(y.name, y.some)

Person.name = "name_class_change"
Person.some = "some_class_change"
print(x.name, x.some)
print(y.name, y.some)



'''
name_construct Some_class
name_construct Some_class

#changed 1 obj params
name_obj_change some_obj_change
name_construct Some_class

#changed class params
name_obj_change some_obj_change
name_construct some_class_change
'''