from random import randint

choice = ["rock","paper","scissors"]

cpu = choice[randint(0,2)]

print("Lets play Rock, Paper, Scissors\n")
player= input("Your Move: ").lower()
print("CPU's move: "+ cpu)

if player == cpu:
    print("Draw")

elif player == "Rock" and cpu == "Paper":
    print("CPU Wins")
elif player == "Rock" and cpu == "Scissor":
    print("Player wins")

elif player == "Paper" and cpu == "Rock":
    print("Player wins")
elif player == "Paper" and cpu == "Scissors":
    print("CPU Wins")

elif player == "Scissors" and cpu == "Rock":
    print("CPU Wins")
elif player == "Scissor" and cpu == "Paper":
    print("Player wins")