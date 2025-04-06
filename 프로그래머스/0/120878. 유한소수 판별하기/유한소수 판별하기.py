from fractions import Fraction

def solution(a, b):
    divide_ab = Fraction(a,b)
    d = divide_ab.denominator
    
    while d % 2 == 0:
        d /= 2
    while d % 5 == 0:
        d /= 5
        
    if d == 1:
        return 1
    else:
        return 2