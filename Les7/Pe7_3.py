dictionary = {'Bob': 7, 'Jan': 3, 'Klaas': 10, 'Karel': 8, 'John': 4, 'Berend': 10, 'Alfred': 9, 'Johan': 6, 'Willie': 1, 'Man': 9,}
for key, value in dictionary.items():
    if 9 <= value:
        print(key)
