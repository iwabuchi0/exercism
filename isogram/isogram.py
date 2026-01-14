def is_isogram(string):
    phrase_lower = string.lower()
    clean_phrase = phrase_lower.replace("-", "").replace(" ", "")
    phrase_no_repetition = set(clean_phrase)
    return len(phrase_no_repetition) == len(clean_phrase)
    
            
            

