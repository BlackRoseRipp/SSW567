def findHypotenuse(a, b, c):
    hypotenuse = 0
    if a > b:
        if a > c:
            hypotenuse = a
        else:
            hypotenuse = c
    elif b > c:
        hypotenuse = b
    elif c != a and c != b:
        hypotenuse = c
    return hypotenuse

def isEquilateral(a, b, c):
    if a == b and b == c:
        return a == c
    return False

def isIso(a, b, c):
    hypotenuse = findHypotenuse(a, b, c)
    if hypotenuse == a:
        return b == c
    elif hypotenuse == b:
        return a == c
    elif hypotenuse == c:
        return a == b
    else: return False

def isRightTriangle(a, b, c):
    hypotenuse = findHypotenuse(a, b, c)
    if hypotenuse == a:
        return (b**2 + c**2) == a**2
    elif hypotenuse == b:
        return (a**2 + c**2) == b**2
    elif hypotenuse == c:
        return (b**2 + a**2) == c**2
    else: return False

def classify_triangle(a, b, c):
    if isRightTriangle(a, b, c):
        if isEquilateral(a, b, c):
            return "This is a right Equilateral triangle."
        elif isIso(a, b, c):
            return "This is a right Isosceles triangle."
        else:
            return "This is a right Scalene triangle."
    else:
        if isEquilateral(a, b, c):
            return "This is an Equilateral triangle without a right angle."
        elif isIso(a, b, c):
            return "This is an Isosceles triangle without a right angle."
        else:
            return "This is a Scalene triangle without a right angle."
