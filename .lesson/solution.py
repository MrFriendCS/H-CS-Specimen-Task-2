# Title: H CS Specimen Task 2
# Author: Mr Friend
# Date: 15 Nov 2021

# Import code for records
from dataclasses import dataclass


# Define the record
@dataclass
class beach:
    name: str = ""
    rating: int = 0


def getBeachData():
    '''
    Read in beach names and ratings from file
    '''

    # Declare local variables and datatypes
    line = ""
    name = ""
    rating = 0
    tempArray = [""] * 2
    beaches = [beach()] * 973

    # Connect to the file
    file = open("beachData.csv", "r")

    # Loop for 973 beaches
    for index in range(len(beaches)):

        # Read a line from the file
        line = file.readline()

        # Split line
        tempArray = line.split(",")

        # Get data
        name = tempArray[0].strip()
        rating = int(tempArray[1].strip())

        # Add a record to array
        beaches[index] = beach(name, rating)

    return beaches


def calcAverage(beaches):
    '''
    Calculate and return the average rating of the beaches tested
    '''

    # Declare local variables
    total = 0
    counter = 0
    average = 0.0

    # Start loop for each beach
    for index in range(len(beaches)):

        # Is rating of current beach not 5?
        if beaches[index].rating != 5:

            # Add current beach rating onto total
            total = total + beaches[index].rating

            # Increment counter
            counter = counter + 1

    # Calculate average to 1 dp
    average = round(total / counter, 1)

    return average


def displayAverage(average):
    '''
    Display the average rating of all beaches tested
    '''

    print("The average rating for all beaches tested is " + str(average))


def displayBeaches(beaches):
    '''
    Display all the beaches with a rating entered by the user
    '''

    # Declare local variables
    userRating = 0

    # Get rating from user
    userRating = int(input("Enter the rating to search for: "))

    # Only accept valid ratings (1-5)
    while userRating < 1 or userRating > 5:
        print("Rating must be a value from 1 to 5.")
        userRating = int(input("Enter the rating to search for: "))

    # Start loop for each beach
    for index in range(len(beaches)):

        # Is current rating = user rating?
        if beaches[index].rating == userRating:
            
            ''' Pre-refinement
            # Display beach name
            print(beaches[index].name)
            '''

            # Set position of space character to 0
            position = 0
            found = False

            # Repeat for each character in name
            for letter in range(len(beaches[index].name)):
                
                # Update position if first space character found
                if found == False and beaches[index].name[letter] == " ":

                    position = letter
                    found = True

            # Is position = 0?
            if position == 0:
                # Yes - Display whole beach name
                print(beaches[index].name)
            
            else:
                # No - Display beach name from first character to the position of the space
                beaches[index].name[0:position]


#
## Main program
#

# Declare global variables and datatypes
averageRating = 0.0
beachData = [beach()] * 973  # Array of record

# Read in beach names and ratings from file
beachData = getBeachData()

# Calculate and return the average rating of the beaches tested
averageRating = calcAverage(beachData)

# Display the average rating of all beaches tested
displayAverage(averageRating)

# Display all the beaches with a rating entered by the user
displayBeaches(beachData)
