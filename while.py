try:
    poäng = int(input("ange dina poäng (0-100):"))

    if poäng >= 90:
        print("utmärkt!")
    elif poäng >= 70:
        print("bra jobbat!")
    elif poäng >= 50:
        print("godkänt!")
    else:
        print("icke godkänt")
except ValueError:
    print("felaktig inmätning")


#test

    

    