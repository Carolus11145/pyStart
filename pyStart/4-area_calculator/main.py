class Rectangle:
    # 1. Initialise height and width attributes of the rectangle class
    def __init__(self, w, h):
        self.w = w
        self.h = h 
    # 2. Create the two functions for redefining the height and width
    def set_h(self, new_h): # sets height to a different value
        self.h = new_h
    
    def set_w(self, new_w): # sets the width to a different value
        self.w = new_w
        
    # 3. Create two methods which calculate the area and perimeter of the rectangle
    def area(self):
        a = self.w * self.h
        return a
    
    def perimeter(self):
        p = (self.w * 2) + (self.h * 2)
        return p
    
    # 4. Create a method which calculates the diagonal of the rectangle
    def diag(self):
        d = (self.w**2 + self.h**2) ** .5
        return d
    
quad1 = Rectangle(7, 3)
quad1.set_h(5)
quad1.set_w(10)
print(quad1.diag())