def inlezen_beginstation(stationes):
    temp = set(stationes)
    sta = ""
    while sta not in temp:
        sta = input("Wat is uw beginstation: ")
    return sta

def inlezen_eindstation(stationes,begin_stationes):
    for t in range(len(stations)):
        if begin_stationes == stations[t]:
            begi = t
    temp = set(stationes)
    sta = ""
    while True:
        sta = input("Wat is uw eindstation: ")
        if sta in temp:
            for t in range(len(stations)):
                if sta == stations[t]:
                    eind = t
                    if eind > begi:
                        return sta
                        break
                    else: print("De trein komt niet in {}".format(stationes[eind]))
        else: print("station bestaat niet!")

def return_sation_index(stationes,station_des):
    for i in range(len(stationes)):
        if station_des == stations[i]:
            return i
            break

def omroepen_reis(stationes,begin_stationes,eind_stationes):
    begi = return_sation_index(stationes,begin_stationes)
    eindi = return_sation_index(stationes,eind_stationes)
    print("Het beginstation {} is het {}e station in het traject".format(begin_stationes,1+ begi))
    print("Het eindstation {} is het {}e station in het traject".format(begin_stationes, 1+ eindi))
    afstand = (1+ eindi)-(1+ begi)
    print("de afstand bedraagt {} station(s)".format(afstand))
    print("de prijs van het kaartje is {:.2f} euro".format(afstand*5))
    print("U stapt op de trein in {}".format(begin_stationes))
    if (begi+1) == eindi:
        print("U stapt uit de trein in {}".format(eind_stationes))
    else:
        for i in range(afstand-1):
            print(" -   {}".format(stations[1+begi+i]))
        print("U stapt uit de trein in {}".format(eind_stationes))




file = open('stations.txt', 'r')
stations = file.read().split(',')

beginstation = inlezen_beginstation(stations)
eindstation =inlezen_eindstation(stations,beginstation)
omroepen_reis(stations,beginstation,eindstation)