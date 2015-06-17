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

def SimpleSymbols(str): #this name has been formated this way for coderbytes
    """check that str is made up of [alpha, "+", "="] and at least one alpha
    return true if each alpha is surrounded by a "+" symbol
    else return false

    >>> SimpleSymbols("+d+")
    True
    >>> SimpleSymbols("+d===+a+")
    True
    >>> SimpleSymbols(+z+z+z+")
    False
    >>> SimpleSymbols("+a=")
    False
    >>> SimpleSymbols("2+a+a+")
    False
    >>> SimpleSymbols("+a++")
    False
    >>> SimpleSymbols("+z+z+==+a+")
    False
    >>> SimpleSymbols("==a+")
    False
    >>> SimpleSymbols("b+")
    False
    """

    if str[0].isalpha():
        return False

    if str[-1].isalpha():
        return False

    for i in str:
        if str[i].isalpha():
            if str[i -1] == "+" and str[i + 1] == "+":
                return True
            else:
                return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print SimpleSymbols('+e+==')