import random

user_wins = 0

computer_wins = 0

choices = ['Rock', 'Paper', 'Scissors']


while True:
    user_input = input("Enter Rock, paper or scissors! ")
    
    
    random_number = random.randint(0, 2)     # 0: Rock | 1: Paper | 2: Scissors   
    
    computer_pick = choices[random_number]
    print("The computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        
            
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
       
    
    else:
        print("You Lost :(")
        computer_wins += 1
    
print("You won " + str(user_wins) + " times")
print("The computer won " + str(computer_wins) + " times")
        
print("Goodbye!")
    
