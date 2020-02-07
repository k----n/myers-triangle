import pytest
from validTriangle import triangleType


def testEquilateral():
    assert triangleType(6, 6, 6) == 'Equilateral Triangle'


def testIsosceles():
    assert triangleType(6, 6, 5) == 'Isosceles Triangle'

    assert triangleType(5, 6, 5) == 'Isosceles Triangle'

    assert triangleType(6, 5, 5) == 'Isosceles Triangle'


def testScalene():
    assert triangleType(4, 5, 6) == 'Scalene Triangle'


def testInvalid():
    # Use the triangle inequality theorem
    # x >= (y + z) ==> !triangle
    # y >= (x + z) ==> !triangle
    # z >= (x + y) ==> !triangle

    assert triangleType(10, 2, 2) == 'Invalid Triangle'
    assert triangleType(2, 5, 2) == 'Invalid Triangle'
    assert triangleType(2, 2, 5) == 'Invalid Triangle'


def testError():
    # Triangle sides should be in (0,10]

    with pytest.raises(ValueError):
        triangleType(25, 19, 25)

    with pytest.raises(ValueError):
        triangleType(19, 25, 25)

    with pytest.raises(ValueError):
        triangleType(25, 25, 19)

    with pytest.raises(ValueError):
        triangleType(-1, 5, 5)

    with pytest.raises(ValueError):
        triangleType(5, -1, 5)

    with pytest.raises(ValueError):
        triangleType(5, 5, -1)

    with pytest.raises(ValueError):
        triangleType(0, 5, 5)

    with pytest.raises(ValueError):
        triangleType(5, 0, 5)

    with pytest.raises(ValueError):
        triangleType(5, 5, 0)
