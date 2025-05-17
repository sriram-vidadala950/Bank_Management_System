class circle:
    def __init__(self,radius):
        self.radius = float(radius)
    def area_of_circle(self):
        return f"Area of circle = {3.14*self.radius**2}"
    def perimete_of_circle(self):
        return f"perimeter of circle = {2*3.14*self.radius}"
area = circle("5.432")
print(area.area_of_circle())
print(area.perimete_of_circle())


