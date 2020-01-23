#!/usr/bin/env python3
import sys, random #Uses the 'random' function that is built into python

assert sys.version_info >= (3,7), "This script requires at least Python 3.7" #Tells the user what version of python is needed to user this file


print('Greetings!') #Prints Greetings in the terminal when the program is run
colors = ['red','orange','yellow','green','blue','violet','purple'] #Colors saves a list of colors to be used later
play_again = '' #Place holder for the answer of the user after being asked if they want to play again 
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'): #This creates a loop that will keep running as long as the user says yes they want to keep playing
    match_color = random.choice(colors) #Chooses a random color out of the list saved in color
    count = 0 #Starts the original guess count to 0 
    color = '' # Place holder where the players color guess will be stored to be checked later
    while (color != match_color): #This is another loop that will occur if the user does not guess the correct color the computer chose the first time
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #reads the input from color and runs it through all spelling conditions
        count += 1 #Adds count + 1 depending on how many times the user had to guess
        if (color == match_color): # will trigger this if statement if the color guessed is the one the computer chose
            print('Correct!') # Correct will be printed in the terminal and it will exit out of the if else clause
        else: #If the conditions are not me in the first if statement it will check the else statment
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # Will print this statement when the player does no guess the correct color and add to its count
    
    print('\nYou guessed it in {} tries!'.format(count)) #Will trigger when the user chooses the correct color and will pull the count from the count int and add it under guesses

    if (count < best_count): # will check if count guessed is less than the other guessed count
        print('This was your best guess so far!') #Will compare counts and tell the user if this was their bestround
        best_count = count #will replace count after every time the secound while loop is played

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #Asks the player if they want to play again and will send the input into the first while loop

print('Thanks for playing!') #Will trigger when the user says they do not want to play again