# print("* * * * * * * * * * * * * * * * * * * *")


# i = int(input("how many stars:"))
# for i in range(0, i):
#     print("*", end = "")

# print(" x *"*4, end = " x")
# i = int(input("enter a number:"))
# print(" x *"*i, end = " x")

# i = int(input("how many stars:"))
# for i in range(0, i):
#     print("*", end = "")
#     print()



# for i in range(0, 3):
#     print("*"*7, end = "")
#     print()

# n = int(input("how many dòng:"))
# m = int(input("how many stars:"))

# for i in range(0, n):
#     print("*"*m, end = "")
#     print()




# x = 2
# y = 3
# for i in range(0, 5):
#     for j in range(6):
#         if i == y and j == x:
#             print("*", end =' ')
#         else:
#             print("-", end =' ')
            
#     print()


x = int(input("tọa độ chiều ngang:"))
y = int(input("tọa độ chiều dọc:"))
w = int(input("chiều rộng"))
h = int(input("chiều dài"))
for i in range(0, w):
    for j in range(h):
        if i == y and j == x:
            print("*", end =' ')
        else:
            print("-", end =' ')
            
    print()



