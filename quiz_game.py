



# Quiz game

# Ask users questions, if they give us right answer, add 1 to their score

print("Welcome to Monkey Game!")

playing = input("Would you like to play Monkey Game? ")



if playing.lower() != "yes":
    print("Alright, Let's do this! ")
elif playing.lower() != "yes":
    print("Okay")

print("A quick note: Answers to this game must be printed in lowercase! ")

score = 0

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!! ")
    score += 1
elif answer.lower() != "yes":
    print("I'm sorry, that's not correct :/ ")
else:
    pass

answer = input("What does GPU stand for?: ")

if answer.lower() == "graphics processing unit":
    print("Correct!! ")
    score += 1
elif answer.lower() != "graphics processing unit":
    print("I'm sorry, that's not correct :/ ")
else:
    pass
    

answer = input("Is it possible to download RAM?: ")

if answer.lower() == "yes":
    print("Correct!! ")
    score += 1
elif answer.lower() != "yes":
    print("Technically incorrect, but correct!")
else:
    pass

answer = input("What, is the circumference, of a moose! ")

if answer.lower() == "i'm a ninja?":
    print("Correct!! ")
    score += 1
elif answer.lower() != "yes":
    print("Who would know amirite?")
else:
    pass
    
if score > 0:
    print("You got " + str(score) + " points!")
    print("Great job!")
elif score < 3:
    print("Not bad, try again! ")
else:
    pass






      



