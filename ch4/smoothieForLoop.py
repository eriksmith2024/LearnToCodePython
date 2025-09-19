smoothies = ['Coconut', 'Stawberry', 'Banana', 'Pineapple', 'Acai Berry']

for smoothie in smoothies:
    output = 'We serve ' + smoothie
    print(output)

range(5)
for i in range(5):
    print('\n Iterating through', i)

length = len(smoothies)
for i in range(length):
    print('Smoothie #' + str(i), smoothies[i])
