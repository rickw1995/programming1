def convert(graden):
    return graden * 1.8 + 32



def table():
    print('  {0:8}{1:8}'.format('F', 'C'))
    for i in range(-30, 40, 10):
        print('{0:5}{1:8.1f}'.format(convert(i), i))


table()
