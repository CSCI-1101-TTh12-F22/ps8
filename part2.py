import random
import numpy as np
import matplotlib.pyplot as plt

# Function that tries to guess the number
# that was passed in as an argument using
#     ~ BINARY SEARCH ~
# it returns the number of guesses required
def binary_search(n):

    # start with the full range of numbers
    high = 100
    low = 1

    # guess the middle number
    theguess = (high+low)//2
    guesscount = 1

    # while your guess is wrong
    while theguess != n:

        # adjust the range appropriately and guess again
        if theguess > n:
            high = theguess - 1
        else:
            low = theguess + 1
        theguess = (high+low)//2
        guesscount += 1
    return guesscount


# Function that tries to guess the number
# that was passed in as an argument using
#     ~ SEQUENTIAL SEARCH ~
# it returns the number of guesses required
def sequential_search(n):

    # start at 1 and just keep going up
    # until you guess it correctly
    theguess = 1
    while theguess != n:
        theguess += 1
    return theguess


# Function that tries to guess the number
# that was passed in as an argument using
#     ~ RANDOM SEARCH ~
# it returns the number of guesses required
def random_search(n):

    # randomly guess between 1 and 100
    theguess = random.randint(1,100)

    # keep track of what numbers have already been guessed
    guessednumbers = [theguess]

    # while the current guess is wrong
    while theguess != n:

        # take another random guess but...
        theguess = random.randint(1,100)

        # ... make sure you haven't guessed that number before!
        while theguess in guessednumbers:
            theguess = random.randint(1,100)
        guessednumbers.append(theguess)
    return len(guessednumbers)



# Function that submits 1000 random numbers
# to the specified guessing function
# Returns a list of all the guess counts.
# Detailed instructions in the problem set description.

def simulateguessing(technique):
    allguesscounts = []

    ################################
    ### YOU DEFINE THIS FUNCTION ###
    ################################


    return allguesscounts
        


# Main function that prints out statistics about each
# simulation and then plots a histogram for each.
# Detailed instructions in the problem set description.
def main():

    ################################
    ### YOU DEFINE THIS FUNCTION ###
    ################################




main()
