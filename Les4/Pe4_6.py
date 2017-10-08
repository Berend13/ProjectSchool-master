lijst = ['a', 'b', 'c']

def wijzig(letterlijst):
    del lijst [0:len(lijst)]
    lijst.extend(['d', 'e', 'f'])

print(lijst)
wijzig(lijst)
print(lijst)

