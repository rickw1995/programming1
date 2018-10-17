def printmenu():
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
    print('2: Ik wil een nieuwe kluis')
    print('3: ik wil even iets uit mijn kluis halen')
    print('4: ik geef mijn kluis terug\n')
    select()

def select():
    selected_number = 0
    while selected_number > 4 or selected_number < 1:
        try:
            selected_number = int(input("invoer: "))
        except:
            print("Voer een getal in!\n")
            selected_number = 0
            printmenu()

        if selected_number < 1 or selected_number > 4:
            print("voer een geldige waarde in!\n")
            printmenu()

        if selected_number == 1:
            hoeveelkluizen()
        elif selected_number == 2:
            nieuwekluis()
        elif selected_number == 3:
            openKluis()
        elif selected_number == 4:
            verwijderKluis()

def hoeveelkluizen():
    try:
        file = open("kluizen.txt" , 'r')
        temp = file.readlines()
        count = 0
        for temp in temp:
            count += 1
        if count < 13:
            print("\ner zijn nog {} kluisjes vrij\n".format(12-count))
        else: print('alle kluisjes zitten vol')
        file.close()
        printmenu()

    except:
        print("\nalle kluizen zijn nog vrij\n")
        printmenu()

def nieuwekluis():
    kluizen = []
    for i in range(1,13):
        kluizen.append(i)

    try:
        file = open("kluizen.txt" , 'r')
        temp = file.readlines()

        for x in temp:
            a = x.split(sep=';')
            kluizen.remove(eval(a[0]))

        file.close()
    except:
        pass


    if len(kluizen) != 0:
        print("u krijgt kluis {}".format(kluizen[0]))
        try:
            file = open("kluizen.txt",'a')
        except:
            file = open('kluizen.txt', 'w')

        ww = ''
        while len(ww) < 4:
            print('Wachtwoord moet minimaal 4 tekens lang zijn!')
            ww = input('typ uw wachtwoord: ')
        file.write("{};{}\n".format(kluizen[0],ww))
        file.close()
        print('Succesvol!\n')
        printmenu()

    else:
        print("alle kluizen zijn bezet\n")
        printmenu()

def openKluis():
    try:
        kluisnmr = int(input('uw kluis nummer: '))
        if kluisnmr > 12:
            kluisnmr = int("haha noob")
        try:

            file = open("kluizen.txt", 'r')
            ww = input("Wachtwoord: ")
            temp = file.readlines()

            succes = 0
            for x in temp:
                a = x.split(sep=';')

                if kluisnmr == int(a[0]) and ww == a[1].strip('\n'):
                    print('Succes, kluis {} wordt nu open gemaakt\n'.format(int(a[0])))
                    succes = 1
            if succes == 0:
                print('De gegevens zijn incorect\n')
            file.close()
            printmenu()
        except:
            print("Je hebt helemaal geen kluis!\n")
            printmenu()
    except:
        print('ongeldig nummer!\n')
        printmenu()

def verwijderKluis():
    try:
        kluisnmr = int(input('Wat is uw kluis nummer: '))
        ww = input('wat is uw wachtwoord: ')
        try:
            file = open("kluizen.txt", "r")
            lines = file.readlines()
            file.close()

            file = open('kluizen.txt', 'w')
            succes = 0
            for x in lines:
                a = "{};{}\n".format(kluisnmr,ww)

                if x != a:
                    file.write(x)
                else: succes = 1
            if succes == 1:
                print("De kluis wordt vrijgegeven\n")
            else: print('De gegevens zijn incorect\n')

            file.close()

            printmenu()

        except:
            print('Jij hebt helemaal geen kluis\n')
            printmenu()
    except:
        print('voer een getal in\n')
        printmenu()
