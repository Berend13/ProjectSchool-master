def standaardtarief(afstandKM):
    if afstandKM > 50:
        output = 15 + afstandKM*.6
    else:
        output = afstandKM*.8
    if afstandKM < 0:
        output = 0
    return output


def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == "ja" :
        if leeftijd < 12 or leeftijd >= 65:
            output = (standaardtarief(afstandKM)) * 0.65
        else:
            output = (standaardtarief(afstandKM)) * 0.6
    else:
        if leeftijd < 12 or leeftijd >= 65:
            output = (standaardtarief(afstandKM)) * 0.7
        else:
            output = (standaardtarief(afstandKM))
    return output


leeftijd = eval(input('Hoe oud bent u: '))
weekendrit = input('Is het weekend? (ja, nee): ')
afstandKM = eval(input('Hoe ver rijst u(in kilometer): '))
print('het kost U',round(ritprijs(leeftijd, weekendrit, afstandKM),2), 'euro, voor een rit van', afstandKM,'kilometer')
