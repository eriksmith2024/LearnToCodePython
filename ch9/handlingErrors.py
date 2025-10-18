try:
    filename = 'notthere.txt'
    file = open(filename, 'r')
except:
    print('Sorry, an error occurred opening', filename)
else:
    print('Glad we got that file open')
    file.close()