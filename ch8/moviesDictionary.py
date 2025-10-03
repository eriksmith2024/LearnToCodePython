movies = []
movie = {}

movie['name'] = 'Forbidden Planet'
movie['year'] = 1957
movie['rating'] = '*****'
movie['year'] = 1956

movies.append(movie)

movie2 = {'name': 'I was a Teenage Werewolf', 
          'year,': 1957, 'rating': '*****'}
movie2['rating'] = '***'

movies.append({'name': 'Viking Woman and the Sea Serpent', 
               'year': 1957,
               'rating': '**'})

movies.append({'name': 'Vertigo',
               'year': 1958,
               'rating': '*****'})

print('Head first movie recommendations')
print('--------------------------------')

for movie in movies:
    if len(movie['rating']) >= 4:
        print(movie['name'], '(' + movie['rating'] + ')', movie['year'])