getallen=[]
while True:
    num = eval(input('geef een getal: '))
    if num == 0: break
    getallen.append(num)
print('er zijn {} getallen ingevoerd, de som is: {}'.format(len(getallen),sum(getallen)))