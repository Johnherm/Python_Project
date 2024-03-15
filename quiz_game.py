print("Welcome to my computer quiz!")
playing = input("Do you want to play? \n")
if playing != "yes":
    print("Have a good time! ")
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

print("You get ",score)
print("You got "+ str((score/4*100)),"%.")
