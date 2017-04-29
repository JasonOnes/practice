year = int(input("Give me a year!"))

def easter(year):
    if year < 1900 or year > 2099:
        print("That year is not within range! Try again")
        return None

    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    dateofeaster = 22 + d + e
    special_years = [1954, 1981, 2049, 2076]
    if year in special_years:
        dateofeaster = dateofeaster - 7
    if dateofeaster < = 31:
        print("In {} Easter is {} of March".format(year, dateofeaster))
    else:
        print("In {} Easter is {} of April.".format(year, dateofeaster))
    #print(dateofeaster)

easter(year)
