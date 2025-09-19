eighties = ['', 'duran duran', 'B-52s', ' muse']
newwave = [ 'flock of seagulls', 'postal service']

remember = eighties.copy()

eighties[1] = 'culture club'

band = newwave[0]

eighties[3] = band

eighties[0] = eighties[2]

eighties[2] = remember

print(eighties)

print(eighties[2])