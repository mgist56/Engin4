# Engin4
Engineering 4, baby. Documentation is here!
 
https://github.com/chssigma/Markdown_Cheatsheet
 
## Table of Contents
 
[Hello Python](#hello-python)
 
[01 Calculator](#01-calculator)
 
[02 Quadratic Solver](#02-quadratic-solver)
 
[03 Strings and Loops](#03-strings-and-loops)
 
[Python Challenge MSP](#python-challenge-msp)
 
[GPIO Pins: Bash](#gpio-pins-bash)
 
[GPIO Pins: Python](#gpio-pins-python)
 
[GPIO Pins: SSH](#gpio-pins-ssh)
 
[GPIO Pins: I2C](#gpio-pins-i2c)
 
[Headless](#headless)
 
[Hello Flask](#hello-flask)
 
[Pi Camera](#pi-camera)
 
## Hello Python
https://cvilleschools.instructure.com/courses/31073/assignments/258557?module_item_id=797037
 
The objective of this assignment is to create a simple dice roller program that picks a number from 1 to 6 when run in the python language.
 
### Takeaways
This assignment was pretty self explanatory to figure out, but I did glance at some other students’ codes in order to verify that my syntax was correct throughout the assignment. I added a “Fred” feature to my code which would choose a number from 1 to 999.
 
 
## 01 Calculator
https://cvilleschools.instructure.com/courses/31073/assignments/258563?module_item_id=797038
 
The objective of this assignment is to create a simple four-function calculator in the python language that gives the sum, difference, quotient, and modulo when given two numbers.
 
### Resources
I most heavily relied on other students in order to write this code: 
 
https://github.com/jfairch81/Engineering_4_Notebook-1/blob/main/Python/calculator
 
https://github.com/rmckee75/Engineering_4_Notebook/blob/main/Python/calculator.py
 
### Takeaways
The major obstacle I had to overcome when compiling this code was to mesh Reece and Jude’s code together in order to create a program that performed the way that I wanted to. In order to have the code work correctly, I had to fiddle around with the placement of certain lines.
 
 
## 02 Quadratic Solver
https://cvilleschools.instructure.com/courses/31073/assignments/258564?module_item_id=797039
 
The objective of this assignment is to create a quadratic function solver program that returns the roots of a function given the coefficients of that function in the python language.
 
### Takeaways
One new python feature that I encountered while compiling this program was the square root function, which was helpful to use instead of trying to use an operation to simplify the numbers. Additionally, the round function was especially helpful in this assignment when working with longer numbers.
 
 
## 03 Strings and Loops
https://cvilleschools.instructure.com/courses/31073/assignments/258565?module_item_id=797042
 
The objective of this assignment is to create a program that splits a sentence into an array and then prints each element of the array with a symbol in place of spaces.
 
### Takeaways
This assignment definitely prepared me for the Python Challenge, as the .split() function and the for “thing” in “thing” loop were both heavily relied upon in that assignment. Whenever I had an issue with understanding syntax or whatnot, I relied on Google and Stack Overflow.
 
 
## Python Challenge MSP
https://cvilleschools.instructure.com/courses/31073/assignments/258562?module_item_id=797043
 
The objective of this assignment is to create a “hangman” game program in the python language. This code was hijacked by Rowan Miller, although he did contribute a bit at the end.
 
### Resources
 
https://stackoverflow.com/questions/33854013/delete-user-input-python
 
https://stackoverflow.com/questions/53549973/how-to-replace-characters-within-string-with-dashes-except-spaces-python
 
https://stackoverflow.com/questions/29409273/how-to-split-string-without-spaces-into-list-of-integers-in-python
 
https://www.kite.com/python/answers/how-to-find-the-position-of-an-element-in-an-array-in-python
 
https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list
 
### Takeaways
This assignment took by far the most time and effort to complete. As is apparent from the extensive resource list (at least in comparison to some of the other assignments), I needed Google much more than in other assignments. For the program, instead of creating a “man-shaped piñata,” I used an amalgamation of two Japanese emoticons to depict a bear flipping a table. While attempting to navigate through the complexity of this code, I found it was useful to have a separate program running with short, experimental code to run a certain feature of the program.
 
 
## GPIO Pins: Bash
https://cvilleschools.instructure.com/courses/31073/assignments/258547?module_item_id=797044
 
The objective of this assignment is to blink two LEDs a total of 10 times using the Raspberry Pi and breadboard and to do so using Bash script.
 
### Resources
I googled Bash syntax things quite a few times because the language makes absolutely no sense to me, although there are not any specific links that I can attribute here.
 
### Takeaways
I did not like this assignment, simply because we had to use Bash script and we had to write in a terminal window, two things that absolutely suck. Bash syntax makes no sense to me, and, ideally, I would like to have very few instances in the future in which I have to use it again.
 
 
## GPIO Pins: Python
https://cvilleschools.instructure.com/courses/31073/assignments/258550?module_item_id=797045
 
The objective of this assignment is to blink two LEDs a total of 10 times using the Raspberry Pi and breadboard and to do so using Python.
 
### Resources
https://raspi.tv/wp-content/uploads/2013/07/Rev2-GPIO-bold-173x300.jpg
 
### Takeaways
For this assignment, I simply rewrote my Bash code from the previous assignment in Python. The only difference between the two assignments was the pin for the two LEDs, which is apparently different when you are writing in Python. I used the diagram linked above to see what pin the code should change to.
 
 
## GPIO Pins: SSH
https://cvilleschools.instructure.com/courses/31073/assignments/258551?module_item_id=797046
 
The objective of this assignment is to turn an LED on using the Raspberry Pi while connecting wirelessly to the Pi using its IP address.
 
### Takeaways
In this assignment, I was initially bamboozled by the program that we were using to connect to the Pi, but then I figured out that the “hostname” of the Pi is simply the IP address. Other than that, I think that it’s pretty neat that we can connect to the Pi’s remotely (and my dad thought that it was pretty cool too).
 
 
## GPIO Pins: I2C
https://cvilleschools.instructure.com/courses/31073/assignments/258549?module_item_id=797049

The objective of this assingment is to display accelerometer data on a screen using the Rasperry Pi while connecing wirelessly using the IP adress.

### Takeaways
This assingment took a lot longer than we originally anticipated and it is quite relieving to have finally completed it. We essentially had the correct code composed, but the lack of "disp.display()" prevented the screen from displaying the data. There was also an odd line that was hidden because of copying and pasting the code, so now we are synching with Replit.
 

## Headless
https://cvilleschools.instructure.com/courses/31073/assignments/258553?module_item_id=797050

The objective of this assingment is to display accelerometer data on a screen in a graph format on the Raspberry Pi while connecting wirelessly using the IP adress.

### Takeaways
This assignment took a lot longer than either Rowan and I anticipated or hoped that it would. Notes: Don't be afraid to mix multiple statments/loops together. That was definitely not the most aesthetically pleasing but it was effective and saved us hair pulling. It's a good idea to print out data when the visuals are weird. That makes it a whole lot easier to visualize where the proplem is and fix it.
 
 
## Hello Flask
https://cvilleschools.instructure.com/courses/31073/assignments/258554?module_item_id=797047
 
The objective of this assignment is to connect the Raspberry Pi as a web server and run a program through it.

### Takeaways
I do not have access to a working Raspberry Pi at this point in time, so I followed along while Rowan completed the assignment on his end. Setting up the Pi as a web server is very neat and I hope that we will be able to incorperate that element into our project when we get to it somehow.
 
 
## Pi Camera
https://cvilleschools.instructure.com/courses/31073/assignments/258559?module_item_id=797051
 
### Resources
 
### Takeaways
 
