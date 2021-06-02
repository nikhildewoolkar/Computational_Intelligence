
Honesty = {"Nikhil": 0.2, "Nancy": 0.3, "Ayush": 0.6, "Sahil": 0.6, "Akash": 0.5}

Sincerity = {"Nikhil": 0.9, "Nancy": 0.9, "Ayush": 0.4, "Sahil": 0.5, "Akash": 0.4}

print('The Honesty of Students is represented as :', Honesty)

print('The Sincerity of Students is represented as :', Sincerity)

Union = dict()

for H, S in zip(Honesty, Sincerity):
    if Honesty[H] > Sincerity[S]:
        Union[H] = Honesty[H]
    else:
        Union[S] = Sincerity[S]

print('\nHonesty and Sincerity Union is :', Union)

Intersection = dict()
for H, S in zip(Honesty, Sincerity):
    if Honesty[H] < Sincerity[S]:
        Intersection[H] = Honesty[H]
    else:
        Intersection[S] = Sincerity[S]
print('\nHonesty and Sincerity Intersection is :', Intersection)

HonestyComplement = dict()
for H in Honesty:
    HonestyComplement[H] = 1-Honesty[H]
print('\nHonesty Complement is :', HonestyComplement)

SincerityComplement = dict()
for S in Sincerity:
    SincerityComplement[S] = 1 - Sincerity[S]
# print('\nSincerety Fuzzy Set Complement is :', SincerityComplement)

Difference = dict()
for H, SC in zip(Honesty, SincerityComplement):
    if Honesty[H] < SincerityComplement[S]:
        Difference[H] = Honesty[H]
    else:
        Difference[SC] = SincerityComplement[SC]

print('\nHonesty and Sincerity Difference is :', Difference)
