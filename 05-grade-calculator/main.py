def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >=70:
        return "C"
    elif score >= 60:
        return 'D'
    else:
        return "F"


while True:
        try:
            name = input("Enter your name: ").title()
            score = float(input("Enter score: "))
            if 0<=score<=100:
                grade  = calculate_grade(score)
                print(f"{name} scored {score}")
                print(f"Grade: {grade}")
                break
            else:
                 print("Error: Score must be between 0 and 100.")
                 continue
        except ValueError:
             print("Error: Please enter a valid number.")