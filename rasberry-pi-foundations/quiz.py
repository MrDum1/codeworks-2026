#Quiz game

score = 0

questions = [
    {
        "question": "What is the name of the red faction in the game HellDivers2?",
        "options": ["A. Robots", "B. Automatons", "C. Terminators", "D. The Seekers"],
        "answer": "B"
    },
    {
        "question": "What is the name of the bug with big legs that spew acid?",
        "options": ["A. Bile Titan", "B. Big Titan", "C. Spewer", "D. Firebug"],
        "answer": "A"
    },
    {
        
        "question": "What faction attacked Super Earth Recently?",
        "options": ["A. Seekers", "B. Automatons", "C. Terminids", "D. Illuminates"],
        "answer": "D"
    }
]

print("Welcome to the HellDivers2 Quiz Game!\n")
print("We serve Freedom, Liberty, and Democracy for Super Earth)")
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
    
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.")

print(f"\nYour final score is: {score}/{len(questions)}")

if score != len(questions): 
    print("\nWell looks like someone is going to Democracy camp!")
else:
    print("\nCongratulations! You are a true HellDiver!, now go and serve Super Earth!")
