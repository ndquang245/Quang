
# singer = input("nhap ten ca si:")
# date = input("nhap ten ngay sinh:")
# country = input("nhap ten nuoc:")

# person = {
#     "singer" : singer,
#     "date" : date,
#     "country" : country
# }
# print(person)
# status =  input("nhap tinh hinh hon nhan:")
# person["status"] = status

# print(person)

# status2 = input("nhap tinh hinh ngon nhan:")
# person["status"] = status2
# print(person)
# a = input("nhap cai muon xoa:")
# del person[a]
# print(person)
# if "singer" in person:
#     print("true")
# else:
#     print("false")

# dictionary = {
#     "iron man" : "co rat nhieu bo giap khac nhau",
#     "batman" : "don gian la co suc manh cua doi",
#     "hulk" : "1 thang to cao da mau xanh"
# }
# print(dictionary)
# n = input("nhap ten anh hung ban muon:")
# dictionary = {
#     n : "co rat nhieu giap",
    
# }
# print(dictionary)
# m = input("nhap ten anh hung:")
# dictionary = {
#     m : "suc manh cua doi"
# }
# i = str.lower(input("nhap ten pokemon:"))

# pokemon = {
#     "raichu" : 'raichu has a regional variant that is Electric/Psychic. It evolves from Pikachu when exposed to a Thunder Stone. All Pikachu in Alola will evolve into this form regardless of their origin.',
#     "onix" : 'Onix resembles a giant chain of gray boulders that become smaller towards the tail. It has a rocky spine on its head and a pair of black eyes right beneath it. This Pokémon has a magnet in its brain'
# }


# while i not in pokemon:
#     print("ko co")
#     i = input("nhap lai ten pokemon:")

# print(pokemon[i])

# person_list = []
# p1 = {
#     "name" : "Huy",
#     "role" : "waiter",
#     "hours" : 12,
#     "salary per hours" : 0.8
# }
# p2 = {
#     "name" : "Tung",
#     "role" : "cook",
#     "hours" : 24,
#     "salary per hours" : 1.5
# }
# p3 = {
#     "name" : "M.Duc",
#     "role" : "manager",
#     "hours" : 20,
#     "salary per hours" : 2
# }
# person_list.append(p1)
# person_list.append(p2)
# person_list.append(p3)
# # print(person_list)
# p4 = {
#     "name" : "Don",
#     "role" : "waiter",
#     "hours" : 12,
#     "salary per hours" : 0.9
# }
# p5 = {
#     "name" : "H.Duc",
#     "role" : "waiter",
#     "hours" : 12,
#     "salary per hours" : 0.7
# }
# person_list.append(p4)
# person_list.append(p5)
# p3 = person_list[2]
# print(p3)

# person_list[0] = {
#     "name" : "Huyen",
#     "role" : "waitress",
#     "hours" : 14,
#     "salary per hours" : 1
# }

# person_list.pop(4)



# print(person_list)
favs =[
    {
        "movies" : "pokemon",
        "nam phat hanh" : 1900,
        "nhan_vat" : ["picachu", "raichu", "onix", "chamander"]

    },
    {
        "comic" : "doremon",
        "nam phat hanh" : 1901,
        "nhan_vat" : ["nobita", "shizuka", "xeko", "chaien"]

    },
]
p1 = favs[0]
p2 = favs[1]
# p1["country"] = "japan"
# p2["country"] = "japan"
# print(favs)
# for k,v in p1.items():
#     print(k,v, sep='-')
#     print("----")
# for m,n in p2.items():
#     print(m,n, sep='-')
i1 = p1['nhan_vat']
i2 = p2['nhan_vat']
# i1[1] = "squiters"
# i2[1] = "chaien"
# i1.append("ivysours")
# i2.append("doremon")
# i1.pop(1)
# i2.pop(1)
# print(i1[1])



# print(favs)
# for x in i1:
#     print(x)
for y in p1:
    print(y)