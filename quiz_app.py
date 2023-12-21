"""
# A dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key vallue pairs
# display each question to the user and allow them to answer
# tell the if they are right or wrong
# show the final result when the quiz is completed
"""
quiz = {
    "q1": {
        "question": "What is the capital of France? ",
        "answer": "Paris"
    },
    "q2": {
        "question": "What is the captial of Germany? ",
        "answer": "Berlin"
    },
    "q3": {
        "question": "What is the capital of Italy? ",
        "answer": "Rome"
    },
    "q4": {
        "question": "What is the capital of Spain? ",
        "answer": "Madrid"
    },
    "q5": {
        "question": "What is the capital of Portugal? ",
        "answer": "Lisbon"
    },
    "q6": {
        "question": "What is the capital of Switzerland? ",
        "answer": "Bern"
    },
    "q7": {
        "question": "What is the capital of Austria? ",
        "answer": "Vienna"
    },
    "q8": {
        "question": "What is the capital of Ghana? ",
        "answer": "Accra"
    },
    "q9": {
        "question": "What is the capital of Togo? ",
        "answer": "Lome"
    },
    "q10": {
        "question": "What is the capital of Senegal? ",
        "answer": "Dakar"
    }

}

score = 0
total = 0

for key, value in quiz.items():
    total += 1
    print(value["question"])
    answer = input("Answer?")
    

    if answer.lower() == value["answer"].lower():
        print("Correct")
        score += 1
        print("")
        print("")
    else:
        print("Wrong")
        print(f"The correct answer is {value["answer"]}")
        print("")
        print("")

print(f"You got {score} out of {total} correct")
print(f"Percentage:  {int(score / total * 100)}%")
