"""
Using the Python language, have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word.
Words will be separated by only one space.
"""

myString = "i ran there"


def LetterCapitalize(str):
    newString = ""
    newString += myString[0].upper() #cap the first letter of the string 
    i = 1 
    while i < len(myString):
        if myString[i] == " ": #find the spaces
            newString += myString[i]
            newString += myString[i + 1].upper() #cap the next letter
            i += 2
        else:
            newString += myString[i]
            i += 1
            
    return newString
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print(LetterCapitalize(myString))
