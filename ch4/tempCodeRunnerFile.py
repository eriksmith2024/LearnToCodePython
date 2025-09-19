smoothies = [ 'cocunut', 'strawberry', 'banana', 'tropical', 'acai berry']
has_cocunut = [True, False, False, True, False]

print('')
i = 0
while i < len(has_cocunut):
    if has_cocunut[i]:
        print(smoothies[i], 'contains cocunut')
    i = i + 1

print('')