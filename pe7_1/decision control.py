def seizoen(maand):
    if maand >= 3 and maand <=5:
        return "Lente"
    elif maand > 5 and maand < 9:
        return "Zomer"
    elif maand >8 and maand < 12:
        return "Herfst"
    else:
        return "Winter"

print('het seizoen is: {}'.format(seizoen(eval(input('Welke maand is het? ')))))