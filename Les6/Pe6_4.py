studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    for student in studentencijfers:
        print(round(sum(student)/ (len(student)),2))

gemiddelde_per_student(studentencijfers)

def gemiddelde_van_alle_studenten(studentencijfers):
    stuudjes = []
    for student in studentencijfers:
        stuudjes.append(round(sum(student)/ (len(student)),2))
    print(round(sum(stuudjes)/len(stuudjes),2))

gemiddelde_van_alle_studenten(studentencijfers)
