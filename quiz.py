import random

# Sample questions
quiz_questions = [
    {
        "type": "multiple_choice",
        "question": "What is the capital of France?",
        "choices": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "type": "fill_in_the_blank",
        "question": "The chemical symbol for water is ____.",
        "answer": "H2O"
    },
    {
        "type": "multiple_choice",
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "type": "fill_in_the_blank",
        "question": "The author of 'Romeo and Juliet' is ____.",
        "answer": "Shakespeare"
    },
]

def display_welcome():
    print("Welcome to the Quiz Game!")
    print("Rules:")
    print("1. You will be asked multiple-choice or fill-in-the-blank questions.")
    print("2. Each correct answer earns you 1 point.")
    print("3. No penalty for wrong answers.\n")

def ask_question(question):
    print("\n" + question["question"])
    if question["type"] == "multiple_choice":
        for choice in question["choices"]:
            print(choice)
        user_answer = input("Enter the letter of your choice (A/B/C/D): ").strip().upper()
    else:
        user_answer = input("Enter your answer: ").strip()
    return user_answer

def evaluate_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def run_quiz():
    score = 0
    random.shuffle(quiz_questions)

    for q in quiz_questions:
        user_answer = ask_question(q)
        if evaluate_answer(user_answer, q["answer"]):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {q['answer']}")
    
    print("\nQuiz Completed!")
    print(f"Your final score: {score}/{len(quiz_questions)}")

    if score == len(quiz_questions):
        print("Excellent! Perfect score!")
    elif score >= len(quiz_questions) // 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing! You'll get better.")

def main():
    while True:
        display_welcome()
        run_quiz()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
