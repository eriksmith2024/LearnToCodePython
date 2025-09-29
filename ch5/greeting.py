greeting = " Greetings"

# def greet(name, message):
#     global greeting
#     print(greeting, name + '.', message)
# greet('June', 'See you soon')

def greet(name, message):
    global greeting
    greeting = 'Hi'
    print(greeting, name + '.', message)

greet('June', 'See you soon!')
print(greeting)