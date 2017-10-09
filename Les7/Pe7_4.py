tickers = {}
list = []
def ticker(filename):
    infiler = open('tickersymbols', 'r')
    lines = infiler.readlines()
    for x in lines:
        if '\n' in x:
            list.append(x.replace('\n',''))
        else: list.append(x)
    split = []
    for x in list:
        split.append(x.split(':'))
    for x in split:
        tickers[x[0]]=(x[1])
    print('Company name:',tickers[filename])

input = input('Bedrijf: ')
ticker(input)
