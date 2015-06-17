'''
Using the Python language, have the function simple_symbols(str) take the str
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
    """ceck that data pass in has at least on letter and is not empty 

    >>> check_legit("---")
    False
    >>> check_legit("-a-")
    '-a-'
    >>> check_legit("")
    'this string had len 0'
    >>> check_legit("-2-")
    False
    """

    if len(str) == 0:
        return "this string had len 0"

    for i in str:
        if i.isalpha():
            return str   
    else:
        return False


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
    if str == False:
        return False

    for i, c in enumerate(str):
        if c.isalpha():
            if i - 1 >= 0 and i + 1 <= (len(str) - 1):
                letter_stamps += str[i - 1], str[i], str[i + 1]
            else:
                return False

    return letter_stamps

def check_for_plus_and_alpha(list):
    """ check that all characters in list are alpha or +

    >>> check_for_plus_and_alpha('[a]')
    True
    >>> check_for_plus_and_alpha('[3, a, +]')
    False
    >>> check_for_plus_and_alpha('[+, G, +]')
    True
    >>> check_for_plus_and_alpha('[+, 7, +]')
    False
    >>> check_for_plus_and_alpha('[a, a, a]')
    True

    """

    special_characters = "~!@#$%^&*()_{}|:<>?`-=\;'./'"

    if list == False:
        return False
    else:
        for i in list:
            # print i
            if i in special_characters:
                return False
            if i.isdigit():
                return False
        return True

def simple_symbols(str):
    """check that str is made up of [alpha, "+", "="] and at least one alpha
    return true if each alpha is surrounded by a "+" symbol
    else return false

    >>> simple_symbols('+a+=')
    True
    >>> simple_symbols('==+c+=')
    True
    >>> simple_symbols('==+c+=+c+')
    True
    >>> simple_symbols('+9+=')
    False
    >>> simple_symbols('')
    False
    >>> simple_symbols('+++')
    False
    >>> simple_symbols('===')
    False
    >>> simple_symbols('a=')
    False
    """

    return check_for_plus_and_alpha(letter_cutter(check_legit(str)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print simple_symbols('+e+==')

'''
1. When the input was "+d+" your output was incorrect.
2. When the input was "+d===+a+" your output was incorrect.
3. When the input was "aaaa" your output was incorrect.
4. When the input was "+z+z+z+" your output was incorrect.
5. When the input was "+a=" your output was incorrect.
6. When the input was "2+a+a+" your output was incorrect.
7. When the input was "+a++" your output was incorrect.
8. When the input was "+z+z+==+a+" your output was incorrect.
9. When the input was "==a+" your output was incorrect.
10. When the input was "b" your output was incorrect.
'''