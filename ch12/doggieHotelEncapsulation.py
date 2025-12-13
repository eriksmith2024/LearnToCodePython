class Frisbee:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "I'm a " + self.color + " frisbee"


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight > 29:
            print(self.name, 'says "WOOF WOOF"')
        else:
            print(self.name, 'says "woof woof"')

    def walk(self):
        print(self.name, 'is walking')

    def human_years(self):
        return self.age * 7

    def __str__(self):
        return "I'm a dog named " + self.name


class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        super().__init__(name, age, weight)
        self.handler = handler
        self.is_working = False

    def walk(self):
        print(self.name, 'is walking')

    def bark(self):
        if self.is_working:
            print(self.name, 'says "I can\'t bark, I\'m working"')
        else:
            super().bark()

    def __str__(self):
        return "I'm a service dog named " + self.name + " and I help " + self.handler


class FrisbeeDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.frisbee = None

    def bark(self):
        if self.frisbee is not None:
            print(self.name, 'says, "I can\'t, I have a frisbee in my mouth"')
        else:
            super().bark()

    def walk(self):
        if self.frisbee is not None:
            print(self.name, 'says, "I can\'t walk, I\'m playing Frisbee"')
        else:
            super().walk()

    def catch(self, frisbee):
        self.frisbee = frisbee
        print(self.name, 'caught a', frisbee.color, 'frisbee')

    def give(self):
        if self.frisbee is not None:
            frisbee = self.frisbee
            self.frisbee = None
            print(self.name, 'gave back', frisbee.color, 'frisbee')
            return frisbee
        else:
            print(self.name, "doesn't have a frisbee")
            return None

    def __str__(self):
        description = "I'm a dog named " + self.name
        if self.frisbee is not None:
            description += " and I have a frisbee"
        return description
    

def test_code():
    dude = FrisbeeDog('Dude', 5, 20)
    blue_frisbee = Frisbee('blue')

    print(dude)
    dude.bark()
    dude.catch(blue_frisbee)
    dude.bark()
    print(dude)
    frisbee = dude.give()
    print(frisbee)
    print(dude)

# test_code()

# --- TEST CODE MATCHING EXPECTED OUTPUT ---

# red_frisbee = Frisbee("red")

# dude = FrisbeeDog("Dude", 5, 32)
# codie = Dog("Codie", 3, 18)
# jackson = Dog("Jackson", 6, 25)
# rody = ServiceDog("Rody", 8, 38, "Joseph")
# duse = FrisbeeDog("Duse", 4, 30)

# dude.catch(red_frisbee)
# codie.walk()
# jackson.walk()
# rody.walk()
# duse.catch(red_frisbee)
# duse.walk()

class Hotel:
    def __init__(self, name):
        self.name = name
        self.kennel_names = []
        self.kennel_dogs = []

    def check_in(self, dog):
        if isinstance(dog, Dog):
            self.kennel_names.append(dog.name)
            self.kennel_dogs.append(dog)
            print(dog.name, 'is checked into', self.name)
        else:
            print('Sorry only Dogs are allowed in', self.name)

    def check_out(self, name):
        for i in range(0, len(self.kennel_names)):
            if name == self.kennel_names[i]:
                dog = self.kennel_dogs[i]
                del self.kennel_names[i]
                del self.kennel_dogs[i]
                print(dog.name, 'is checked out of', self.name)
                return dog
        print('Sorry', name, ' is checked out of', self.name)
        return None

class Cat():
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name, 'Says, "Meow"')

def test_code():
    codie = Dog('Codie', 12, 38)
    jackson = Dog('Jackson', 9, 12)
    sparky = Dog('Sparky', 2, 14)
    rody = ServiceDog('Rody', 8, 38, 'Joseph')
    dude = FrisbeeDog('Dude', 5, 20)
    kitty = Cat('Kitty')

    hotel = Hotel('Doggie Hotel')
    hotel.check_in(codie)
    hotel.check_in(jackson)
    hotel.check_in(rody)
    hotel.check_in(dude)
    hotel.check_in(kitty)

    dog = hotel.check_out(codie.name)
    print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
    dog = hotel.check_out(jackson.name)
    print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
    dog = hotel.check_out(rody.name)
    print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
    dog = hotel.check_out(dude.name)
    print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
    dog = hotel.check_out(sparky.name)


test_code()