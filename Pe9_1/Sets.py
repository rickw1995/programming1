bruin = {"Boxtel", "Best", "Beukenlaan", "Eindhoven", "Helmond 't Hout", "Helmond", "Helmond Brouwhuis", "Deurne"}
groen = {"Boxtel", "Best", "Beukenlaan", "Eindhoven", "Geldrop", "Heeze", "Weert"}

print("de treinen rijden allebei langs de volgende stations: {}".format(bruin.intersection(groen)))
print("de groene trein rijdt niet langs de volgende stations: {}".format(bruin.difference(groen)))
print("alle stations: {}".format(bruin.union(groen)))