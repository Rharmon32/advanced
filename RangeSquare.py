#This program uses a loop to display a
#table showing the numbers 1 through 10
#and ther squares.

#Print the table headings.
print('Number\tSquare')
print('---------------')

#Print the number 1 through 10
#and their squares
for number in range(1, 10):
    square = number**2
    print(number, '\t', square)

