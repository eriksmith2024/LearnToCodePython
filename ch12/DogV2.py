# --- Basic dog age calculator ---

dog_name = input("What is your dog's name? ")
dog_age = input("What is your dog's age? ")
human_age = int(dog_age) * 7
print('Your dog', dog_name, 'is', human_age, 'years old in human years')


# --- Dog class ---

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
        """Return age in human-equivalent years."""
        return self.age * 7


def print_dog(dog):
    """Print a dog's age and weight."""
    print(dog.name + "'s age is", dog.age, "and weight is", dog.weight)


# --- Using the Dog class ---

codie = Dog('Codie', 12, 38)
jackson = Dog('Jackson', 9, 12)

# You tried to pass strings into print_dog (which expects a Dog object)
# Fixed to instead print human years correctly.
print(codie.name, "is", codie.human_years(), "in human years")
print(jackson.name, "is", jackson.human_years(), "in human years")


# --- ServiceDog subclass ---

class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        super().__init__(name, age, weight)
        self.handler = handler

    def walk(self):
        print(self.name, 'is helping its handler', self.handler, 'walk')


rody = ServiceDog('Rody', 8, 38, 'Joseph')
print("This dog's name is", rody.name)
print("This dog's handlers name is", rody.handler)
print_dog(rody)
rody.bark()
rody.walk()

mystery_dog = ServiceDog('Mystery', 5, 13, 'Helen')
seeing_eye_dog = Dog('Chester', 6, 8)   # A Dog, not a class


# --- isinstance checks ---

if isinstance(mystery_dog, ServiceDog):
    print("Yup, it's a ServiceDog")
else:
    print('That is no ServiceDog')

if isinstance(mystery_dog, Dog):
    print("Yup, it's a Dog")
else:
    print("That is no Dog")

# This will ALWAYS be False because seeing_eye_dog is an instance, not a class.
if isinstance(mystery_dog, type(seeing_eye_dog)):
    print("Yup, it's the same type as seeing_eye_dog")
else:
    print("Nope, they are not the same type")
