full = False                   # start with 'full' set to False (box not full yet)

donations = []                 # create an empty list to store donated toys
full_load = 45                 # the box should hold 45 toys

toys = ['robot', 'doll', 'ball', 'slinky']   # the list of toy types we can add

# keep looping until the box is marked as full
while not full:
    # go through each toy in the list, one by one
    for toy in toys:
        donations.append(toy)              # add the toy to the donations list
        size = len(donations)              # check how many toys are now in the box
        if(size >= full_load):             # if we’ve reached at least 45 toys
            full = True                    # stop: the box is now full

# once full, print the final number of toys and the list of toys
print('Full with', len(donations), 'toys')
print(donations)


