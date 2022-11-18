import random

level = 0
guess = 0

quiz= [{
         "category": "Music",
         "question": "Who sang the song 'Hit me baby? ",
         "correct_answer": "3",
         "choice": [
             "Justin Waka Kinobi", "Nick June", "Haley Smith", "Adele"
            ]
        },
        
        {
         "category": "Music",
         "question": "Who was the singer for song 'Break it down? ",
         "correct_answer": "4",
         "choice": [
             "Waka Kinobi", "Nicky June", "Hals Smitu", "Akon"
            ]
        },
        {
         "category": "Music",
         "question": "Who was the singer for Linkin Park? ",
         "correct_answer": "2",
         "choice": [
             "Waka Kinobi", "Chester Bennington", "Ibby Izzy", "Ricky Martin"
            ]
        },
        {
         "category": "Music",
         "question": "Who was the first album of Pink Floyd? ",
         "correct_answer": "4",
         "choice": [
             "Wish you were here", "The Wall", "The dark side of the moon", "Piper at the Gates of Dawn"
            ]
        },
        {
         "category": "Music",
         "question": "Who was the very first American Idol winner? ",
         "correct_answer": "2",
         "choice": [
             "Kelly CLarkson", "Carrie Underwood", "David Cook", "Ricky Martin"
            ]
        }
        ]

while (exit != "1" and level <= 3 and guess <2):
    try:    
        print(quiz[level].get("question"))
        i = 1
        for x in quiz[level].get("choice"):
            print("\t", i, ".", x)
            i +=1
        response = input("Choose 1, 2, 3 or 4: ")
    except ValueError as NoCharactersAccepted:
        print("Please enter a number! ")
    
    

    
    while (guess<2):
        if level == 3:
            print("Congrats! You won the game!")
            break
        if response == quiz[level].get("correct_answer"):
            print("You guess right")
            level += 1
            guess = 0
            break
        elif guess == 1:
            print("Time is up! ", guess)
            guess = 0
            break
        else:
            response = input("You guessed wrong!!! Last chance!! Please choose again: ")
            guess +=1
            continue
            
    
    exit = input("Press 1 to exit or any other key to continue?  ")
    
