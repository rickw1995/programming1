def namen():
    studenten = {}
    while True:
        naam = input("Volgende naam: ")
        if naam == "":
            break

        if naam in studenten:
            studenten[naam] += 1
        else:
            studenten[naam] = 1
    for student in studenten:
        if studenten[student] == 1:
            print("Er is {} student met de naam {}".format(studenten[student],student))
        else:
            print("Er zijn {} studenten met de naam {}".format(studenten[student],student))

namen()