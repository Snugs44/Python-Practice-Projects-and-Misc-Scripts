print("Let's play guess the animal!")

secret_word = "monkey"
guess = ""
guess_counter = 0
out_of_guesses = False
guess_limit = 5

print("Hint, it really likes bananas!")

while guess != secret_word and not(out_of_guesses):
    if guess_counter < guess_limit:
        guess = input("Enter guess ")
        guess_counter += 1
        print(guess_counter)
    else:
          out_of_guesses = True

if out_of_guesses:
    print("No more guesses left, please input .50 C to continue playing!")
elif guess == secret_word.lower():
    print("You got it!")