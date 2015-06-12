"""
Using the Python language, have the function SimpleAdding(num) add up all the numbers from 1 to num.
For the test cases, the parameter num will be any number from 1 to 1000.
"""

number = 140


def SimpleAdding(num):
  output = 0 
  for i in range(0, num + 1):
    print(i) 
    output += i
  
  return output
  
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print(SimpleAdding(number))
