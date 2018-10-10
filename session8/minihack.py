
# PART1


# a = int(input("how many hp:"))
# b = int(input("how many dell:"))
# c = int(input("how many macbook:"))
# d = int(input("how many asus:"))
laptop_list = {
    "hp" : 20,
    "dell" : 50,
    "macbook" : 12,
    "asus" : 30
}

# laptop_list = {
#     "hp" : a,
#     "dell" : b,
#     "macbook" : c,
#     "asus" : d


# print(laptop_list["macbook"])
# laptop = input("enter a laptop you like:")
# print(laptop_list[laptop])

# laptop_list["toshiba"] = "10"
# print(laptop_list)
# print(laptop_list)



# laptop_list["dell"] += 10
# laptop_list["macbook"] -= 2
# print(laptop_list)

# PART2
laptop_list = {
    "hp" : 20,
    "dell" : 50,
    "macbook" : 12,
    "asus" : 30
}
for k,v in laptop_list.items():
    print(k,v, sep=':')