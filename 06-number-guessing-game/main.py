import random
secret_num= random.randint(1,100)
def check_guess(secret_num):
    attempt = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if 1 <= guess <= 100:
                attempt += 1
                if guess < secret_num:
                    print("Too low! Try again.")
                elif guess > secret_num:
                    print("Too high! Try again.")
                else:
                    return guess, attempt
            else:
                print("Please enter a number between 1 and 100.")
                continue  
        except ValueError:
            print("Please enter a valid integer.")
            continue
guess, attempt = check_guess(secret_num)
print(f"Secret number: {secret_num}")
print(f"Your guess: {guess}")
print(f"Attempt {attempt}")

