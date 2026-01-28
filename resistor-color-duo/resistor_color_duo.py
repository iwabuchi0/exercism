def value(colors):
    resistor_color_list = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    a = []
    
    for i in colors[0:2]:
        number_color = str(resistor_color_list.index(colors[0])) + str(resistor_color_list.index(colors[1]))
        return int(number_color)
          