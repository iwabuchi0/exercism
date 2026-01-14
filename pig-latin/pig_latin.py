def translate(text):
    rule1 = "xr", "yt","a", "e", "i", "o", "u"
    rule2 = "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"
    for item in text:
        if item.startswith(rule2):
           item.strip(rule2)
           item = item + "ay"
           return item
        if item.startswith(rule1):
            item += "ay"
            return item         
