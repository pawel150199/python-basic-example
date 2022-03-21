from cmath import sqrt
import random
import math
class Vector:
    def __init__(self,length = 3):
        self.length = length
        self.michas = []
    
    def generate(self):
        for i in range(self.length):
            self.michas.append(random.randint(0, 1000))
        return self.michas

    def read(self, vector):
        self.michas = []
        for i in vector:
            self.michas.append(i)
        self.length = len(self.michas)
        return self.michas

    def add(self, other):
        try:
            if len(self.michas) != len(other):
                raise ValueError
            else: 
                xd = []
                for i in range(self.length):
                    xd.append(self.michas[i] + other[i])
                return xd
        except ValueError:
            print("Kocham Kasie")

        
    def sub(self, other):
        try:
            if len(self.michas) != len(other):
                raise ValueError
            else: 
                xd = []
                for i in range(self.length):
                    xd.append(self.michas[i] - other[i])
                return xd
        except ValueError:
            print("Kocham Kasie")

    def mul(self, numb):
        for i in range(self.length):
            self.michas[i] = self.michas[i] * numb
        return self.michas
    def lengg(self):
        leng = 0
        for i in range(self.length):
            leng += i**2
        return math.sqrt(leng)
    def sum(self):
        suma = 0
        for i in self.michas:
            suma += i
        return suma
    
    def iloczyn(self, other):
        xd = 0
        for i in range(self.length):
            xd += other[i] * self.michas[i]
        return xd
    def str(self):
        print(str(Vector))

    def piri(self):
        print(Vector)

    def dostep(self, numb):

        try:
            if numb > self.length:
                raise ValueError
            else: return self.michas[numb]
        except ValueError:
            print('Zła liczba')
    def czyjest(self, numb):
        if numb in self.michas:
            return True
        else:
            return False

        
    



