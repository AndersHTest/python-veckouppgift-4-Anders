import random

## Version 1
## Om man lägger ihop talen 1 + 2 + 3 + 4 + … så kommer talens summa att bli större och större.
## Förr eller senare kommer man förbi 21.
## Skriv en funktion som skriver ut det första talet i talserien som är större än 21.

def spelet_21_v1():
    y = 0
    for i in range(1, 30):
        y += i
        if y > 21:
            break
    return y


## Version 2
## Istället för att använda talserien, slumpa tal mellan 1 och 13.

def spelet_21_v2():
    card = random.randint(1, 13)
    return card

## Version 3
## Bygg ett spel som frågar användaren om man vill ta ett nytt kort eller stanna.
## Gör så att datorn kan simulera en motståndare. Målet är att vinna över datorn.


def hitta_narmsta_vardet(ditt_varde, datorns_varde, target):
    diff1 = abs(ditt_varde - target)
    diff2 = abs(datorns_varde - target)

    if diff1 < diff2:
        narmsta = ditt_varde
    elif diff2 < diff1:
        narmsta = datorns_varde
    else:
        narmsta = min(ditt_varde, datorns_varde)
    return narmsta


def spelet_21_v3():

    ta_kort = input(f"Tryck 1 för att ta ett kort eller 0 för att stanna: ")
    din_hand = []
    datorns_hand = []
    x = True

    while x:

        if ta_kort == "1":
            kort = spelet_21_v2()
            kort1 = spelet_21_v2()
            din_hand.append(kort)
            datorns_hand.append(kort1)
            ta_kort = input(f"Du har nu {sum(din_hand)} på handen.\nTryck 1 för att fortsätta eller 0 för att avsluta: ")
      #      if ta_kort == "1":
       #         din_hand.append(kort)
        #        datorns_hand.append(kort1)

        elif ta_kort == "0":
            limit = 21
            narmsta_vardet = hitta_narmsta_vardet(sum(din_hand), sum(datorns_hand), limit)
            diff = limit - abs(narmsta_vardet)

            print(f"Du stannade på {sum(din_hand)} och datorn fick {sum(datorns_hand)}.")
            if narmsta_vardet == 0:
                print(f"Det blev lika! Båda var {limit - abs(sum(din_hand))} ifrån 21.")
            elif narmsta_vardet == sum(din_hand) and narmsta_vardet != sum(datorns_hand):
                print(f"Du vann! Du var {abs(diff)} ifrån 21.")
            else:
                print(f"Datorn vann! Datorn var {abs(diff)} ifrån 21.")
            x = False