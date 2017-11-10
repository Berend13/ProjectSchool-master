import random

def monopolyworpen():
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    worp1 = []
    worp1.append(a)
    worp1.append(b)
    if a != b:
        print(a,'+',b,'=',sum(worp1))
    if a == b:
        print(a,'+',b,'=',sum(worp1),'(dubbel)')
        c = random.randrange(1, 7)
        d = random.randrange(1, 7)
        worp02 = []
        worp02.append(c)
        worp02.append(d)
        if c != d:
            print(c,'+',d,'=',sum(worp02))
        if c == d:
            print(c,'+',d,'=',sum(worp02),'(dubbel)')
            e = random.randrange(1, 7)
            f = random.randrange(1, 7)
            worp03 = []
            worp03.append(e)
            worp03.append(f)
            if e != f:
                print(e,'+',f,'=',sum(worp03))
            if e == f:
                print(e,'+',f,'=','(direct naar gevangenis')

monopolyworpen()