ICOR = 6.0

PROG = 8.0

CSN = 8.0

#beloning per punt

OS = 30.0

GEM = (CSN + PROG + ICOR) / 3

GEMM = str(round(GEM, 2))

Totaal = PROG + CSN + ICOR

beloning = OS * Totaal


print('mijn cijfers, gemiddeld een ' + GEMM + ' leveren mij een beloning van €' + str(beloning) + ' op.')


