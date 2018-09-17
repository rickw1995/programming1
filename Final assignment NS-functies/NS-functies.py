def standaardprijs(afstandKM):
    if afstandKM > 50:
        return 15 + (afstandKM * 0.6)
    else:
        return afstandKM * 0.8


def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if weekendrit == True:
        if leeftijd < 12 or leeftijd >= 65:
            return (prijs *0.65)
        else:
            return(prijs * 0.6)
    else:
        if leeftijd < 12 or leeftijd >= 65:
            return (prijs *0.7)
        else:
            return prijs

weekend = input('Is het weekend? (ja/nee) ')

weekendrit = 'ja' in weekend

leeftijd = eval(input('Wat is uw leeftijd? '))
afstandKM = eval(input('Aantal kilometers: '))

print('De prijs voor uw rit bedraagt €' + str('%.2f' %(ritprijs(leeftijd, weekendrit, afstandKM))))
