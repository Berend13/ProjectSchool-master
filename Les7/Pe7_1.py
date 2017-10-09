count = 0
Total = 0
while True:
    Antwoord = int(input('Geef een nummer:'))
    count += 1
    Total += Antwoord
    if Antwoord == 0:
        print('er zijn',count,'getallen in gevoerd, de som is:', Total)
        break