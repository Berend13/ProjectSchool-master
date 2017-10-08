def amountlines(filename):
    infile = open('Kaartnummers.txt','r')
    lineList = infile.readlines()
    infile.close()
    print('Deze file telt',len(lineList),'regels')

def maxnumber(filename):
    infile = open('Kaartnummers.txt','r')
    content = infile.readlines()
    numbers = []
    for line in content:
        numbers.append(int(line.split(',')[0]))
    maxnumbers = max(numbers)
    linemax = numbers.index(max(numbers))+1
    print('Het grootste kaartnummer is:',maxnumbers,'en die staat op regel',linemax)


amountlines(input)
maxnumber(input)
