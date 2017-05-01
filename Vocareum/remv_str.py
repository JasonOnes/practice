#from test import testEqual


def remove(substr,theStr):
    """Removes the first and only the first occurence of the substring
       from the string."""
    x = theStr.find(substr)
    if x < 0:
        return theStr
    y = len(substr)
    extract = theStr[x:x+y]
    new_string = theStr[:x] + theStr[x+y:]
    print(new_string)
    return new_string


remove('an', 'banana') #, 'bana')
remove('cyc', 'bicycle') #, 'bile')
remove('iss', 'Mississippi') #, 'Missippi')
remove('egg', 'bicycle') #, 'bicycle')
remove('oo', 'Yahoohoo') #, 'Yahhoo')
