answer = input("Hello! Welcome to this game! Do you want to play a game? \n")
score = 0
if answer.lower() == "yes":
    print("Okay! Let's begin! \n ")
else:
    quit()



answer = input("What is the your first work in this university? \n")      # GETTING GRADE 4
if answer.lower() == "getting grade 4":
    score +=1
    print("You are correct \n")                                               
elif answer.lower()  == "getting grade 4":
    print("please write the correct your plan! \n")
else:
    print("Incorrect\n")



answer = input("What is the your second work in this university? \n")  # TO BE A MECHANICAL ENGINEER
if answer.lower() == "to be a mechanical engineer":
    score +=1
    print("You are correct\n")
else:
    print("Incorrect\n")


answer = input("What is the your third work in this university? \n")   # TO BE A SOFTWARE ENGINEER
if answer.lower() == "to be a software engineer":
    score +=1
    print("You are correct\n")
else:
    print("Incorrect\n")


answer = input("What is the your forth work in this university?\n ")   # TE BE A GRAPHICS DESIGNER
if answer.lower() == "to be a graphics designer":
    score +=1
    print("You are correct \n")
else:
    print("Incorrect \n")


answer = input("What is the your fifth work in this university?\n ")   # TO SPEAK ENGLISH FLUENTLY
if answer.lower() == "to speak English fluently":
    score +=1
    print("You are correct \n")
else:
    print("Incorrect \n")


answer = input("What is the your sixth work in this university?\n ")   # TO BUILD MY MUSCLE
if answer.lower() == "building my muscle":
    score +=1
    print("You are correct \n")
else:
    print("Incorrect \n")

answer = input("What is the your seventh work in this university?\n ")   # TO BE BEST FOR FAMILY AND FRIENDS
if answer.lower() == "to be best man for my friends and my family":
    score +=1
    print("You are correct \n")
else:
    print("Incorrect \n")


answer = input("What is the your eighth work in this university?\n ")   # TO BE HIGH STATUS WITH FLIRTING TECHNIQUES
if answer.lower() == "high status with flirting":
    score +=1
    print("You are correct \n")
else:
    print("Incorrect \n")


if score == 8:
    print("Wow this is amazing! you get all the answer. So know what you want in this campus. Please keep going you will get it in short time later. Because you know what you want exactly\n")
    print("You got "+ str((score/8)*100) + "%.")
else:
    print("You got "+ str((score/8)*100) + "%. \n")
