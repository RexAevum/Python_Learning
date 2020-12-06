# MODULES

# Built in modules for certain operations
import time # used to suspend the program using time.sleeo()
import sys # imports the built in system modules

# To find the all the lib you have on the computer, can use python comand 
#
#     import sys
#     sys.prefix
#
# That willshow you where pythion is instaled, the librarries are in the site-packages folder

# can check if a path exists
import os
filePath = "Files/vegetables.txt"
exists = os.path.exists(filePath) # True if exists and false if does not exist
print(exists)

# You can instal 3rd party modules/libraries 
# The comand is 
# 
#       pip install {name of library}
#
# After installing the library you still need to import it
import numpy
import pandas
filePath = "Files/temps_today.csv"

while True:
    if os.path.exists(filePath):
        data = pandas.read_csv(filePath)
        print(data.mean())
    else:
        print("No file")
    time.sleep(10)
    break