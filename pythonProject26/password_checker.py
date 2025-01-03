password = input("Input password.It should be more than five characters long.It should contain special characters, uppercase,lowercase and digits ")

with open('common passwds.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("This password is too common, making it easy to be guessed")
    exit()



if any(char.isupper() for char in password):
    upper = 1
else:
    upper = 0

if any(char.islower() for char in password):
    lower = 1
else:
    lower = 0

if any(char.isdigit() for char in password):
    dig = 1
else:
    dig = 0

characters = set("@#$%^&*()<>?/\|}{~:;!'\"[]")
if any(char in characters for char in password):
    characters = 1
else:
    characters = 0

score = dig + upper + lower + characters

if len(password) >= 8:
    score += 1

if len(password) < 5:
    print("The password is too short.")
    exit()


if score >= 5:
    print("The password is strong")
else:
    print("The password is too weak")
