studenten = {
    'jan' : 8,
    'peter' : 7,
    'david' : 9,
    'gerard' : 10,
    'fillip' : 9.5,
    'stefan' : 2,
    'kees' : 7,
    'dude' : 10
}

for student in studenten:
    if studenten[student] > 9:
        print('{} heeft een {} gehaald'.format(student,studenten[student]))