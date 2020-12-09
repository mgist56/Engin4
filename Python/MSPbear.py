#MSP
#Meg Gist and Rowan Miller
#ʕノಡᴥಡʔノ︵┻━┻

import os

def game():
  guesses = []
  #array for the letters that have been guessed
  bearnumb = 0
  #easier to use a variable
  #than changing the number every time
  guessnumb = 7
  #number of "lives" Player 2 has

  #keep those out of the loop
  #otherwise they will reset as I have learned

  bear = ["ʕ","ノ","ಡ","ᴥ","ಡ","ʔ","ノ","︵","┻","━","┻"]
  bearjoin = " ".join(bear)
  #removes brackets and commas from bear
  print("Player 1, please enter a word.")
  word = input()

  wordarr = list(map(str, word))
  #changes the word into an array
  #map splits the word into letters

  scorearr = " ".join(list("_"*len(wordarr)))
  placearr = list("_"*len(word))

  #creates array same ammount of letters as word
  #and replaces each letter with underscores

  os.system('clear')
  #more effective than print("\n"*100)
  #even if Player 2 scrolls they won't find it

  print("Player 2, a word has been chosen.")
  print()
  print("There are",len(word),"letters.")
  print()
  print(scorearr)
  print()
  print("You have",(guessnumb),"guesses left.")
  #prints number of letters and guesses

  while 1 == 1:
    if "_" not in placearr:
    #checks to see if underscores are in placearr
    #if not, then Player 2 has won and can play again
      print("Player 2 wins! Play again?")
      print("Please press y and then Enter to play again.")
      play_again = input("Press n and then Enter to stop.")
      print()
      if play_again == "y":
        game()
        #runs the whole process over again from the top
      else:
        break 
        #stops the while loop, ending the code. 

    guess = input()

    os.system('clear')

    if guess in word:
      for place, letter in enumerate(wordarr):
      #for index, item in enumerate(choices):
        if letter == guess:
          placearr[place] = guess
          #replaces the guess place
          #with the actual letter

    else:
      guessnumb = guessnumb - 1
      bearnumb = bearnumb + 4

    print(" ".join(placearr))
    print()

    if guess in guesses:
      print("You have already guessed that letter.")
      print("Please guess a different letter.")
    else:
      guesses.append(guess)
      #only adds new letter if letter
      #has not already been guessed

    print("Guessed letters:"," ".join(guesses))
    print()
    print(bearjoin[0:bearnumb])
    #kind of wonky with the stages bear forms in
    #but matches ammount of possible guesses so 乁(ಠ_ಠ)ㄏ

    guess = " "
    #resets guess so that a new letter can be stored in it
    
    if guessnumb == 0:
    #if all of the guesser's lives are used up
      print()
      print("Sorry, you lose! Play again?")
      print("Please press y and then Enter to play again.")
      play_again = input("Press n and then Enter to stop.")
      print()
      if play_again == "y":
        game()
        #runs the whole process over again from the top
      else:
        break 
        #stops the while loop, ending the code.
      
game()
