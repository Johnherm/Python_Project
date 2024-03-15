print("Welcome to my computer quiz!")
playing = input("Do you want to play? \n")
if playing != "yes":
    print(" Okay! Have a good time! ")
    quit()
print("Okay! Let's play:) ")
answer = input("What does CPU stand for? \n")
score = 0
if answer == "central processing unit":
    score +=1
    print("Correct!")
else:
    print("Incorrect!")
answer = input("What does GPU stand for? \n")  #GPU     
if answer.lower() == "graphics processing unit":
    score +=1
    print("Correct!")
else:
    print("Incorrect!")
answer = input("What does RAM stand for? \n")
if answer.lower() == "random access memory":
    score +=1
    print("Correct!")
else:
    print("Incorrect!")
answer = input("What does PSU stand for? \n")

if answer.lower() == "power supply":
    score +=1
    print("Correct!")
else:
    print("Incorrect!")

print("Your score is  ",score)
print("So you got "+ str((score/4*100)),"%.")
