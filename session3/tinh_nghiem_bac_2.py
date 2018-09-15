a = int(input("a=?"))
b = int(input("b=?"))
c = int(input("c=?"))
denta = b**2 - 4*a*c
if denta < 0:
    print("vo nghiem")
elif denta == 0:
    x=(-b+denta*0.5)/2*a
    print("nghiem kep")
    print("x=",x)




else:
    x1=(-b+denta*0.5)/2*a
    x2=(-b-denta*0.5)/2*a
    print("2 nghiem phan biet")
    print("x1=", x1)
    print("x2=", x2)
