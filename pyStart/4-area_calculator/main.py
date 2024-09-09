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
    
    # 5. Create a function that generates a pictorial representation of the shape
    def display(self):
        w_line = "*" * self.w
        h_line = f"\n{w_line}" * (self.h - 1)
        pic = w_line + h_line
        if self.w > 50 or self.h > 50:
            return "Too big for picture"
        else:
            return pic + "\n"
    # 6. Create a fn which returns the amount of times the given shape could fit into the other
    def get_amount_inside(self, other):
       return self.area() // other.area() # the quotient of the tow areas gives us the amount of times the one quad can fit into the other
    # 10. Create a function which generates a string that returns the details of the quadrilateral
    def __str__(self):
        return f'Rectangle(width={self.w}, height={self.h})'
class Square(Rectangle): # the square child class of the rectangle class
    # 7. Initialise the square child class with the w and h set to side
    def __init__(self, side):
        super().__init__(w=side, h=side)
        self.side = side
    # 8. Create a variable in square child class that sets side to a new variable
    def set_side(self, new_side):
        self.side = new_side
        return new_side
    def __str__(self):
        return f'Square(side={self.side})'
    
quad1 = Rectangle(7, 3)
quad1.set_h(1)
quad1.set_w(4)
print(quad1.display())

quad2 = Square(4)
print(quad2.display())

quad1.set_h(8)
quad1.set_w(16)
print(quad1)
print(quad2)