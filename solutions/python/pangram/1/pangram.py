import string
def is_pangram(sentence):
    alfabeto = set(string.ascii_lowercase)
    frase_letras = set(sentence.lower())
    return alfabeto.issubset(frase_letras)
