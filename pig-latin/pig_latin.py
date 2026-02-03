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
        elif word.startswith(RULE3):
            new_phrase.append(word[2:] + "quay")
        elif word [1:3] == "qu":
            new_phrase.append(word[3:] + word[:3] + "ay")
        elif word[1] == "y":
            new_phrase.append(word[1:] + word[0] + "ay")
        elif word[2] == "y":
            new_phrase.append(word[2:] + word[0:2] + "ay")
        elif word[0] in RULE2 and word[1] in RULE2 and word[2] in RULE2:
            new_phrase.append(word[3:] + word[0:3] + "ay")
        elif word[0] in RULE2 and word[1] in RULE2:
            new_phrase.append(word[2:] + word[0:2] + "ay")
        elif word.startswith(RULE2):
            new_phrase.append(word[1:] + word[0] + "ay")
    return ' '.join(new_phrase)


