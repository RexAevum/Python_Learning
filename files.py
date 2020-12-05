# opening a file
myFile = open("fruits.txt")

# printing info from file once open
print(myFile.read())
myFile.close()

# File cursor -> pointer in the file from where it starts to read until it reaches end of file or line
# if you try to print from file again without reseting the pointer or sving the info to a container
file = open("fruits.txt")
container = file.read()

# close the file once you are done working on it to clear it from memory and make sure there is no data loss
file.close() 
# if you try to read from file agin -> will give you an error
print(container)

# OPENING USING 'WITH'
with open("fruits.txt") as file:
    # write whatever you will do with the file and will close it automaticaly after all code under with is excecuted 
    container = file.read()


# FILEPATHS  - if files are not in the root directory of proiject
with open("Files/fruits.txt") as file:
    print(file.read())

# WRITING TO FILE 
# - when opening a file you can specify the mode (read, write, append)
with open("Files/writeToFile.txt", 'w') as myFile:
    # can write several times to same file
    # DONT FORGET THE NEW LINE
    myFile.write("Hello world!\n")
    myFile.write("This is me!\n")
# If you open an alredy existing file in write mode -> it will override whatever is in the file bofre the write

# APPEND TO FILE
with open("fruits.txt", 'a+') as file: # the + is for read/write 
    file.write("\nApple")
    # if you read after appending, the pointer will be at the end of the file -> to move it back
    file.seek(0) # puts pointer at the start of the file
    print(file.read())

# if file is oppen in append+ (a+) mode, the cursor is at the end of the file, so you have to move it back up to start
# if you want to first read what's in the file




# Example 
def getChar (item, file):
    with open(file) as openFile:
        return openFile.read().count(item)

