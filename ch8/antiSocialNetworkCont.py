attributes = {
    'email': 'kim@oreilly.com',
    'gender': 'f',
    'age': 27,
    'fiends':['John', 'Josh']
}

users = {}

users['Kim'] = attributes

users['John'] = {'email': 'john@abc.com', 'gender': 'm', 'age': 24, 'friends':['Kim', 'Josh']}
users['Josh'] = {'email': 'josh@wickedlysmart.com', 'gender': 'm', 'age': 32, 'friends':['Kim']}

print(users)

def average_age (username):
    global users

    user = users[username]
    friends = user[friends]