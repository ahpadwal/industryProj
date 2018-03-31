from random import randint
values=["Rock","Paper","Scissor"]
print ("Starting Rock Paper Scissor...")
userIn=1
while userIn==1:
    userIn=int(input("\nSelect your option 1:Rock 2:Paper 3:Scissor : "))
    user = values[userIn - 1]
    computer=values[(randint(1,3))-1]
    if user == computer:
        print("Tie!")
    elif user == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", user)
        else:
            print("You win!", user, "smashes", computer)
    elif user == "Paper":
        if computer == "Scissor":
            print("You lose!", computer, "cut", user)
        else:
            print("You win!", user, "covers", computer)
    elif user == "Scissor":
        if computer == "Rock":
            print("You lose...", computer, "smashes", user)
        else:
            print("You win!", user, "cut", computer)
    else:
        print("Please enter a valid selecetion")
    userIn=int(input("Do you want to continue? [1/0] "))
print("Good Bye!")

#changed in CentOS
