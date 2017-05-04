def mirror(text):
    mirror_text = text + reverse(text)
    return mirror_text


def reverse(text):
    reverse_text = text[::-1]
    return reverse_text


# Don't copy these tests into Vocareum
from test import testEqual
testEqual(mirror('good'), 'gooddoog')
testEqual(mirror('Python'), 'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'), 'aa')
