# How to write functions in pythonm

# Command to define functiuon -> def
def calculateMean(myList) :
    # The next line is meant to be indented by 4 spaces or Tab
    temp_calc = sum(myList) / len(myList)
    return temp_calc

# Function call
tempMean = calculateMean([1, 2, 3, 4, 5])
print(tempMean)

# Conditionals - If/else 
def mean(x):
    # If 
    if type(x) == dict:
        # If x is a dictionary
        return sum(x.values()) / len(x)
    else:
        return sum(x) / len(x)

# AND & OR operators
def func1 (x):
    itemToReturn = None
    if x > 1 and x != 2: # both have to be true to return true
        itemToReturn = 1
    elif x == 2 or x == 20: # if one is true -> return true
       itemToReturn = 2
    else:
        itemToReturn = 0
    return itemToReturn

print(func1(0))