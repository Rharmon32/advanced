#This program converts the speeds 60 kph
#Through 130 kph (in 10 kph increments)
#to mph

#Get constants
START_SPEED = 60   #Starting Speed
END_SPEED = 131    #Ending Speed
INCREMENT = 10     #Speed Increment
CONVERSION_FACTOR = .6214  #Conversion Factor

#Print the table headins
print('KPH\tMPH')
print('--------')

#Print the speeds.
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(kph, '\t', format(mph, '.1f'))
