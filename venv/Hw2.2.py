class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img


    def __add__(self, other):
        real = self.real + other.real
        img = self.img + other.img
        return Complex(real, img)
    def __str__(self):
        return  f"{self.real} + {self.img}i"

c1 = Complex(1, 2)
c2 = Complex(1, 4)
c3 = c1 + c2
c4 = c3 + c1
print(c4.real)
print(c4.img)