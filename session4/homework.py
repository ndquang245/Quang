from random import randint

print("pick a number 0 to 100")


guest_number = int(input("enter your number:"))
i = True

while i:
    computer_number = randint(0,100)
    if computer_number == guest_number:
        print("computer number:", computer_number)
        print("computer number is right")
        i = False
    elif computer_number > guest_number:
        print("computer number:", computer_number) 
        print("your number smaller")
    else:
        print("computer number:", computer_number)
        print("your number bigger")
    


