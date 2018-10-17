studentencijfers = [[95,92,86],[66,75,54],[89,72,100],[34,0,0]]

def gemiddelde_per_student(cijfers):
    temp = []
    for std in cijfers:
        temp.append(sum(std)/len(std))
    return temp

def gemiddelde_van_alle_studenten(alle_gem_cijvers):
    return sum(alle_gem_cijvers)/len(alle_gem_cijvers)



print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(gemiddelde_per_student(studentencijfers)))