import random
import sys

playerchoice = input("enter..\n1 for Rock\n2 for paper\n3 for scissor\n\n")
player=int(playerchoice)

if player < 1 or player > 3:
    sys.exit("you must enter 1,2,3.")

computerchoice= random.choice("123")
computer = int(computerchoice)

print("")
print("yourchoice" + playerchoice + ".")
print("computerchoice " + computerchoice + ".")
print("")

if player ==1 and computer ==3:
    print("you win")
elif player ==2 and computer ==1:
    print("you win")
elif player ==3 and computer ==1:
    print("you win")
elif player == computer:
   print("tie game")
   
else:
 print("computer win")
