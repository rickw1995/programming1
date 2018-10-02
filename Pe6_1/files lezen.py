infile = open('kaartnummers.txt')
for i in infile.readlines():
    temp = i.split(sep=',')
    print(temp[1].strip('\n ') + " heeft kaartnummer: " + temp[0])
infile.close()

