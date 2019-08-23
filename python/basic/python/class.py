
# class Dog():
#     #Calss object attribute
#     species = 'mammal'
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name

#     def bark(self,numb):
#         print("woof {x} number is {n}".format(x = self.name, n = numb))

# doggy = Dog('huskie', 'tommy')

# print(doggy.name)
# doggy.bark(5)

#attributes and methods
class math():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius

    def get_circumference(self):
        cir = self.pi*self.radius*2
        print(cir)

mycircle = math(300)

print(mycircle.pi)
print(mycircle.radius)
mycircle.get_circumference()

#inheretence

class Animal():
    def __init__(self):
        print("Animal Class Created")
    def who_am_i(self):
        print ("I am an animal")
    def eat(self):
        print("I am eating veggies")

# my_animal = Animal()


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)                                                                                                                                               
        print('Dog created')
    
    def bark(self,numb):
        print("woof number is {n}".format(n = numb))

my_dog = Dog()

my_dog.who_am_i()

my_dog.bark(5)


class Doggy():
    def __init__(self, name):
        self.name = name 

    def speak(self):
        print (("{n} says Woof !").format(n = self.name))

bux = Doggy("Bux")
bux.speak()

class Cat():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(("{n} says meow !").format(n = self.name))

felix = Cat("Felix")
felix.speak()


for i in [bux, felix]:
    print(i.speak())
   
def sound(pet):
    print(pet.speak())

sound(felix)