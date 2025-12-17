import random
import string

def password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password1 = ''.join(random.choice(characters)
    for _ in range(length))
    return password1

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        new_password = password(length)
        print("Generated Password:", new_password)
