#Vraag een dag van de week op (ma,di,wo,do,vr,za,zo) Print alle dagen tot en met de opgegeven dag.

dag = int(input("kies welke dag is het MA=1/DI=2/WO=3/DO=4/VR=5/ZA=6/ZO=7"))

ma = 1
di = 2
wo = 3
do = 4
vr = 5
za = 6
zo = 7
uitkomst = 0

while uitkomst != dag:
    uitkomst = uitkomst + 1

    if uitkomst == ma:
        print("Maandag")

    elif uitkomst == di:
        print("Dinsdag")

    elif uitkomst == wo:
     print("Woendag")

    elif uitkomst == do:
        print("Donderdag")

    elif uitkomst == vr:
        print("Vrijdag")

    elif uitkomst == za:
        print("Zaterdag")

    else:
        print("Zondag")






