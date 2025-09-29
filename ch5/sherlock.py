balance = 10500
camera_on = True

def steal(balance, amount):
    global camera_on
    camera_on = False
    if(amount < balance):
        balance = balance - amount

    return amount
    camera_on = True

proceeds = steal(balance, 1250)
print('Criminal: you stole', proceeds)    

print('The global variable balance is still:',balance)


print('This was because the balance used in the def steal function was a different local variable hence sherlock was not worried')