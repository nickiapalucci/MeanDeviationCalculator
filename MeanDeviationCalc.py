# Students Name = Nick Iapalucci

# Date = December 4, 2014

# Assignment 10.2, #10.9
# Write a program that prompts the user to enter a list of numbers, and
# displays the mean and standard deviations of these numbers
# using custom functions

# Honor Code: I pledge that this program represents my own program code.
# I received help from no one in designing and debugging my program.

# import math module for square root calcuations
import math

def welcome() :
    print("\n\nWelcome to Mean and Standard Deviation Calculator!\n\n"
          "This program will ask you to enter a set of numbers,\n"
          "and then calculate the Mean and Standard Deviation\n"
          "of your entries.\n\n")

def getNumbers() :
# Preset variables
    done = False
    count = 0
    numbers = list()

# Data entry loop
# Allows for any blank or non float to break loop
    while not done :
        value = input("Please enter a number, or leave blank if finished, \n"
            "and press [ENTER] ")
        try :
            value = float(value)
        except :
            done = True
            break
        count += 1
        numbers.append(value)
    return numbers

def mean(numbers) :
    mean = sum(numbers) / len(numbers)
    return mean

def deviation(numbers, CalcMean) :
    StanDev = 0
    for i in numbers :
        StanDev += (i - CalcMean) ** 2
    StanDev /= (len(numbers) - 1)
    StanDev = math.sqrt(StanDev)
    return StanDev

def showResults(CalcMean, CalcDeviation) :
    print ("\nThe mean is ", CalcMean, "\n")
    print("The standard deviation is ", CalcDeviation, "\n")

def main() :
    welcome()
    numbers = getNumbers()
# Check to see if list is empty.  Abort if it is.
# (an empty list will crash the Calc functions)
    if len(numbers) != 0 :
        CalcMean = mean(numbers)
        CalcDeviation = deviation(numbers, CalcMean)
        showResults(CalcMean, CalcDeviation)
    else :
        print("\nNo entry was made.\n")

main()
