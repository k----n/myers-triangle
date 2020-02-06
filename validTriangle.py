def triangleType(x, y, z):
    
    #Check if x, y, z inputs represent a valid triangle

    if "all sides length are equal":
        return 'Equilateral Triangle'
    elif "two sides length are equal and one is different":
        return 'Isosceles Triangle'
    else:
        return 'Scalene Triangle'