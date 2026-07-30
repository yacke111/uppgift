try:
    Celsius = float(input("ange temperatur i celsius:"))
    fehrenheit = Celsius * (9/5) +32
    print(f"i fehrenheit :{fehrenheit}")
    if Celsius < 0:
         print("mycket kallt!")
    elif Celsius < 17:
        print("svalt!")
    elif Celsius < 21:
        print ("lagom!")
    else:
        print("varmt!")

except ValueError:
    print("felaktig inmätning")