def convert(celsius):
    fahrenheit = celsius*1.8+32
    return fahrenheit

print(" C         F")


for temp_c in range(-30, 41, 10):
    temp_f = convert(temp_c)
    print(temp_c,'  \t',temp_f)


