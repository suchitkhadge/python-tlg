import os
import questions

def main():
    #player level and guesses player used counter
    exit = ""
    level = 0
    guess = 0

    os.system("cls")
    ##While loop for see if user pressed 1 to exit or level is complete
    while (exit != "1" and level < len(questions.quiz) and guess <2):
        try:    
            print(questions.quiz[level].get("question"))
            i = 1
            for x in questions.quiz[level].get("choice"):
                print("\t", i, ".", x)
                i +=1
            response = input("Choose 1, 2, 3 or 4: ")
            if response.isdigit() == False:
                print("Wrong input. Please choose from the given options. ")
                continue
        except ValueError as NoCharactersAccepted:
            print("Please enter a number! ")
        
        

        #While loop to see if the user selected the correct answer
        while (guess<2):
            if response == questions.quiz[level].get("correct_answer"):
                if level == len(questions.quiz)-1:
                    level += 1
                    print("Congrats! You won the game! Level ", level, " passed!")
                    break
                level += 1
                guess = 0
                print("You guessed right. Level ", level, "passed. ")
                break
            elif guess == 1:
                guess +=1
                print("GAME OVER! TRY AGAIN!  ")
                break
            else:
                response = input("You guessed wrong!!! Last chance!! Please choose again: ")
                guess +=1
                continue
                
        
    exit = print("-----THE END----- ")

if __name__ == "__main__":
    main()
    
