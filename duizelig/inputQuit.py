#Herhaal een input() tot het resultaat daarvan gelijk is aan ‘quit’.
#Print het aantal iteraties per iteratie. (Het aantal keren dat de vraag is gesteld)

stop = input("""Wilt u stoppen? 
om te stoppen typ: 'quit'  """)
aantalXgestelt = 1

while stop != "quit":
    aantalXgestelt = aantalXgestelt + 1
    stop = input("""Wilt u stoppen? 
om te stoppen typ: 'quit'  """)
    print(f"{aantalXgestelt} keer gevraagt")