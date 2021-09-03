#This program will determine the grade a user
#Gets on a test

#Named Constant 
perfect_score = 100

#Get a Test score from the user. 
test_score = int(input('Enter your test score: '))

if test_score == perfect_score:
    print('Excellent! You earned a', perfect_score)

else:
    if test_score >= 90:
        print('Congrats, you have earned an A with the score', test_score)

    else:
        if test_score >= 80 and test_score < 90:
            print('Nice work you earned a B with the score', test_score)

        else:
            if test_score >= 70 and test_score < 80:
                print('You received a passing grade of', test_score)

            else:
                print('I am sorry, but you did not pass the test.')


    
