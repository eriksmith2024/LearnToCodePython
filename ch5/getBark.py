
def get_bark(weight):
    if weight > 20:
        return'WOOF WOOF'
    else:
        return ' woof woof' 

def make_greeting(name):
    return 'Hi ' + name + '!'

def compute(x, y):
    total = x + y
    if total > 10:
        total = 10
    return total 

def allow_access(person):
    if person == 'Dr Evil':
        answer = True
    else:
        answer = False
    return answer

codies_bark = get_bark(40)
print("Codie's bark is", codies_bark)

print(get_bark(20))
print(make_greeting('Speedy'))
print(compute(2,3))
print(compute(11,3))
print(allow_access('Codie'))
print(allow_access('Dr Evil'))