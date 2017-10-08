leeftijd = 19
paspoort = 0        # 0 is ja en 1 is nee

if leeftijd > 18 and paspoort == 0:
    print('Geef je leeftijd:', leeftijd)
    print('Nederlands paspoort: ja')
    print('U mag stemmen!')

else:
    print('Geef je leeftijd:', leeftijd)
    print('Nederlands paspoort: nee')
    print('Helaas, U mag niet stemmen')
