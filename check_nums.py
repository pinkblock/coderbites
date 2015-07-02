def CheckNums(num1, num2):
    """takes both parameters being passed and returns the correct string
    if num2 > num1
    return "true"

    if num2 == num1
    return "-1"

    else
    return "false"

    >>> CheckNums(1, 2)
    'true'
    >>> CheckNums(2, 1)
    'false'
    >>> CheckNums(67, 67)
    '-1'
    """

    if num2 > num1:
        return "true"

    elif num2 == num1:
        return "-1"

    else:
        return "false"

# print CheckNums(raw_input())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print CheckNums(3, 122)
