def translate(text):
    rule1 = "xr", "yt","a", "e", "i", "o", "u"
    rule2 = "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"
    rule3 = "qu"
    rule4 = "y"
    new_phrase = []
    for item in text:
        if item[0] == 'q' and item[1] == 'u':
            new_world = item[2:] + "quay"
            new_phrase.append(new_world)
            continue
        if item[0:2] == 'xr' or item[0:2] == 'yt' or item[0] in rule1:
            new_world = item + "ay"
            new_phrase.append(new_world)
            continue
        if item[0] == 'y' or item[1] == 'y' or item[2] == 'y':
            new_world = item[1:] + item[0] + "ay"
            new_phrase.append(new_world)
            continue    
