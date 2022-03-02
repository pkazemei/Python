class Ninja:
    energy=0
    health=0
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet
    def walk(self):
        print(Pet.play(self))
        return self
    def feed(self):
        print(Pet.eat(self))
        return self
    def bathe(self):
        print(Pet.noise(self))
        return self

class Pet:
    energy=0
    health=0
    def __init__(self, name, type, tricks):
        self.name=name
        self.type=type
        self.tricks=tricks
    def sleep(self):
        self.energy+=25
        return(f"Pet's energy increased by {self.energy}")
    def eat(self):
        self.energy+=5
        self.health+=10
        return(f"Pet's energy increased by {self.energy} & health by {self.health}")
    def play(self):
        self.health+=5
        return(f"Pet's health increased by {self.health}")
    def noise(self):
        return(f"Your pet is growling at you")

Babri=Pet("Babri", "Cat", "Go to bed")
Ryu=Ninja("Ryu", "Hayabusa", "Greenies", "Tuna", Babri)

Ryu.feed().walk().bathe()