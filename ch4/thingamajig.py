# Thingamajig is a palindrome - basically a word that is the same from front to back i.e. racecar /. level
# Thingamig basiaclly prints the letters start to finish and then finish to start
characters = ['d', 'o', 'g']

output = ''
length = len(characters)
i = 0
while (i < length):
    output = output + characters[i]
    i = i + 1

print(output)

length = length * -1
i = -1

while (i >= length):
    output = output + characters[i]
    i = i - 1

print(output)