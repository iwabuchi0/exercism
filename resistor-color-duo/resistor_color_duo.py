RESISTOR_COLORS_LIST = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
def value(colors):
    
    first_digit = RESISTOR_COLORS_LIST.index(colors[0]) * 10
    second_digit = RESISTOR_COLORS_LIST.index(colors[1])
    return first_digit + second_digit
          