marbles = [10, 13, 39, 14, 41, 9, 3]

print('The total is', sum(marbles))

def compute_sum(list):
    sum = 0

    for number in list:
        sum = sum + number
    
    return sum

print('The total is', compute_sum(marbles))

compute_sum([])

print(10 + compute_sum([13, 39, 14, 41, 9, 3]))