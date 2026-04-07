idade = int(input("Informe a idade"))

if idade<10:
    print("Infantil")
else:
    if idade<15:
        print("Juvenil")
    else:
        if idade <20:
            print("Junior")
        else:
            if idade<30:
                print("Adulto")
            else:
                print("Senior")