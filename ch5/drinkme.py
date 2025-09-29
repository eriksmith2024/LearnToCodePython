def drink_me(param): # param becomes a local variable
    msg = 'Drinking ' + param + ' glass'  # msg & param local variables
    print(msg)
    param = 'empty'

glass = 'full' # global variable
drink_me(glass)
print('The glass is', glass)
drink_me('')
    