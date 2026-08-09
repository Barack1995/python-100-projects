import string
import random
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
special = string.punctuation
correct_characters = string.ascii_letters + string.digits + string.punctuation
def generate_password(length):
    password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(numbers),
    random.choice(special)]

    for _ in range(length-len(password)):
        password.append(random.choice(correct_characters))
    random.shuffle(password)
    return "".join(password)
    
while True:
    try:
        password_length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    if password_length < 4:
        print("Password length should be at least 4 characters.")
        continue
    else:
        password = generate_password(password_length)
    break
print("Password generated:", password)

