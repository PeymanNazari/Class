presence = 180
temp = 200

print(bool(presence or temp))

presence = 180
temp = 200

print(bool(presence and temp))

presence = 180<160
temp = 220>300

print(bool(presence or temp))

presence = 180>200
temp = 210

print(bool(presence and temp))