import random

welc_message = input("Welcome to the number guessing game! Would you like to play? ")


if welc_message.lower() == "yes":
    print("Alright, let's get started!")
    
elif welc_message.lower() != "yes":
    print("Okay, no problem! ")
    quit()
    


max_num_range = input("Enter the maximum number you want to guess: ")

if max_num_range.isdigit():
        max_num_range = int(max_num_range)
        
        if max_num_range >= 101:
            print("The maximum number cannot be greater than 100!")
            quit()
    
else:
     print("Please enter an integer! ")
     quit()
            
    
    
min_num_range = input("Enter the minimum number you want to guess: ")

if min_num_range.isdigit():
            min_num_range = int(min_num_range)
            
            if min_num_range < 0:
                print("The minimum number cannot be negative")
                quit()
else:
    print("Please enter an integer! ")
    quit()
            
            
rand_num = random.randint(min_num_range, max_num_range)


while True:
    instruc = input("Please enter a number for your guess! ")
    
    if instruc.isdigit():
        instruc = int(instruc)
        
    else:
        print("Please enter an integer!")
        continue
    
    if instruc == rand_num:
        print("You nailed it!")
        break
    
    
    elif instruc <= rand_num:
        print("Try guessing higher!")
            
    elif instruc >= rand_num:
        print("Close, try going lower!")
        







        


    







 
