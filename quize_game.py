#--------------------------------
def new_game():
    quesses = []
    correct_guess = 0
    question_number = 1
    for key in questions:
        print("--------------------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
        quess = input("Enter (A, B, C, or D): ").upper()
        quesses.append(quess)

        correct_guess += check_answer(questions.get(key), quess)
        question_number += 1
        display_score(correct_guess, quesses)




#--------------------------------
def check_answer(answer, quesses):
    if answer == quesses:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
#--------------------------------
def display_score(correct_guess, quesses):
    print("--------------------------------")
    print("RESULTS")
    print("--------------------------------")
    print("Answer: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Quesses: ", end="")
    for i in quesses:
        print(i, end=" ")
    print()
    score = int((correct_guess/len(questions))*100)
    print("Your score is: "+str(score)+"%")
#--------------------------------
def play_again():
    response = input("Do you want to play again?(YES or No): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False









questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
    }

options = [["A. Quido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1998", "B. 1991", "C. 1999", "D. 2000"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Somthing", "D. Whta's Earth?"]]

new_game()
while play_again():
    new_game()
print("Thank you for Playing!")