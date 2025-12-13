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
        if self.is_working:
            print(self.name, 'is helping its handler ' + self.handler, 'walk')
        else:
            Dog.walk

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



class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "I'm a person and my name is " + self.name

class DogWalker(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    
    def walk_the_dogs(self, dogs):
        for dog_name in dogs:
            dogs[dog_name].walk()


class Hotel:
    def __init__(self, name):
        self.name = name
        self.kennel = {}

    def check_in(self, dog):
        if isinstance(dog, Dog):
            self.kennel[dog.name] = dog
            print(dog.name, 'is checked into', self.name)
        else:
            print('Sorry only Dogs are allowed in', self.name)

    def check_out(self, name):
        if name in self.kennel:
            dog = self.kennel[name]
            print(dog.name, 'is checked out of', self.name)
            del self.kennel[dog.name]
            return dog
        else:
            print('Sorry', name, 'is not boarding at', self.name)
            return None
        
    def barktime(self):
        for dog_name in self.kennel:
            dog = self.kennel[dog_name]
            dog.bark()

    def hire_walker(self, walker):
        if isinstance(walker, DogWalker):
            self.walker = walker
        else:
            print('Sory,', walker.name, 'is not a Dog Walker')

    def walking_service(self):
        if self.walker != None:
            self.walker.walk_the_dogs(self.kennel)


class Cat():
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name, 'Says, "Meow"')


    

# def test_code():
#     codie = Dog('Codie', 12, 38)
#     jackson = Dog('Jackson', 9, 12)
#     sparky = Dog('Sparky', 2, 14)
#     rody = ServiceDog('Rody', 8, 38, 'Joseph')
#     dude = FrisbeeDog('Dude', 5, 20)
#     kitty = Cat('Kitty')

#     hotel = Hotel('Doggie Hotel')
#     hotel.check_in(codie)
#     hotel.check_in(jackson)
#     hotel.check_in(rody)
#     hotel.check_in(dude)
#     hotel.check_in(kitty)

#     dog = hotel.check_out(codie.name)
#     print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
#     dog = hotel.check_out(jackson.name)
#     print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
#     dog = hotel.check_out(rody.name)
#     print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
#     dog = hotel.check_out(dude.name)
#     print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
#     dog = hotel.check_out(sparky.name)


# test_code()


# def test_code():
#     codie = Dog('Codie', 12, 38)
#     jackson = Dog('Jackson', 9, 12)
#     rody = ServiceDog('Rody', 8, 38, 'Joseph')
#     frisbee = Frisbee('red')
#     dude = FrisbeeDog('Dude', 5, 20)
#     dude.catch(frisbee)

#     codie.walk()
#     jackson.walk()
#     rody.walk()
#     dude.walk()

    # hotel = Hotel('Doggie Hotel')
    # hotel.check_in(codie)
    # hotel.check_in(jackson)
    # hotel.check_in(rody)
    # hotel.check_in(dude)

    # hotel.barktime()





def test_code():
    codie = Dog('Codie', 12, 38)
    jackson = Dog('Jackson', 9, 12)
    sparky = Dog('Sparky', 2, 14)
    rody = ServiceDog('Rody', 8, 38, 'Joseph')
    rody.is_working = True
    dude = FrisbeeDog('Dude', 5, 20)
    
    hotel = Hotel('Doggie Hotel')
    hotel.check_in(codie)
    hotel.check_in(jackson)
    hotel.check_in(rody)
    hotel.check_in(dude)

    joe = DogWalker('joe')
    hotel.hire_walker(joe)

    hotel.walking_service()

test_code()