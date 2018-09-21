from random import randint

x = randint(0,10)


i = int(input("đoán đi:"))
while i != x:
    if i > x:
        print("nhỏ hơn đi")
    else:
        print("lớn hơn đi")
    i = int(input("đoán lại đi:"))
    
if i == x:
    print("đúng r")





