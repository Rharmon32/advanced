import random

#A function do shuffle all the characters of a string
def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

#Main program starts here
uppercaseLetter1 = chr(random.randint(65, 90))  #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2 = chr(random.randint(65, 90))  #Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
uppercaseLetter3 = chr(random.randint(65, 90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1 = chr(random.randint(97, 122))   #Generate a random lowercase letter (based on ASCII code)
lowercaseLetter2 = chr(random.randint(97, 122))   #Generate a random lowercase letter (based on ASCII code)
lowercaseLetter3 = chr(random.randint(97, 122))   #Generate a random lowercase letter (based on ASCII code)
lowercaseLetter4 = chr(random.randint(97, 122))   #Generate a random lowercase letter (based on ASCII code)

#Generate password using all the characters in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4
password = shuffle(password)

#output
print(password)
