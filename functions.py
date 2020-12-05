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

# ----------------------------------------------------------------------------------------------------------

# Functions with multiple arguments and no default values
def newFunc (name, lastName): # arguments are seperated by a comma
    return name + ' ' + lastName

# Functions with multiple arguments and default values - the default value has to be after the non default or error
def newFuncDef (name, lastName = 'Smith'): # arguments are seperated by a comma
    return name + ' ' + lastName
# to call the function you can use keyword and non-keywoard arguments
#keywoard arguments - position of arguments do not matter
x = newFunc(lastName = 'adsf', name = 'assd')

# non-keyword - based on order
x = newFunc('1', '2')

# funtions with infinite* areguments - does not have a set number of variables
# need to use the '*args' in the argument for function definition -> generates a tuple of arguments
def mult(*args):
    return sorted([x.upper() for x in args])
        

# Key word arguments only
def meanKwargs (**kwargs): # to force keyword args you need to use '**' before the kwargs (can change)
    return kwargs

# if method needs kwargs then all passed arguments need to be with keywords -> creates a dictionary that hold the key and value
test = meanKwargs(a = 1, b = 2, c = 3)
# if you don't give the arguments it will result in error