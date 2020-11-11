# Automatic Dice Roller
# Written by Meg Gist

from random import randint #for chosing things randomly

global result #variable to temporarily hold result

print ("Automatic Dice Roller")
print ("Press Enter to roll for numbers 1 - 6.")
print ("Type Fred then press Enter for numbers 1 - 999.")
print ("Type x to quit Automatic Dice Roller.")

while 1 == 1:
	userinput = input() #put here to prevent spammage of roll results
	if userinput == "x":
		print ("Thanks for rolling. Come again!")
		break #ends the running of the code
	elif userinput == "Fred": #reference to Guess the Number with Fred
		result = randint(1,999)
	else:
		result = randint(1,6) #regular dice options
	print (result)
