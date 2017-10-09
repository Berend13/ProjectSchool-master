dict = {}
list =[]
while True:
    inputnaam = input('volgende naam:')
    if inputnaam == '':
        break
    list.append(inputnaam)
    if inputnaam not in dict:
        dict[inputnaam] = 0
    dict[inputnaam] += 1

for key, value in dict.items() :
    if value == 1:
        print('er is',value,'student met de naam',key)
    else:
        print ('er zijn',value,'studenten met de naam',key)