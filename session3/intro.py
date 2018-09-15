yob = int(input("your year of birth?"))

age = 2018 - yob


print(age)

if age < 10:
    print("baby")
elif age < 18: # else if
    print("teen")
else:
    print("not baby")


