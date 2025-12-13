class Frisbee:
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return "I'm a "  + self.color + 'frisbee'



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
        print(self.name, 'is helping its handler', self.handler, 'walk')

    def __str__(self):
        return "I'm a service dog named " + self.name + " and I help " + self.handler

    def bark(self):
        if self.is_working:
            print(self.name, 'says " I can\'t bark, I\'m working"')
        else:
            Dog.bark(self)

class FrisneeDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None
    
    def bark(self):
        if self.frisbee != None:
            print(self.name, 'says, "I can\'t, I have a frisbee in my mouth"')
        else:
            Dog.bark(self)

    def walk(self):
        if self.frisbee != None:
            print(self.name, 'says, "I can\'t walk, Im playing Frisbee!"')
        else: 
            Dog.walk(self)
    
    def catch(self, frisbee):
        self.frisbee = frisbee
        print(self.name, 'caught a', frisbee.color, 'frisbee')

    def give(self):
        if self.frisbee != None:
            frisbee = self.frisbee
            self.frisbee = None
            print(self.name, 'give back', frisbee.color, 'frisbee')
        else:
            print(self.name, "doesn't have a frisbee")
            return None
        
    def __str__(self):
        str = "I'm a dog named " + self.name
        if self.frisbee != None:
            str = str + ' and I have a frisbee'
        return str



rody = ServiceDog('Rody', 8, 38, 'Joseph')
rody.bark()
rody.is_working = True
rody.bark()