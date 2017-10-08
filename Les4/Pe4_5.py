def kwadraten_som(grondgetallen):
    s = 0
    for x in grondgetallen:
        if x > 0:
            s = s + x**2
    return s

print (kwadraten_som([4,5,3,-81]))
