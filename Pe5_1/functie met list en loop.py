def kwadraten_som(grondgetallen):
    list = []
    for nummer in grondgetallen:
        if nummer > 0:
            list.append(nummer **2)
    return  sum(list)

lijst = [3, 5, 10, -81]

print(kwadraten_som(lijst))
