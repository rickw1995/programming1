leeftijd = input('Wat is uw leeftijd: ')


if int(leeftijd) >= 18:
    Paspoort = input('Bent u in het bezit van een Nederlands paspoort(antwoord met ja of nee): ')
    if 'ja' in Paspoort:
        print('Gefeliciteerd, u mag stemmen!')
    else:
        print('U mag niet stemmen.')
else: print('u mag nog niet stemmen.')

# dit is ook gelijk de if/else opdracht