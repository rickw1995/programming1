import time
try:
    file = open("hardlopers.txt", "a")
except:
    file = open("hardlopers.txt", "w")

stop = 0
while stop == False:
    per = input("Naam volgende die binnenkomt: ")
    if per != 'stop':
        file.write(time.strftime('%a %d %b %Y, %H:%M:%S', time.localtime()) + ', ' + per + '\n')
    else:
        stop = True
file.close()
