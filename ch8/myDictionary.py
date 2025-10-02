my_dictionary = {}

my_dictionary['Jenny'] = '867-5309' 
my_dictionary['Paul'] = '555-1201' 
my_dictionary['David'] = '321-6617'
my_dictionary['Jamie'] = '771 - 0091'

my_dictionary['Paul'] = '443-0000'

phone_number = my_dictionary['Jenny']
print("Jenny's number is", phone_number)

my_dictionary['age'] = 27
my_dictionary[42] = 'answer'
my_dictionary['scores'] = [92, 87, 99]

del my_dictionary['David']

if 'Jenny' in my_dictionary:
    print('Found her', my_dictionary['Jenny'])
else:
    print('I need to get her number')

for key in my_dictionary:
    print(key, ':', my_dictionary[key],'\n')

print(my_dictionary)