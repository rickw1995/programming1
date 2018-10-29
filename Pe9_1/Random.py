import random
def monopolyworp():
    def worp_werpen():
        return [random.randrange(1,7),random.randrange(1,7)]
    worp = worp_werpen()
    if worp[0] == worp[1]:
        print("{} + {} = {} (Dubbel!)".format(worp[0],worp[1],worp[0]+worp[1]))
        worp = worp_werpen()
        if worp[0] == worp[1]:
            print("{} + {} = {} (Dubbel!)".format(worp[0],worp[1],worp[0]+worp[1]))
            worp = worp_werpen()
            if worp[0] == worp[1]:
                print("{} + {} = (Direct naar de gevangenis!)".format(worp[0], worp[1]))
            else: print("{} + {} = {}".format(worp[0], worp[1], worp[0] + worp[1]))
        else: print("{} + {} = {}".format(worp[0],worp[1],worp[0]+worp[1]))
    else: print("{} + {} = {}".format(worp[0], worp[1], worp[0] + worp[1]))


monopolyworp()
