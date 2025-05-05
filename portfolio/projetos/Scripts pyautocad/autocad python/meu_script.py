from pyautocad import Autocad, APoint
from math import *

acad = Autocad(create_if_not_exists=True)


l1 = acad.model.AddLine(APoint(0,0), APoint(0, 420))
l1 = acad.model.AddLine(APoint(0,420), APoint(594, 420))
l1 = acad.model.AddLine(APoint(0,0), APoint(420, 0))
l1 = acad.model.AddLine(APoint(0,0), APoint(420, 0))