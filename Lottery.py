import random
Player_Decision= "y"
Random_Numbers= []
Three_Numbers_User= []

for k in range(0,3):
        Three_Random_Numbers= random.randint(0,9)

        while Three_Random_Numbers in Random_Numbers:
            Three_Random_Numbers = random.randint(0,9)

        Random_Numbers.append(Three_Random_Numbers)
while Player_Decision == "y":
    for k in range (0,3):
        User_Input_Three_Numbers = int(input("Enter Number: "))

        while User_Input_Three_Numbers in Three_Numbers_User or User_Input_Three_Numbers < 0 or User_Input_Three_Numbers >9:
            print("Your Number is not valid")
            User_Input_Three_Numbers = int(input("Enter Number:"))
    
        Three_Numbers_User.append(User_Input_Three_Numbers)

    print(f"The lottery numbers are {Random_Numbers}")
    print(f"The number you have chosen are {Three_Numbers_User}")

    if Random_Numbers == Three_Numbers_User:
        print("Winner")
        Random_Numbers.clear()
        Three_Numbers_User.clear()
    else: 
        print("You loss")
        Random_Numbers.clear()
        Three_Numbers_User.clear()

    Player_Decision= str(input("\n [y]Play again \n [n]Exit \n Do you want to try again? "))
    if Player_Decision == "y":
            for b in range(0,3):
                    Three_Random_Numbers= random.randint(0,9)

                    while Three_Random_Numbers in Random_Numbers:
                        Three_Random_Numbers = random.randint(0,9)

                    Random_Numbers.append(Three_Random_Numbers)
            
    if Player_Decision == "n":
        print("Thank you for playing Kaydee Lottery")
        break