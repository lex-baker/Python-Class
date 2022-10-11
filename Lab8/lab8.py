Mariners_runs = (10, 8, 8, 2, 3, 3, 5, 0, 6, 1)
print(Mariners_runs)

Opponents_runs = (3, 5, 2, 3, 1, 6, 3, 2, 4, 3)
print(Opponents_runs)

"""
print(Mariners_runs[6])
print(Opponents_runs[5])
print(Mariners_runs[1])
print(Mariners_runs[0])
print(Mariners_runs[10])
"""

"""
Mariners_record = 0
for i in range(10):
    if Mariners_runs[i] > Opponents_runs[i]:
        Mariners_record += 1
print(Mariners_record)
"""
"""
crazy_tuple = (42, "hello", 3.14159, True)
print(crazy_tuple)
print(crazy_tuple[1])
"""
team_name = 'Mariners'
print(team_name[0])
print(team_name[1])
print(len(team_name))
#print(team_name[8])

#team_name[5] = 'o'
#del team_name[5]

animals = ('cat', 'dog', 'bird', 'rabbit', 'lizard')
animals[1]
animals[3]
animals[-1]
animals[-3]
animals[-len(animals)]
#animals[len(animals)]
#animals[3] = 'ferret'

animals[1:3]
animals[:3]
animals[3:]
animals[:]
animals[-2:]

print(animals[2:4])
print(animals[-3:-1])

new_zoo = animals[:3] + ('ferret',) + animals[3:]
print(new_zoo)

even_newer_zoo = new_zoo[:3] + ('meercat',) + new_zoo[4:]
print(even_newer_zoo)

print(animals[2][0])
print(animals[2][1])
print(animals[2][2])
print(animals[2][2])
print(animals[2][:2])
print(animals[-1][-4:])

print(animals[3][2:4])

scores = (Mariners_runs, ) + (Opponents_runs, )
print(scores)