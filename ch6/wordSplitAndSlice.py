lyrics = 'I heard you on the wireless back in fifty two'
words = lyrics.split()
print('\n',words)
count = len(words)
print('\n',count)

print('')

# for char in lyrics:
#     print(char)

print('')

my_substring = lyrics[2:7]
print(my_substring,'\n')

my_substring2 = lyrics[:6]
print(my_substring2, '\n')

my_substring3 = lyrics[28:]
print(my_substring3, '\n')

my_substring4 = lyrics[28:-1]
print(my_substring4, '\n')

my_substring5 = lyrics[-17:]
print(my_substring5, '\n')