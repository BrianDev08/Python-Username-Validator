#invalidate user input exercise
#1.username is no more than 12 character
#2.username must not contain space
#3.username must not contain digit

username=input("Enter your username: ")

if len(username) > 12:
    print("Your username can't be longer than 12 characters")
elif not username.find(" ")==-1:
    print("Your username can't contain space")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
