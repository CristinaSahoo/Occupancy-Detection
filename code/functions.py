import string

def to_snake_case(name):
    if name == name.upper():
        name = name.lower()
        return name
    if name[0] in string.ascii_uppercase:
        name = name.replace(name[0], name[0].lower())
    for letter in name:
        if letter in string.ascii_uppercase:
            name = name.replace(letter, '_' + letter.lower())
    return name