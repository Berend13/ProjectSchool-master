print('1: Ik wil weten hoeveel kluizen vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil even iets uit mijn kluis halen')
print('4: Ik geef mijn kluis terug')

ans = eval(input('Geef uw keuze: '))

infilea = open('kluizen.txt','a')
infiler = open('kluizen.txt','r')


if ans == 1:
    num_lines = sum(1 for line in open('kluizen.txt'))
    print("er zijn nog",12 - num_lines,"kluisjes vrij.")

if ans == 2:
    kluisnummers = [1,2,3,4,5,6,7,8,9,10,11,12]
    kluizen = infiler.readlines()
    open_kluizen = []
    d = []
    with open('kluizen.txt') as kluizen:
        for line in kluizen:
            (nummer, wachtwoord) = line.split(';')
            d.append(nummer)
    for line in d:
        open_kluizen.append(int(line.replace('\n','')))
    lege_kluizen = [x for x in kluisnummers if x not in open_kluizen]
    print('Dit zijn de lege kluizen: ',lege_kluizen)
    kluiskeuze = eval(input('Welke kluis wil je: '))
    if kluiskeuze not in lege_kluizen:
        print('Dit is niet mogelijk')
    while kluiskeuze not in lege_kluizen:
        kluiskeuze = eval(input('Welke kluis wil je: '))
    infilea.write(str(kluiskeuze))
    infilea.write(';')
    infilea.write(input('Geef een wachtwoord: '))
    infilea.write('\n')

if ans == 3:
    kluisnr = input('Kluisnummer: ')
    if kluisnr not in open('kluizen.txt').read():
        print("sorry.")
    kluisww = input('Wachtwoord: ')
    if kluisww in open('kluizen.txt').read():
        print("uw kluis is open!")

if ans == 4:
    with open('kluizen.txt', 'r+') as f:
        t = f.read()
        to_delete = input('Geef uw kluisnummer en wachtwoord: ').strip()   # input PSP0101
        f.seek(0)
        for line in t.split('\n'):
            if line != to_delete:
                f.write(line + '\n')
        f.truncate()
    print("Uw kluis is verwijderd!")

infilea.close()

