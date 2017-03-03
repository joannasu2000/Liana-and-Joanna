intro1 = "KABOOOOOMMMM! Your neighboring country just dropped a nuclear bomb, Tsar Bomba on your nation. You have lost \
your family, a house, and all the supplies. The rescue army will come to save you in 7 days; however, you currently\
don't have water, food, or bedding. You need to find a way to survive during this 7 days! Are you ready to start your\
survival in this devastating situation?"


def day1S1(choice1):
    if choice1.lower() == "a":
        print "You just died."
        outcome = False
    elif choice1.lower() == "b":
        print "Great Choice!"
        outcome = True
    else:
        print "Your input is not valid."
        outcome = None
    return outcome

def day1s2(choice2):
    if choice2.lower() == "a":
        print "Great! You have food for the next day!"
        outcome2 = True
    elif choice2.lower() == "b":
        print "You died due to hunger and dehydration."
        outcome2 = False
    else:
        print "Your input is not valid."
        outcome2 = None
    return outcome2

print intro
Day1S1 = raw_input("Your house just got bombed, and severe radiation is decaying your body. Do you want to a. stay outside or b. go into the \
                   bunker?  Choose a or b.  ")

if day1S1(Day1S1) == False:
    print intro
elif day1S1(Day1S1) == True:
    print day1s2
else:
    print intro

Day1S2 = raw_input("You are on your way to the bunker and you saw this bag of bread and water. Do you want to a. pick it up or\
                   b. leave it there? Remember you don't have any food or drink. Choose a or b. ")

if day1s2(Day1S2) == True:
    print day1S3
elif day1s2(Day1S2) == False:
    print intro
else:
    print Day1S2

Day1S3 = raw_input("You arrived the bunker, and the sun has set. You feel extremely tired, but there is only filthy-looking\
                   bed in your sight. Do you want to a. go to sleep or b. stay up all night? Choose between a and b. ")

Day1S3_coffee = "In order to stay up all night, you need to play a game to get a coffee. "

coffee = "There are three people in front of you. They will each say a fact about computer programming. One person is right about the fact; the other two are wrong, they correct person has the normal conffee, the people who ha the wrong answers had poinsonous coffeee. You have to pick the one who is right."
a = "4.0 is a string."
b = "There are only two conditionals: If and Elif."
c = "5 is an interger."
A ="A. Person 1 says " + a
B = "B. Person 2 says " + b
C = "C. Perons 3 says " + c

def day1S3(ans):
    if ans.lower() == "a":
        print "Sleeping"
        #Move to Day2S1
        print "day2S1"
        outcome3 = True
    elif ans.lower() == "b":
        print Day1S3_coffee
        print a and b and c and A and B and C
        print day1S3_coffee
        outcome3 = False
    else:
        print "Your output is invalid."
        outcome3 = None
    return outcome3


def day1S3_coffee(ans):
    ans = raw_input("Choose A, B, or C ")
    if ans == "a":
        print "You failed to get a coffee. You just died due to fatigue."
    elif ans == "b":
        print "You failed to get a coffee. You just died due to fatigue."
    elif ans == "c":
        print "Congratulations! You just won the coffee."

from random import randint
doubles = 0
num1 = randint(1, 6)
num2 = randint(1, 6)
print "Are you ready to roll your dice? (Y)es or (N)o"
answer = raw_input()
you = num1 + num2
while answer.lower()[0] == "y":
    print "You rolled a", num1, "and a", num2, ". Your total is", you
    break
mag = num1 + num2
print "It is now the magician's turn to roll the dice. He rolled a ", num1, "and a", num2, ". His total is", mag
