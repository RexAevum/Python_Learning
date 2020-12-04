# How to implement loops in python
demoList = [1, 2, 3, 4, 5]

# FOR LOOP - runst until all items are exausted
# Through a list
for item in demoList:
    print(item)

# Through a dictionary
students = {"Marry" : 9.2, "Jhon" : 10.2, "Face" : 0.1}

# You can cast the pair into a single variable
# the .items() will grab the whole pair
# the .values() will grab only the value
# the .keys() will grab only the keys

for pair in students.items(): 
    print("Name is %s and score is %s" % (pair[0], pair[1]))

# can use more than one variable to asighn to
for key, value in students.items():
    print("Name is %s and score is %s" % (key, value))

# WHILE LOOP - runs as long as the conditional is true
a = 0
while a == 0:
    print(a)
    a = a + 1

# Using break and continue statements
# break -> breakes out of the loop
# continue -> moves on the the top of the loop/goes to the next iteration item
a = True
while True: # will loop forever, since always True
    if a == False:
        break
    else:
        a = False
        continue