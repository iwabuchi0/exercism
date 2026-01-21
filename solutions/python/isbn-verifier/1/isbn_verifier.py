def is_valid(isbn):
    texto_limpo = isbn.replace("-", "")
    
    if len(texto_limpo) != 10:
        return False
    
    S = 10
    soma = 0
    
    for i in texto_limpo:
        if i == "X":
            if S == 1:
                valor = 10
            else:
                return False
        elif i.isdigit():
            valor = int(i)
        else:
            return False
        
        soma += valor * S
        S -= 1
    return soma % 11 == 0
        


