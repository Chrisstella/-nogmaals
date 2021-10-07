# name of student: Chrisstella B
# number of student:99065775
# purpose of program: bij de kassa wisselgeld(terug geven) uitrekenen en vertellen wat+hoeveel
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: ')) * 100)  # euro(hoeveel moest betalen) opvragen en in cent zetten
paid = int(float(input('Paid amount: ')) * 100)  # euro(hoeveel er betaalt is) opvragen en in cent zetten
change = paid - toPay  # het verschil/hoeveel er terug gegeven moet worden

if change > 0:          # als er iets terug gegeven moet worden
    coinValue = 500  #

    while change > 0 and coinValue > 0:  #
        nrCoins = change // coinValue  #

        if nrCoins > 0:  #
          if coinValue == 500 or coinValue == 300 or coinValue == 200:
            print('return maximal ', nrCoins, ' coins of ', coinValue//100, ' Euro!')  #
            nrCoinsReturned = int(input('How many coins of ' + str(coinValue//100) + ' Euro did you return? '))  #
            change -= nrCoinsReturned * coinValue  #

          else:
            print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!')  #
            nrCoinsReturned = int(input('How many coins of ' + str(coinValue) + ' cents did you return? '))  #
            change -= nrCoinsReturned * coinValue  #

        # comment on code below:
        if coinValue == 500:
            coinValue = 300
        elif coinValue == 300:
            coinValue = 200
        elif coinValue == 200:
            coinValue = 50
        elif coinValue == 50:
            coinValue = 20
        elif coinValue == 20:
            coinValue = 10
        elif coinValue == 10:
            coinValue = 5
        elif coinValue == 5:
            coinValue = 2
        elif coinValue == 2:
            coinValue = 1
        else:
            coinValue = 0

if change > 0:  #
    print('Change not returned: ', str(change) + ' cents')
else:
    print('done')
    print(f"{paid - toPay} cents returned ")
