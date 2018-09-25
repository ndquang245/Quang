n = int(input("how many cạnh you want:"))


from turtle import *
shape("turtle")
a = 360/n
for i in range(n):
    forward(100)
    left(a)
    n = n + 1



mainloop()