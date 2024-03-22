class Circle:
    def __init__(self, radious:int):
        self.radious = radious
    
    def get_area(self)->float:
        return math.pi*self.radious**2
    
    def get_diameter(self):
        return 2*self.radious

    def get_circ(self)->float:
        return 2*math.pi*self.radious