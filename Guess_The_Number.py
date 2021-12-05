import random

User_Random_Number= random.randint(0,100)
User_Guess_Number= int(input("Guess the Random Number: "))

while User_Guess_Number != User_Random_Number:
    if User_Guess_Number < User_Random_Number:
        print("Your guess was lower than the correct answer.")
        User_Guess_Number= int(input("Guess the Random Number: "))
    elif User_Guess_Number > User_Random_Number:
        print("Your guess was higher than the correct answer.")
        User_Guess_Number= int(input("Guess the Random Number: "))

print("Congratulations you guessed the corrrect number!")

