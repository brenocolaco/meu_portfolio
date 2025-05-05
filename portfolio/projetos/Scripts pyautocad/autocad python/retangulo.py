from pyautocad import Autocad, APoint, aDouble
from math import *

acad = Autocad(create_if_not_exists=True)

sqp = aDouble(50, 150, 0, 50, 550, 0, 850, 550, 0, 850, 150, 0, 50, 150, 0)
sq1 = acad.model.AddPolyline(sqp)