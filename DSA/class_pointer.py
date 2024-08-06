class Cookie:
    def __init__(self,color):
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color=color


c1 = Cookie('Green')
print(c1.get_color())

c1.set_color('Blue')
print(c1.get_color())
