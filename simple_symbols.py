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

def check_legit(str):
    """ check that data pass has at least on letter and thous is not empty 

    >>> check_legit("---")
    'error'
    >>> check_legit("-a-")
    -a-
    >>> check_legit("")
    'error'
    >>> check_legit("-2-")
    'error'
    """
    for i in str:
        if i.isalpha():
            return str
    else:
        return 'error'


def letter_cutter(str):
    """Iterate threw str find all letters if the letter is the first or last 
    character in the string return False else return the character befor it 
    the letter and the character after it.

    >>> letter_cutter("+a+")
    ['+', 'a', '+']
    >>> letter_cutter("3a3")
    ['3', 'a', '3']
    >>> letter_cutter("+a+==")
    ['+', 'a', '+']
    >>> letter_cutter("a+===")
    False
    >>> letter_cutter("==+a+")
    ['+', 'a', '+']
    >>> letter_cutter("===+a")
    False
    """

    letter_stamps = []
    # print(len(str))
    for i, c in enumerate(str):
        if c.isalpha():
            if i - 1 >= 0 and i + 1 <= (len(str) - 1):
                letter_stamps += str[i - 1], str[i], str[i + 1]
            else:
                return False

    return letter_stamps

def check_for_minus(list):
    """ check that all characters in list are letters or +

    >>> check_for_minus("-")
    False
    >>> check_for_minus("a")
    True
    >>> check_for_minus("1")
    False
    >>> check_for_minus("A")
    True
    >>> check_for_minus("4567$%^&")
    False
    >>> check_for_minus("+d+=3=+s+")
    True
    """

    if list == "error":
        return False
    else:
        for i in list:
            # print i
            if i == "-":
                return False
        return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print check_for_minus(letter_cutter(check_legit("+d=3=+s+")))