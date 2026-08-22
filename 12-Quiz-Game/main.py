question = {
    "question": "What is the capital of France?",
    "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
    "answer": "C"
}

question2 = {
    "question": "What is the largest planet in our solar system?",
    "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
    "answer": "B"
}
    
question3 = {
    "question": "What is the chemical symbol for water?",
    "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
    "answer": "A"
}

questions = [question, question2, question3]
score = 0

for index, question in enumerate(questions, start=1):
    print(f"{index}. {question['question']}") 
    for option in question['options']:
        print(option)

    print()  # Print a blank line for better readability
    while True:
        user_answer = input("Enter your answer: ").strip().upper()
        if user_answer not in ['A', 'B', 'C', 'D']:
            print("Invalid input. Please enter A, B, C, or D.")
            continue
        break
    if user_answer == question['answer']:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌")
    print()
percentage = (score / len(questions)) * 100
print("Quiz completed! 🎉")
print(f" Final score: {score}/{len(questions)}\n")
print("Percentage: {:.1f}%".format(percentage))
