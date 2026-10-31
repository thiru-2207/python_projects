#importing libraries
import os
import random
import os

#clearing screen
os.system('cls' if os.name == 'nt' else 'clear')

#tutorial
print("\n\n\nWelcome! Guess the secret number between 1 and 100 in as few tries as possible.")


# each iteration is a separate game
while True:
        
        #generates a random number
        bot_choice = random.randint(1,100)

        #variables
        attempts = 0


        # the actual game part
        while True:

                #asking input from user
                try:
                    user_choice = int(input("\n\nEnter your choice (1-100): "))
                except ValueError:
                        print("\n\n~~~~~~Invalid Input~~~~~~\n{ hint : Enter an number }\n\n")
                        continue
                
                # displaying user the information for the input
                if user_choice == bot_choice :
                        attempts += 1
                        print(f"you won in the {attempts} attempt(s).\n\n")
                        break
                elif user_choice < bot_choice :
                        print("your value is TOO LOW.\n")
                        attempts +=1
                else:
                        print("your value is TOO HIGH.\n")
                        attempts +=1

        # asking user wheather they want to continue
        user_input=input("Do You Want To Play Again? {y/n  dafault:n} : ").strip().lower()
        if user_input == 'y':
                continue
        else:
                break
print("Thank you for playing !!!\n\n\n ")