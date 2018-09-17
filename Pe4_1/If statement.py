score = input('Geef je score: ')

if int(score) > 15:
    print('Gefeliciteerd!')
    print('Met een score van ' + str(score) + ' ben je geslaagd!');
else:
    print('U bent niet geslaagd.')

# als de print niet onder het if of else statement staat wordt het sowieso geprint.