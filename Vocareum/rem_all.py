def remove_all(substr, theStr):
    while substr in theStr:
        begin_at = theStr.find(substr)
        end_at = begin_at + len(substr)
        theStr = theStr[:begin_at] + theStr[end_at:]
        remove_all(substr, theStr)
    print(theStr)
    return theStr

remove_all('an', 'banana')
