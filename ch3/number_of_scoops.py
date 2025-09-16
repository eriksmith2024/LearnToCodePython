import random

number_of_scoops = random.randint(0,5)


if number_of_scoops == 0:
    print('You didnt want any ice cream?')
    print('We have lots of flavors.')
elif number_of_scoops == 1:
    print('A single scoop for you coming up.')
elif number_of_scoops == 2:
    print('Oh two scoops for you.')
elif number_of_scoops >= 3:
    print('Wow thats a lot of scoops')
else:
    print("I am sorry I can't give you negtive scoops. ")