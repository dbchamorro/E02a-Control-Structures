
# E02a-Control-Structures

Let's start experimenting with some Python code! This is a set of exercises for MSCH-C220; they should give you the tools to help build your first game.
 
This exercise assumes that you have already installed Python, GitHub Desktop, and VS Code, and that you have already created a GitHub account. If that is not the case, please refer to previous exercises.

This repository contains several files that you will need to alter to complete the assignment. Fork this repository (instructions below) and edit the files. Commit and push the changes back to GitHub and turn in the URL to your repository on Canvas.

Comments in Python are marked by a # sign (for single-line comments) or three matching quotation marks (''' or """) if a comment requires more than one line. They should also appear in a different color in VS Code. The Python Interpreter ignores comments, so you can safely include any information you want there.

*If you wish your exercise to be graded, please edit the LICENSE file (add the current year and your name).*

## This program asks the user to guess 'my' favorite color. 

Edit README.md to answer the following questions:
  
Commit your changes and push them back to the repository.
- Open main01.py. Before running it, what do you expect this program to do?
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
  ## The program closed after it recieved my answer.
  - What do you think the program did with what you typed in answer to the question?
## It read my answer and then closed the program.
- Open main02.py. Before running it, describe how this is different than main01.py.
## main02 saves your response and prints it.
  - What do you think the color = input() will do?
  ## It will save whatever the user types into it in to the int color
  - Run the program in the terminal and answer the question. Did the program do what you expected? 
  ## Color = input() was not added in main01
- Open main03.py. Before running it, describe how this is different than main02.py.
## There is an 'IF' funtion in main03 
  - What is happening on lines 9–12?
  ## The program is checking the input from line 8 and comparing it to the statements in the 'if' statement.
  - Why are lines 10 and 12 indented?
  ## They are apart of the of an if loop so they are within a function.
  - Run the program and answer the question. What happens if you don’t capitalize Red?
  ## The programs output is "Sorry try again."
  - What does this tell you about "color"?
  ## It tells me that color is case sensitive.
- Open main04.py. Before running it, describe how this is different than main03.py.
## This program takes into account the different spellings of red.
  - What problem is this trying to solve?
  ## 
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
  ## The error reoccures and "Sorry try again" is printed again.
- Open main05.py. What do you expect line 9 to do?
## It should fix the capitilizing issue with the spelling of red.
  - What problem is it trying to solve?
  ## It is trying to solve the problem of spelling with the word red.
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
  ## The error reoccurs.
 - Open main06.py. How is line 9 different than in main05.py?
 ## .strip is used after .lower
   - What would you guess .strip() is doing?
   ## I think it is fixing the spacing issues
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
   ## If you spell red with a space inbetween it (r e d) you will receive the error message.
 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
 ## This program seems to give hints when the user gets close to the color red. 
   - What is happening on line 12?
   ## 'elif' is apart of the if else statement
   - Run the program and answer the question.
 - Open main08.py. What is the purpose of line 9?
 ## 'While' creates a continuous loop until the program gets the answer he wants. 
   - Why are lines 10–17 indented?
   ## They are within a loop so they must be indented. 
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
   ## I think it would only ask the question once and keep running the input cursor.
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
 - Open main09.py. What is happening on line 13?
 ## Count is keeping track of how many times a user puts an input before they get the right answer.
   - What is the purpose of “count”?
   ## used as a place holder to keep count of how many inputs a user does
   - What is happening on line 21?
   ## it is printing what was in place in the count place holder and printing it to the user. 
   - Run the program.
 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
 - *Extra credit:* open main11.py. What is happening on lines 6-11?
 ## I think it is defining a function that cant be changed but can be called in other functions simplifying the code
  
Commit your changes and push them back to the repository.
 

---
