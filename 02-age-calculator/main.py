def calculate_age(name,dob):
    current_year = 2026
    age = current_year - dob
    return age
    

    
name = input("What is your name: ")
dob = int(input ("What is your date of birth: "))
age = calculate_age(name,dob)
print(f"Hello, {name.capitalize()}!")
print(f"You were born in {dob}.")
print(f"You are {age} years old.")