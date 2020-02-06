def triangleType(x, y, z):
    """
    Determine if the triangle is valid given the length of each side x,y,z.
    
    :param x: First side of triangle
    :param y: Second side of triangle
    :param z: Third side of triangle
    :returns: Whether a triangle is an 'Equilateral Triangle',
              'Isoceles Triangle', 'Scalene Triangle', or 'Invalid Triangle'
    :raises valueError: if the sides are not within (0,10]
    """
    if x == y == z:
        return 'Equilateral Triangle'
    elif x == y or y == z:
        return 'Isosceles Triangle'
    elif x != y and x != z and y != z:
        return 'Scalene Triangle'
    else:
        return 'Invalid Triangle'

