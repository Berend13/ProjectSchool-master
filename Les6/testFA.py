

d = []
with open("kluizen.txt") as f:
    for line in f:
       (nummer, wachtwoord) = line.split(';')
       d.append (nummer)
print(d)

