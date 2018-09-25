username = input("enter your username:")
password = input("enter your password:")
repassword = input("enter your password again:")
while password != repassword:
    print("sai r huhu")
    repassword = input("enter your password again:")
if password == repassword:
    print("đúng r")
email = input("enter your email:")
while "@" not in email and "." not in email:
    print("lỗi")
    email = input("enter your email again:")

