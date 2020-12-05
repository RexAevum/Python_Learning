# A small app to combine multiple inputs
# Program need to keep asking for input until \end is entered, each new sentence has to start with capital

# Try 1
newStr = ""

def addStr(resultStr):
    newStr = resultStr
    while True:
        tempStr = input("Say something: ")
        if tempStr == r"\end":
            break
        else:
            newStr = newStr + tempStr.title() + ' '
    return newStr
        
#newStr = addStr(newStr)
print(newStr)

# Try 2 - i like better

def makeNewStr ():
    newStr = ""
    questions = ('how', 'why', 'what', 'if', 'where') #Has to be a tuple (cannot be changed)
    while True:
        userIn = input("Say something: ")
        if userIn == r'\end':
            return newStr
        else:
            # To check if str ends with a stop
            if (userIn.startswith(questions)):
                userIn = userIn + '?'
            elif (userIn[-1] != '.'):
                userIn = userIn + "."
            elif (userIn[-1] == ' ' and userIn[-2] != '.'):
                userIn = userIn[:-1] + '.'
            newStr = newStr + userIn.title() + " " 

print(makeNewStr())

# Given solution
# Func to format the senctence 
def sentence_maker(phrase):
    interrogatives =  ('how', 'why', 'what', 'if', 'where') 
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "%s?" % capitalized
    else:
        return "%s." % capitalized

# Main - loop to get input from user and add to results
results = []
while True:
    userIn = input('Say something: ')
    if userIn == r'\end':
        break
    else:
        results.append(sentence_maker(userIn))

# ' '.join(list) - will join the str with the defined char inbetween
#print(' '.join(results))