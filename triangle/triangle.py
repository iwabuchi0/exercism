def equilateral(sides):
    a, b, c = sides[0], sides[1], sides[2]
    true_triangle = a + b >= c and b + c >= a and  a + c >= b and a!= 0 and b!=0 and c!=0
    if true_triangle:
        return a == b == c
    else: 
        return False

def isosceles(sides):
    a, b, c = sides[0], sides[1], sides[2]
    true_triangle = a + b >= c and b + c >= a and  a + c >= b and a!= 0 and b!=0 and c!=0
    if true_triangle:
        return a == b or a ==c or c==b
    else: 
        return False


def scalene(sides):
    a, b, c = sides[0], sides[1], sides[2]
    true_triangle = a + b >= c and b + c >= a and  a + c >= b and a!= 0 and b!=0 and c!=0
    if true_triangle:
       return a != b != c != a
    else: 
        return False
