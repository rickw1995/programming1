def hoi(lijst):
    temp = (lijst.split(sep="-"))
    getallen = []
    for i in temp:
        getallen.append(eval(i))
    getallen.sort()
    print('Gesorteerde list van ints: {}'.format(getallen))
    print('Grootste getal: {} en Kleinste getal: {}'.format(max(getallen),min(getallen)))
    print('Aantal getallen: {} en Som van de getallen: {}'.format(len(getallen),sum(getallen)))
    print('Gemiddelde: {:.2f}'.format(sum(getallen)/len(getallen)))

hoi(input('invoer: '))