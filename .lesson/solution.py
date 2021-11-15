# Title: H Specimen - Water Quality
# Author: Mr Friend
# Date: 15 Nov 2021

# Import code for records
from dataclasses import dataclass

# Define the record
@dataclass
class beachData:
    name: str = ""
    rating: int = 0


def getBeachData():
    '''

    ''' 

    # Declare local variables and datatypes
    line = ""
    name = ""
    rating = 0
    tempArray = [""] * 2
    beaches = [beachData()] * 973

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
        beaches[index] = beachData(name, rating)

    return beaches




#
## Main program
#

# Declare global variables and datatypes
beaches = [beachData()] * 973  # Array of record

# Get beach data
beaches = getBeachData()

# Get average beach rating