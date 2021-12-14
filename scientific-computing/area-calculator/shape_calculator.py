class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    

    def set_width(self, new_width):
        self.width = new_width
    

    def set_height(self, new_height):
        self.height = new_height


    def get_area(self):
        return self.width ** 2 + self.height ** 2


    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        pic = ("*"*self.width +"\n")*self.height
        return pic

    def get_amount_inside(self, rect):
        w = rect.width
        h = rect.height

        x = self.width // w
        y = self.height // h
        return x*y
