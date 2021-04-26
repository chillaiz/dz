class fraction:

    def __init__(self, chislitel, znamenatel):
        self.chislitel = chislitel
        if znamenatel == 0:
            raise ValueError("nepravilno")
        self.znamenatel = znamenatel

    def add(self, other):
        chislitel = self.chislitel * other.znamenatel + self.chislitel * other.znamenatel
        znamenatel = self.znamenatel * other.znamenatel
        return fraction(chislitel, znamenatel)

    def sub(self, other):
        if self.znamenatel == other.znamenatel:
            chislitel = self.chislitel - other.chislitel
            znamenatel = self.znamenatel
            return fraction(chislitel, znamenatel)

        else:
            if self.znamenatel != other.znamenatel:
                chislitel = self.chislitel * other.znamenatel - other.chislitel * self.znamenatel
                znamenatel = self.znamenatel * other.znamenatel
                return fraction(chislitel, znamenatel)

    def div(self, other):
        chislitel = self.chislitel * other.znamenatel
        znamenatel = self.znamenatel * other.chislitel
        return fraction(chislitel, znamenatel)


    def mult(self, other):
        chislitel = self.chislitel * other.chislitel
        znamenatel = self.znamenatel * other.znamenatel
        return fraction(chislitel, znamenatel)


Fraction1 = fraction(1, 2)
Fraction2 = fraction(1, 8)
fraction3 = Fraction1.div(Fraction2)
print(fraction3.chislitel)
print("--")
print(fraction3.znamenatel)
