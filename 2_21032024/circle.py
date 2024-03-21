import math

class Circle:
    def __init__(self, radious:int):
        self.radious = radious
    
    @property
    def get_area(self)->float:
        return math.pi*self.radious**2
    
    @property
    def get_diameter(self):
        return 2*self.radious

    @property
    def get_circ(self)->float:
        return 2*math.pi*self.radious