def gemiddelde(zin):
    zinsplit = zin.split()
    lenlist = []
    for woord in zinsplit:
        lenlist.append(len(woord))


    return round(sum(lenlist)/len(lenlist),2)

zin = input('Geef een willekeurige zin:\n')
print('de gemiddelde lengte van de woorden in de zin is',gemiddelde(zin),'karakters')
