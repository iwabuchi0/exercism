RULE1 = ("xr", "yt","a", "e", "i", "o", "u")
RULE2 = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
RULE3 = ("qu")
RULE4 = ("y")

def translate(text):
    words_list = text.split()
    new_phrase = []

    for word in words_list:
        if word.startswith(RULE1):
            new_phrase.append(word + 'ay')
            continue
    return ' '.join(new_phrase)


