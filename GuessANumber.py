#This program asks the user if they want to play a guessing game
#The user has to pick a number between 1 and 25
print('Let\'s play a guessing game')
print('Please choose y for yes or n for no.')

#Create a variable to control the loop
guess = input('Would you like to guess a number? ')

#Create a series of outcomes. 
while guess == 'y':
    number = int(input('Guess a number between 1 and 25: '))

    if number >= 1 and number <=25:
        print('Your number is within range!')
        print('You receive 1 point')
    else:
        if number > 25:
            print('Your number is too high.')
            print('You lose 1 point.')
            print('Please guess a number between 1 and 25.')

        else:
            if number < 1:
                  print('Your number is too low.')
                  print('You lose 1 point.')
                  print('Please guess a number between 1 and 25.')
                  
    #See if the user wants to guess another number.
    guess = input('Would you like to guess a number? ')
                  
                  
    
    
             
