# How to create lists quickly 
temps = [75, 23, 55]

# comprehention
newTemp = [temp / 10 for temp in temps]
print(newTemp)

# comprehention with if statement 
temps = [75, 23, 55, -9999] # want to ignore -9999, so that it is not modified 
ignore = -9999 # what value to ignore
newTempIf = [temp / 10 for temp in temps if temp != ignore]
print(newTempIf)

# comprehention with if/else conditional
# if/else conditional is before the for loop
newTempIfElse = [temp / 10 if temp != ignore else 0 for temp in temps]
print(newTempIfElse)