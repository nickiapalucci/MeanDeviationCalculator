# import math module for square root calcuations
# import sys module for version check
import math, sys

def versionCheck() :
    if sys.version_info < (3, 4, 3) :
        sys.exit("Please run this program using Python version 3.4")

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
        except ValueError :
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
    versionCheck()
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

if __name__ == "__main__":
    main()
