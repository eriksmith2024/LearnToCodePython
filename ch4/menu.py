menu = []
menu.append('Burger')
menu.append('Sushi')

print('\n', menu, '\n')

del menu[0]
print(menu, '\n')


menu.extend(['BBQ', 'Tacos'])
print('\n', menu, '\n')

menu.append(['Burger', 'Ribs'])
print('\n', menu, '\n')

# append = add one item to the list even if that is multiple items in a list they will be added as one item
# extend = add many things to the list that are then seperate items that can be iterated over  


# below contatenation of two lists does the same as extend
menu = menu + ['Pizza', 'Fries']
print('\n', menu, '\n') 

menu.insert(1, 'Stir Fry')
print('\n', menu, '\n')