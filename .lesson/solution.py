# Title: H Specimen - Water Quality
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

