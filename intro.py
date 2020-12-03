import datetime
print( "Current time: ", datetime.datetime.now())

#Store into a varialbe 
nowTime = datetime.datetime.now()
print(nowTime)
num = 2
#print(nowTime, " ", num, "\n")

# Types
x = 10 # int
y = '10' # str - can use both '10' or "10"
z = 10.0 #float

print(type(x), type(y), type(z))

# Lists
list1 = [10.0, 0, "OK"] # can have different types in the same list!!!
#print(list1)

# Using built in functions
student_grades = [75, 30, 99, 79]

gradeSum = sum(student_grades)
# This comand will count the nr of times the provided item is found
gradeCount = student_grades.count(1)
# To get item count in container need to use built in len() command
# Can also be written using the builtins of pythone
gradeCount2 = len(student_grades)
#print('\nGrades:', gradeCount, '\n', gradeCount2, '\n')
# get mean

mean = gradeSum / gradeCount2
#print(mean, '\n')

# List vs dictionary 
exampleList = [1, 2, 3] # this is a list -> square brackets and each value is sepperated with comma

exampleDictionary = {"Jeff" : 9.1, "Kyle" : 6.9, "Chig" : 2.1}
#print(exampleDictionary, '\n')

# Tuple in dictionary 
day_temperatures = {1 : (), '2' : (), '3' : ()}
#print(day_temperatures, '\n')

# Modifying a list
listToMod = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# add itme
listToMod.append(7)
# remove item
listToMod.remove(7)

# To access a specific range of indexes in the container 
print(listToMod[1:3]) # The range can be longer than the lenght of the list, will just cover till last item

# To access from a specific index to end of list
listToMod[3:]

# Negative indexes on a list of strings
wordList = ['hello', 'bye', 'stay']
temp = wordList[0][2] # the first square will get the 0 index item and the second square will get the letter at index 2 
#print(temp) 

# Dictionaries use keys in the square brakets
temp = exampleDictionary["Jeff"]
print(temp) 

# coverting between data structures
# From tuple to list

data = (1, 2, 3)
list(data)

# From list to tuple

data = [4, 5, 6]
tuple(data)

# From list to dictionary
data = [["name", "Jhon"], ["surname", "Smith"]] # its a list of lists, each internal list contains 2 variables - the key and the value
dict(data)