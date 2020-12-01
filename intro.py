import datetime
print( "Current time: ", datetime.datetime.now())

#Store into a varialbe 
nowTime = datetime.datetime.now()
print(nowTime)
num = 2
print(nowTime, " ", num, "\n")

# Types
x = 10 # int
y = '10' # str - can use both '10' or "10"
z = 10.0 #float

print(type(x), type(y), type(z))

# Lists
list1 = [10.0, 0, "OK"] # can have different types in the same list!!!
print(list1)

# Using built in functions
student_grades = [75, 30, 99, 79]

gradeSum = sum(student_grades)
# This comand will count the nr of times the provided item is found
gradeCount = student_grades.count(1)
# To get item count in container need to use built in len() command
# Can also be written using the builtins of pythone
gradeCount2 = len(student_grades)
print('\nGrades:', gradeCount, '\n', gradeCount2, '\n')
# get mean

mean = gradeSum / gradeCount2
print(mean, '\n')

# List vs dictionary 
exampleList = [1, 2, 3] # this is a list -> square brackets and each value is sepperated with comma

exampleDictionary = {"Nr 1: " : 9.1, "Nr 2: " : 6.9, "Nr 3: " : 2.1}
print(exampleDictionary, '\n')

# Tuple in dictionary 
day_temperatures = {1 : (), '2' : (), '3' : ()}
print(day_temperatures, '\n')