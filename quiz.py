import random
import matplotlib.pyplot as plt

def ask_question(question, choices, correct_answer):
    print("\n" + question)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    
    while True:
        try:
            answer = int(input("Enter your choice (1-4): "))
            if 1 <= answer <= 4:
                return answer == correct_answer
            else:
                print("Invalid choice. Choose a number between 1-4.")
        except ValueError:
            print("Invalid input. Enter a number between 1-4.")

def run_quiz():
    questions = [
        {"question": "What is the capital of Japan?", "choices": ["Seoul", "Tokyo", "Beijing", "Bangkok"], "answer": 2},
        {"question": "Which planet is known as the Red Planet?", "choices": ["Earth", "Mars", "Jupiter", "Venus"], "answer": 2},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "choices": ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Jane Austen"], "answer": 1},
        {"question": "What is the chemical symbol for Gold?", "choices": ["Au", "Ag", "Pb", "Pt"], "answer": 1},
        {"question": "Which ocean is the largest?", "choices": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": 3},
    ]
    
    random.shuffle(questions)
    correct = 0
    incorrect = 0
    
    for q in questions:
        if ask_question(q["question"], q["choices"], q["answer"]):
            print("Correct!")
            correct += 1
        else:
            print("Incorrect!")
            incorrect += 1
    
    print(f"\nFinal Score: {correct} correct, {incorrect} incorrect")
    visualize_results(correct, incorrect)

def visualize_results(correct, incorrect):
    labels = ['Correct', 'Incorrect']
    values = [correct, incorrect]
    colors = ['green', 'red']
    
    plt.bar(labels, values, color=colors)
    plt.xlabel('Answer Type')
    plt.ylabel('Count')
    plt.title('Quiz Performance')
    plt.show()

if __name__ == "__main__":
    run_quiz()