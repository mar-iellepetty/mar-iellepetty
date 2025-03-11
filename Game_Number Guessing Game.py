
from random import randint

def number_guessing_game():
    computer_number = randint(1,100)
    #Part 1: Start the game
    #Step 2.1: Computer first gets the number between 1 to 100
    print("Welcome to the Number Guessing Game!")
    print('The goal of the game is to guess the a random number between 1 to 100. To make it more fun, try to guess the number in the least amount of rounds possible.')

    #Part 2: Loop
    round_number = 1

    user_number = int(input("Input number: "))

    while computer_number != user_number:
        if computer_number < user_number: 
            print('wrong. you are over. guess again')
        if computer_number > user_number: 
            print('wrong. you are under. guess again')
        user_number = int(input("Input number: "))
    
        round_number += 1

    print(f'Congratulations! You have guessed the number correctly! You have guessed the number in {round_number} rounds! ^0^')

    #2.1 input the number.

    

    #2.2.2: While loop condition is true (computer number equals to user number) then end game
    #2.2.1: While loop, if the number is higher print 'You are over. Guess again' else, 'You are under. Guess again'
        
        



#when game ends, print congratulations your number of guesses = 

number_guessing_game()


#Notes: -----------------
# my_function-snake case
# myFunction - camel case
#input is 


#question ----
# argument, function, 
#input function - do more research


#hurdles: 
'''
- Stop caputalizing stuff
- def function
- sometimes, ending the function can be outside the loop, don't need to always put if not/ false, sometimes it will end on its own; hence, use part 3
- when using a function can do 2 things
from (function imported) import (library)
OR
(library).(function imported)

- number conversion from string to int


- end a program in any coding language: ctrl+c
- debugging, you add print statement in any place in place of any function (manual) or just use debugger

   

 '''