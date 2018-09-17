s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = 'aeoiu'
for a in s:
    if a in klinkers:
        print(a, end=', ')

