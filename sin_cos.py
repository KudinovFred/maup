def cos_angle(angle,n):
    addition=1
    result = 1
    n+=1

    for i in range(2,n,2): print(i,"g")

    for i in range(2,n,2):
        print (i)

        addition *= -1*(angle**2)/(n*n-n)

        print(addition)

        result+=addition
    print(result)

    pass

cos_angle(60,6)
cos_angle(60,8)
cos_angle(60,10)
cos_angle(60,20)


from math import sqrt,cos,sin,pi

print("lkj",cos(pi/6))

print(pi/6)