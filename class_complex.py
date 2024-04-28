class complexl():
    def __init__(self,rl=0,img=0):
        self.real = rl
        self.img  = img

    def add(self,Z2):
        Z = complexl()
        Z.real = self.real + Z2.real
        Z.img = self.img + Z2.img
        return Z
    
    def display(self):
        print("Z= "+str(self.real) +" + "+ str(self.img) + "i")
    

Z1 = complexl(1,2)
Z2 = complexl(3,4)
Z3 = complexl()
Z3 = Z1.add(Z2)
Z1.display()
Z2.display()
Z3.display()