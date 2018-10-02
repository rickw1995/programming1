file = open('Kaartnummers.txt')
lst = []
a = file.readlines()

for i in a:
    temp = i.split(sep=',')
    lst.append(eval(temp[0]))

waarde = max(lst)

y=0

for i in a:
    y = y+1
    if str(waarde) in i:
        print('Deze file telt ' + str(len(a)) + ' regels')
        print('Het grootste kaartnummer is: ' + str(waarde) + ' en dat staat op regel ' + str(y))

