file = open('Kaartnummers.txt', 'r')
for lines in file:
    number, word = lines.split(',')
    print(lines[8:600].replace('\n',''),"heeft kaart nummer:", lines[0:6])
file.close()

