person_list = []
p1 = {
    "name" : "Quang",
    "age" : 15
}
p2 = {
    "name" : "QChau",
    "age" : 15
}


person_list.append(p1)
person_list.append(p2)
# print(person_list)

# person_list.pop(0)
# print(person_list)
# person_list[0] = {
#     "name" : "An Binh",
#     "age" : 16
# }
# print(person_list)
# p = person_list[0]
# p["age"] += 1
# print(p["name"])
# print(p)

p = person_list[0]
# print(p)
for p in person_list:
    print(p)
    print(p["name"])
    print(p["age"])
    print("________")