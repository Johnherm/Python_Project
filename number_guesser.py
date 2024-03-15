import random
top_of_range = input("Type a number: \n")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0 for the next time")
        quit()
else:
    print("Please a number for the next time")
    


random_number = random.randint(0,top_of_range)

guesses = 0

while True:
    guesses +=1
    user_guess = input("Make a guess: \n")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number for the next time")
        continue
    if user_guess == random_number:
        print("You got it! ")
        break
    elif random_number < user_guess:
        print("You guessed above number ")
    else:
        print("You guessed below number")

print("You guessed ",guesses,"time")


