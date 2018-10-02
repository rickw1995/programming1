def gemmidelde(wil_zin):
    woorden = wil_zin.split(sep=' ')
    temp = []
    for woord in woorden:
        temp.append(len(woord))
    return (sum(temp)/len(temp))

print(gemmidelde(input("zin: ")))