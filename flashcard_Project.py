


# function to create cards when users input

def card_creator():
    print("Welcome to the program.")
    userCards = []
    inputQues = input("Enter a question or press enter to finish: ")
    while inputQues:
        inputAns = input("Enter your answer to the question: ")
        card = {"Question":inputQues,
            "Answer":inputAns}
        userCards.append(card)
        inputQues = input("Enter a question or press enter to finish: ")
    print("-"*20)
    return userCards

#### main program
cards = card_creator()

def study():
    print("Now let's go over your flashcards to see how much you remember.")
    rightAns = 0
    for i in cards:
        print(i['Question'])
        studyInput = input("Answer: ")
        if studyInput == i['Answer']:
            print("Correct")
            rightAns += 1
        else:
            print("Incorrect")
    print("Number of right answers: ", str(rightAns)+'/'+str(len(cards)))


def review():
    index = 1
    print("Below is your flashcard:")
    print("-"*20)
    for j in cards:
        print(str(index) + '.'+' ' + j['Question']+':'+ ' ' +j['Answer'])
        index = int(index)+ 1
        
def review_or_study():
    print("Great job! You have successfully created your flashcards")
    choice = input('Now press "r" to review your flash cards or press "s" to study your flash cards\n(press anything else to end the program): ')
    if choice == 's':
          study()
    elif choice == 'r':
        review()
    else:
        print("Thank you for using the program.")

review_or_study()

        

      



    









