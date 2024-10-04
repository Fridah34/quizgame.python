def new_game():

     guesses =[]
     correct_guesses = 0
     question_num = 1

     for key in questions:
         print("----------------------")
         print(key)
         for i in options[question_num-1]:
             print(i)
         guess=input("Enter(A,B,C or D): ")
         guess=guess.upper()
         guesses.append(guess)

         correct_guesses +=check_answer(questions.get(key),guess)
         question_num +=1
     display_score(correct_guesses,guesses)

#--------------------------------
def check_answer(answer,guess):

    if answer==guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


#--------------------------------
def display_score(correct_guesses,guesses):
    print("---------------------")
    print("RESULTS")
    print("---------------------")

    print("Answers:",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Guesses:", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score=int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


#--------------------------------
def play_again():

    response=input("Do you want to play again? (yes or no): ")
    response=response.upper()

    if response=="YES":
        return True
    else:
        return False
#--------------------------------

questions={
    "Who was Kenya's president in 2017?: ":"C",
    "Which is the largest airport in Kenya?: ": "D",
    "When were the last olympics held?: ": "B",
    "When did Kenya attain Independence?: ":"A"
}

options=[["A. Jomo Kenyatta","B. Daniel Arap Moi","C. Uhuru Kenyatta","D. Mwai Kibaki"],
         ["A. Kisumu  Airport","B. Wilson Airport","C. Eldoret  Airport","D. Jomo Kenyatta International Airport"],
         ["A. 2020","B. 2024","C. 2023","D. 2019"],
         ["A. 1963","B. 1974","C. 1973","D. 1954"]]

new_game()

while play_again():
    new_game()
print("Byeeeeee!")



