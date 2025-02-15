print("---------------------------------Welcome to the Harry Potter Quiz Game-----------------------------------------")

playing=input("Do you want to play the game? (y/n): ")
print(playing)
if playing.lower() !="y":
    quit()
print("Ok.... Let's playing")

score=0
#question 1
answer = input("What is Alastor Moody’s nickname?: ")
if answer.lower() =="madeye moody":
    print("Congratulations! You got it!")
    score += 1
else:
    print("Sorry, that's not a right answer")

#question 2
answer = input("Who is Harry Potter’s godfather?: ")
if answer.lower() =="sirius black":
    print("Congratulations! You got it!")
    score += 1
else:
    print("Sorry, that's not a right answer")

#question 3
answer = input("What type of animals is Ron Weasley most scared of?: ")
if answer.lower() =="spiders":
    print("Congratulations! You got it!")
    score += 1
else:
    print("Sorry, that's not a right answer")

#question 4
answer = input("Who does Harry Potter marry?: ")
if answer.lower() =="ginny weasley":
    print("Congratulations! You got it!")
    score += 1
else:
    print("Sorry, that's not a right answer")

#question 5
answer = input("What is Tom Riddle’s middle name? ")
if answer.lower() =="marvolo":
    print("Congratulations! You got it!")
    score += 1
else:
    print("Sorry, that's not a right answer")

#question 6
answer = input("Which platform at London Kings Cross would you need to be on to catch a train to Hogwarts? ")
if answer.lower() =="platform 9 3/4":
    print("Congratulations! You got it!")
    score += 1
else:
    print("Sorry, that's not a right answer")

#question 7
answer = input("What position does Harry play on the Quidditch team? ")
if answer.lower() =="seeker":
    print("Congratulations! You got it!")
    score += 1
else:
    print("Sorry, that's not a right answer")

#question 8
answer = input("Who is the headmaster of Hogwarts? ")
if answer.lower() =="albus dumbledore":
    print("Congratulations! You got it!")
    score += 1
else:
    print("Sorry, that's not a right answer")

#question 9
answer = input("What is the name of Voldermort's pet snake? ")
if answer.lower() =="nagini":
    print("Congratulations! You got it!")
    score += 1
else:
    print("Sorry, that's not a right answer")

#question 10
answer = input("What kind of creatures run Gringotts bank? ")
if answer.lower() =="goblins":
    print("Congratulations! You got it!")
    score += 1
else:
    print("Sorry, that's not a right answer")

answer = input("What does the potion Felix Felicis do? ")
if answer.lower() =="makes you lucky":
    print("Congratulations! You got it!")
    score += 1
else:
    print("Sorry, that's not a right answer")

print("You got " + str(score) +  " question correctly.")
print("You got " + str((score/11)*100) +  "%")