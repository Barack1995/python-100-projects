def greeting(name,age,country):
    print("Hello ",name.capitalize())
    print(f'You are {age} years old ')
    print("You are from",country.title())
    print("Welcome to Python programming!")


name = input("What is your name: ")
age = int(input ("What is your age: "))
country = input ("What is your country: ")
greeting(name,age,country)