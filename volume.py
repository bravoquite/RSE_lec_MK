import pint

_si = pint.UnitRegistry()

def volume(length: float | pint.Quantity,
           width: float | pint.Quantity,
           height: float | pint.Quantity) -> pint.Quantity:
    """Calculate the volume of a rectangular prism.

    Formula: V = length * width * height.

    Parameters
    ----------
    length : float or pint.Quantity
        Length of an object, by default in meters (m).
    width : float or pint.Quantity
        Width of an object, by default in meters (m).
    height : float or pint.Quantity
        Height of an object, by default in meters (m).

    Returns
    -------
    pint.Quantity
        Volume of the object, in cubic meters (m^3).

    Raises
    ------
    ValueError
        If any dimension is negative.
    pint.errors.DimensionalityError
        If input has incompatible units.
    """

    if not isinstance(length, _si.Quantity):
        length = length * _si.m
    length = length.to(_si.m)

    if not isinstance(width, _si.Quantity):
        width = width * _si.m
    width = width.to(_si.m)

    if not isinstance(height, _si.Quantity):
        height = height * _si.m
    height = height.to(_si.m)

    if length.magnitude < 0 or width.magnitude < 0 or height.magnitude < 0:
        raise ValueError("Dimensions cannot be negative numbers")

    return length * width * height