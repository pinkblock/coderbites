'''
Using the Python language, have the function SimpleSymbols(str) take the str 
parameter being passed and determine if it is an acceptable sequence by either 
returning the string true or false. The str parameter will be composed 
of + and = symbols with several letters between them (ie. ++d+===+c++==a) and 
for the string to be true each letter must be surrounded by a + symbol. 
So the string to the left would be false. The string will not be empty and 
will have at least one letter.

Use the Parameter Testing feature in the box below to test your code with 
different arguments
'''

def SimpleSymbols(str): 
	for i in str:
		print i
	return str    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SimpleSymbols("--+d+----")  