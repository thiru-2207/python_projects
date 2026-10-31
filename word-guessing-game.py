#importing libraries
import random
import os

#clears screen
os.system('cls' if os.name == 'nt' else 'clear')

#list of words
words = ["bambo", "bingo", "dodge", "funky", "gizmo","goofy", "jambo", "jazzy", "jolly", "ninja","pixie", "tango", "wacky", "zilch", "zippy","bliss", "chirp", "dance", "happy", "lucky", "magic", "party", "sunny", "sweet", "vibes","blitz", "chomp", "crash", "flick", "punch","shark", "smash", "ingot"]

#this while loop iterates once every game
def main():
    while True:
        #selects a random word from list
        random_word = random.choice(words)

        listforvariables = [None] * 5

        iteration = 0
        #this while loop runs for 5 times
        for attempt in range (5):
            while True:
                user_word = input("Guess the word : ")
                if len(user_word) != 5:
                    print("~~~~Please enter a 5-letter word.~~~~")
                    continue
                break
            for letter_pos in range (5):
                if user_word[letter_pos] == random_word[letter_pos] :
                    listforvariables[letter_pos] = f"\033[1;92m {user_word[letter_pos]} \033[0m"
                elif user_word[letter_pos] in random_word :
                    listforvariables[letter_pos] = f"\033[1;93m {user_word[letter_pos]} \033[0m"
                else:
                    listforvariables[letter_pos] = f"\033[1;91m {user_word[letter_pos]} \033[0m"
            print("~"*50,"\n",*listforvariables,"\n","~"*50)
            if user_word == random_word :
                print("you found the word!!! ")
                break
        print(random_word)
        if input("do u want to play again ?? (y/n) : ").lower() != 'y':
            break
            
        


if __name__ == '__main__' :
    main()
