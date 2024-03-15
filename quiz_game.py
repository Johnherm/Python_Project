print("Welcome to my computer quiz!")
playing = input("Do you want to play? \n")
if playing != "yes":
    quit()
print("Okay! Let's play:) ")
answer = input("What does CPU stand for? \n")

if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")