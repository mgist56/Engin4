#Python 01 Calculator
#Meg Gist
#Kudos to Jude Farichild
#and Reece McKee

def doMath(numb1, numb2, oper):
# defines function "doMath"
# reqires 3 inputs: 2 numbers & operation
	if oper == 'add':
		x = numb1 + numb2
		return str(x)
		# return is defined in function
	if oper == 'sub':
		x = numb1 - numb2
		return str(x)
	if oper == 'mult':
		x = numb1 * numb2
		return str(x)
	if oper == 'div':
		x = round((numb1 / numb2), 2)
		# "2" is the number to round to
		return str(x)
	if oper == 'mod':
		x = round((numb1 % numb2), 2)
		# technically, only div needed rounding
		return str(x)

while 1 == 1 : # loop that actually runs program
	a = int(input("Enter first number: "))
	# prompts user to input first number
	b = int(input("Enter second number: "))
	# prompts user to input second number

	oper = input("Enter operation (add/sub/mult/div/mod):")
	if oper in ('add', 'sub', 'mult', 'div', 'mod'):
		if oper == 'add': # addition
			print("Sum:\t\t" + doMath(a,b,'add'))
		elif oper == 'sub': # subtraction
			print("Difference:\t" + doMath(a,b,'sub'))
		elif oper == 'mult': # multiplication
			print("Product:\t" + doMath(a,b,'mult'))
		elif oper == 'div': # division
			print("Quotient:\t" + doMath(a,b,'div'))
		elif oper == 'mod': # modulo
			print("Modulo:\t\t" + doMath(a,b,'mod')) 
		else:
			("Error. Try again.")

	print("Press Enter to calculate again.")
	print("Press x then Enter to exit.")
	# prompting the user to go again or quit

	next = input(" ")
	# program will not run again without input
	if next == "x":
		print("Thanks for calculating. Come again!")
		break

