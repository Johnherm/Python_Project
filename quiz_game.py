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

answer = input("What does GPU stand for? \n")  #GPU     

if answer == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for? \n")

if answer == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")
answer = input("What does PSU stand for? \n")

if answer == "power supply":
    print("Correct!")
else:
    print("Incorrect!")
