"""
def my_func():
    s = input("input some value")
    return lambda x: eval(s)


z = my_func()
a= z(2)
"""

def my_func(a,b,  *args, x=5, **kwargs):


    print (a,b,x)
    print(args)
    print(kwargs)






my = [[11,12,13],[21,22,23],[31,32,33]]
print(*my)

print(list(zip(*my)))
for i in zip(*my): print(i)



def gen_x(n):
    yield n**2

for i in range(5):
    print(gen_x(i))


print(6&1)


from math import pi, sin

print(sin(pi/6))
