import random

def rules():
    print("-------Game Rules-------")
    print("There are 5 fruits to choose from.")
    print("Apple, Orange, Banana, Kiwi, Grape")
    print("A sequence of 4 randomly chosen fruits will be generated")
    print("Example: Orange, Banana, Kiwi, Orange")
    print("After each guess, the game will tell you how many fruits have been correctly chosen but in the wrong position")
    print("And how many have been correctly chosen and also in the right position")
    print("Your goal is to correctly guess the sequence of fruits in as few tries as possible")
    print("Press Enter to start")
    enter = input("Are You Ready?")



def menu():
    print("Welcome To Mastermind")
    start = str(input("Would You Like To Play (Y/N): "))
    if start == "Y" or  start == "y":
        print("Great Let's Start")
        game()
    elif start == "N" or  start == "n":
        end()
    else:
        print("Please Only Enter Y or N")
        menu()
    
def game():
    fruits = ["apple", "orange", "banana", "kiwi", "grape"]
    corrAnswer = []
    for i in range(4):
        corrAnswer.append(random.choice(fruits))
    print (corrAnswer) #remove this line to show answer
    familiar = str(input("Are You Familiar With The Rules? (Y/N): ")).lower()
    while familiar != "y" and familiar != "n":
        print("Please Only Enter Y or N")
        game()
    if familiar == "n":
            rules()
    e = 0
    tries = 10
    while e == 0:
        e = 0
        print("----------------------Difficulty---------------------")
        print("Easy - 15 Tries   Normal - 12 Tries   Hard - 10 Tries")
        triesStr = input("Select A Difficulty (E/N/H): ")
        triesStrLow = triesStr.lower()
        if triesStrLow == "e":
            tries = 15
            e += 1
        elif triesStrLow == "n":
            tries = 12
            e += 1
        elif triesStrLow == "h":
            tries = 10
            e += 1
        else:
            print("Enter A Valid Answer")
    print("---------Let's Begin---------")
    gameOver = False
    while gameOver == False :
    #Vefification of inputed answer
        print("Tries Remaining: " + str(tries))
        corr = 0
        while corr < 4:
            print("Enter Your Answer Seperated By A Dash - ex: Orange-Apple-Banana-Grape")
            ans = str(input("Your Answer: "))
            lowerAns = ans.lower()
            listAnswer = lowerAns.split("-")
            if len(listAnswer) == 4:
                for i in range(len(listAnswer)):
                    x = 0
                    mismatches = 0
                    for j in range(len(fruits)):
                        if listAnswer[i] == fruits[j]:
                            corr += 1
                            break
                        else:
                            mismatches += 1
                        if mismatches == 5:
                            print("Please Enter A Valid Answer")
                            x += 1
                            break
                    if x > 0:
                        break
            else:
                print("You've Only Entered " + str(len(listAnswer)) + "/4 Fruits In Your Answer. Try Again")
        #Game Logic
        #Compare listAnswer[i] against corrAnswer[i] 
        #If match found, correct place += 1 and remove from listAnswer & corrAnswer
        listAnswerTemp = listAnswer
        corrAnswerTemp = corrAnswer[:]
        corrFruit = 0
        wrongFruit = 0
        i = 0
        f = 0
        toRemove = []
        for i in range(len(listAnswerTemp)) :
            if listAnswerTemp[i] == corrAnswerTemp[i]:
                toRemove.append(listAnswerTemp[i])
                corrFruit += 1
        x = 0
        while x < len(toRemove):
            listAnswerTemp.remove(toRemove[x])
            corrAnswerTemp.remove(toRemove[x])
            x += 1
        #Check listAnwer[i] against corrAnswer[j]
        #If match, wrong place += 1 and remove from listAnswer &corrAnswer
        i = 0
        j = 0
        for i in range(len(listAnswerTemp)) :
            for j in range(len(corrAnswerTemp)):
                if listAnswerTemp[i] == corrAnswerTemp[j] :
                    wrongFruit += 1
                    break
                j += 1
            i += 1
        tries -= 1
        if corrFruit == 4 :
            gameOver = True
            print("--------YOU WON--------")
        else:
            print("Fruits In Correct Position: " + str(corrFruit))
            print("Fruits In The Wrong Position: " + str(wrongFruit))
            if tries == 0:
                gameOver = True
                print("-------------GAME OVER-------------")
                print("Answer Was: " + str(corrAnswer))
    passed = False
    while passed == False:
        again = input("Would You Like To Play Another Game? (Y/N): ")
        againLower = again.lower()
        if againLower == "y" :
            game()
        elif againLower == "n" :
            end()

def end():
    print("Thanks For Playing, Hope to See You Soon!")
    quit()

menu()