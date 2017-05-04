def pig_latin(word):
    #if len(word) > 2:
    pig_word = word[1:] + word[0] + 'ay'
    #print(pig_word)
    return pig_word
    # else:
    #     return False

def translate_pig(phrase):
    for char in phrase:
        while len(phrase) > 2:
            phrase = phrase + ' '
            x = phrase.find(' ')
            word_x = pig_latin(phrase[:x])
            #print(word_x)
            print(word_x + ' ', end='')
            phrase = phrase[x+1:]
    #print('\n')

translate_pig("purple monkey dishwasher")
#pig_latin("purple")
