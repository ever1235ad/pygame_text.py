class Point ():
    x = 0.0 
    y = 0.0
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("Point constructor")
        
    def Tostring(self):
        return "{X:" + str(self.x) + ",Y:" + str(self.y) + "}"

class Ellipse (Point):
    a_radious = 0.0
    b_radious = 0.0
    
    def __init__(self,x,y,a_radious,b_radious):
        super().__init__(x,y)
        self.a_radious = a_radious
        self.b_radious = b_radious
        print("Circle radious")
        
    def Bostring(self):
        return super().Tostring() + ",{" + "a_radious:" + str(self.a_radious) + ",b_radious:" + str(self.b_radious) + "}"

 
p = Point(20,30)
print(p.Tostring())
e = Ellipse(20,30,20,30)
print(e.Bostring())        
    
class Rectangle():
    def __init__(self,raidous,pi = 3.14159):
        self.radious = raidous
        self.pi = pi
        
    def CalcArea(self):
        area = self.pi * self.radious * self.radious
        return area
a = Rectangle(30)
area = a.CalcArea()
print(area)
        
