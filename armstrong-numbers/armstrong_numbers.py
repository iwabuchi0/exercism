#%%
def is_armstrong_number(number):
    size = len(str(number))
    total = 0

    for d in str(number):
        digito = int(d)
        total += digito**size
    return total == number


# %%
is_armstrong_number(153)

# %%
is_armstrong_number(111)
