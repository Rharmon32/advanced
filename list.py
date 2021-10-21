#This program takes a sentence and turns it into a list.
#Then turns each word into uppercase letters.

#Get the variables
sentence = "This example has five words."
words = sentence.split()

print(words)

# 
for index in range(len(words)):
	words[index] = words[index].upper()

	
print(words)
