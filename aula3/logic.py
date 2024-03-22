import math

def list():
    number = int(input ("How many numbers would you like to input:\n"))
    list =[]
    for i in range(number):
        list.append(input(f"{i+1}º number:\n"))
    for i, num in enumerate(list):
        print (f"For index {i} the number is {list[i]}")

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

class Rectangle:

    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
    
    @property
    def get_area(self)->int:
        return self.width*self.height
    
    @property
    def get_perimeter(self)->int:
        return self.width*2+self.height*2


if __name__ == "__main__":
    main()