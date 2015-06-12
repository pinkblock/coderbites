"""
Using the Python language, have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm.
Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""

mystring = "fun times!"

def LetterChanges(str): 
  strL = str.lower()
  alphaL = "abcdefghijklmnopqrstuvwxyz"
  voules = "aeiou"
  strLout = ""
  tooReturn = ""
  
  for x in strL:
    if x.isalpha():
      for y in range(0, len(alphaL)):
        if x == alphaL[y]:
          strLout += alphaL[y + 1]
    else:
      strLout += x

  for letter in strLout:
    if letter in voules:
      tooReturn += letter.upper()
    else:
      tooReturn += letter

  return tooReturn

# keep this function call here  
# to see how to enter arguments in Python scroll down
print(LetterChanges(mystring))