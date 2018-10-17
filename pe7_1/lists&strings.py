def get4stringback(lijst):
    temp = []
    for woord in lijst:
        if len(woord) == 4:
            temp.append(woord)
    return temp

print('De nieuw-gemaakte lijst met alle vier-letter strings is: {}'.format(get4stringback(eval(input("Geef een lijst met minimaal 10 strings: ")))))
