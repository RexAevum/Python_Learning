# Getting user input in python and string formatting

# To get user input command
name = input("Enter your name: ")
print(name)

# All inputs will be of type str, so if you will have to cast it to another type
# To cast
x = input("Enter number: ")
temp1 = int(x)
temp2 = float(x)
# Need to be carfull, since if user inputs a float and you try to cast it as int -> will give you an error

#------------------------------------------------------------------------------------------------------------

# To format the user input
userIn = input("Enter info: ")
# To print text with variable in python
userIn = int(2)
formatMessage = "You entered %s" % userIn

# or
formatMessage2 = "You entered {}".format(userIn)

# New method since python 3.6
formatMessage36 = f"You entered {userIn}"

print(formatMessage)

# For multiple variables
x = 20
y = 100
text = "First is %s and then comes %s" % (x, y)
print(text)

text36 = f"First is {x} and then comes {y}"
print(text36)