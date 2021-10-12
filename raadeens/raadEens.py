import random
starten = 1
ronden = 1
keerGeraden = 1

print("""raad het getal!
om te stoppen typ: 0""")
while ronden <= 20 or starten >= 1:
    randomGetal = random.randint(1, 1000)
    ronden = ronden + 1
    while keerGeraden <= 10:
        geradenGetal = int(input("Raad een getal "))
        keerGeraden = keerGeraden + 1
        starten = geradenGetal
        if geradenGetal < randomGetal:
            print("moet grooter")
        else:
            print("moet kleiner")

        if randomGetal > geradenGetal:
            if randomGetal - geradenGetal <= 50:
                if randomGetal - geradenGetal <= 20:
                    print("heet20")
                else:
                    print("warm50")

        else:
            if randomGetal - geradenGetal + 50 >= 0:
                if randomGetal - geradenGetal + 20 >= 0:
                    print("heet20")
                else:
                    print("warm50")

