########### distance and slope of line
class Geometry():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def slope(self):
        slp = (self.coor2[1] - self.coor1[1])/(self.coor2[0]-self.coor1[0])
        print(slp)
        
    def distance(self):
        dis = (((self.coor2[1] - self.coor1[1]))**2 + ((self.coor2[0]-self.coor1[0]))**2)*0.5
        print (dis)

geo = Geometry((3,2),(8,10))

geo.slope()
geo.distance()


########Volume area of cylinder
class Cylinder():
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
    
    def volume(self):
        v = 3.14*(self.radius**2)*self.height
        print (v)
    def area(self):
        a = (2*3.14*self.radius*self.height) + (2*3.14*(self.radius**2))
        print(a)

cyl = Cylinder(2,3)

cyl.volume()
cyl.area()

###########
class Account():
    def __init__(self, owner, balance = 0):
        self.owner  = owner
        self.balance = balance 
    def deposit(self,dep):
        self.balance = self.balance + dep
        print ("Added {d}".format(d = dep))
    def withdrawl(self,wth):
        if self.balance >= wth:
            self.balance = self.balance - wth
            print("Withrew {w}".format(w = wth))
        else:
            print("not enough funds")
    
    def __str__(self):
        return f"Owner : {self.owner} \n Balance : {self.balance}"

bank = Account('Yogi',100)
bank.deposit(200)

