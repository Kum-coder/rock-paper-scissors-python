import random
l = ["rock", "paper", "scissor"]
while True:
    userCount = 0
    compCount = 0
    uc = int(input('''
   Game Start...
    1 Yes
    2 No | Exit'''))
    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
     1 rock
     2 paper
     3 scissor      '''))
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "paper"
            elif userInput == 3:
                uchoice = "scissor"
            else:
                print("Invalid input, try again!")
                continue

            compchoice = random.choice(l)
            if compchoice == uchoice:
                print("computer value: ", compchoice)
                print("User value: ", uchoice)
                print("Game draw")
                userCount = userCount + 1
                compCount = compCount + 1
            elif (uchoice == "rock" and compchoice == "scissor") or (uchoice == "scissor" and compchoice == "paper") or (uchoice == "paper" and compchoice == "rock"):
                print("you win")
                userCount = userCount + 1
            else:
                print("computer value: ", compchoice)
                print("User value: ", uchoice)
                print("Comp Win")
                compCount = compCount + 1

        if userCount == compCount:
            print("Final Game Draw")
            print("User Score: ", userCount)
            print("Comp Score: ", compCount)
        elif userCount > compCount:
            print("You won")
            print("User Score: ", userCount)
            print("Comp Score: ", compCount)
        else:
            print("Comp won")
            print("User Score: ", userCount)
            print("Comp Score: ", compCount)
    else:
        break
