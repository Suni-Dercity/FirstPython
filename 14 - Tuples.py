mon_tuple = ('Sam', True, 27, ['mma', 'box thai', 'moto'])

print(mon_tuple[0])

# mon tuple[0] = 'Tom' # erreur car tuple non modifiable

mon_tuple[3][0] = 'judo'

print(mon_tuple)

mon_tuple[3].append('toto')
print(mon_tuple)

# mon_tuple[3] = ['toto', 'titi']

