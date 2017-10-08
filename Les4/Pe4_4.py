def new_password(oldpassword, newpassword):
    return (new_password)

oldpassword = (input("Geef je oude wachtwoord op:"))
newpassword = (input("Geef je nieuwe wachtwoord op:"))

if oldpassword == newpassword or len(newpassword) < 6:
    print("Het wachtwoord mag niet hetzelfde zijn en / of minder dan 6 tekens lang zijn")

else:
    print("Uw wachtwoord is succesvol veranderd!")

