import random
min = 1
max = 6

def monopolyworp():
    worp1 = []
    worp2 = []
    worp3 = []
    dobbelsteen1 = random.randint(min, max)
    dobbelsteen2 = random.randint(min, max)
    worp1.append(dobbelsteen1)
    worp1.append(dobbelsteen2)
    print(dobbelsteen1, '+', dobbelsteen2, '=', sum(worp1))
    if dobbelsteen1 == dobbelsteen2:
        dobbelsteen3 = random.randint(min, max)
        dobbelsteen4 = random.randint(min, max)
        worp2.append(dobbelsteen3)
        worp2.append(dobbelsteen4)
        print(dobbelsteen3,'+', dobbelsteen4, '=', sum(worp2))
        if dobbelsteen3 == dobbelsteen4:
            dobbelsteen5 = random.randint(min, max)
            dobbelsteen6 = random.randint(min, max)
            worp3.append(dobbelsteen5)
            worp3.append(dobbelsteen6)
            print(dobbelsteen4, '+', dobbelsteen5, '=', sum(worp3))
            print('Ga naar de gevangenis!')
monopolyworp()