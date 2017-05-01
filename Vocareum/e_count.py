
def analyze_text(text):
    """Gives a count of all the alphanumeric characters and how many are 'e'"""
    clean_text = text.lower()
    counter = 0
    e_count = 0
    for char in clean_text:
        if char.isalpha():
            counter += 1
            if char == 'e':
                e_count += 1
#import pdb; pdb_settrace
    e_percentage = (e_count/counter) * 100
    print(e_percentage)
    print("The text contains {} alphabetic characters, of which {} ({}%) are 'e'.".format
          (counter, e_count, e_percentage))

"""This code also works though clunky it passes ThinkPython test excercise
    while above does not"""
def analyze_text(text):
    """Gives a count of all the alphanumeric characters and how many are 'e'"""
    clean_text = text.lower()
    counter = 0
    e_count = 0
    for char in clean_text:
        if char.isalpha():
            counter += 1
            if char == 'e':
                e_count += 1
    e_percentage = float(e_count/counter) * 100
    print(e_percentage)
    print("The text contains", str(counter),"alphabetic characters, of which",
         str(e_count), "("+str(e_percentage)+"%) are 'e'.")
    x = ("The text contains " + str(counter) + " alphabetic characters, of which "
         +str(e_count) + " ("+str(e_percentage)+"%) are 'e'.")
    print(type(x))
    print(x)
    return x

text1 = 'Eeee'
analyze_text(text1)
text2 = 'Blueberries are tasteee!'
text3 = 'Wright\'s book, Gadsby, contains a total of 0 of that most common symbol ;)'
analyze_text(text2)
analyze_text(text3)
