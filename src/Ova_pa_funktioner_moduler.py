## 1 Skriv en funktion som tar en sträng som parameter.
## När den anropas ska den skriva ut strängen och "är en fena på programmering".
## Exempel: my_function("David") → "David är en riktig hacker"

def my_function(x):
    print(f"{x} är en fena på programmering")


## 2a Skriv en funktion med namnet "eko".
## När den anropas med en sträng ska den upprepa strängen, och skriva ut resultatet. Exempel:
## eko("hej") → skriver ut "hejhej"

def eko(x):
    print(x * 2)

## 2b Lägg till en parameter "count", som avgör hur många ekon som ska skapas. Exempel:
## eko("hej", 3) → skriver ut "hejhejhej"

def eko2(x, y):
    print(x * y)


## Uppgift 2.3
## Följande kod ska sluta loopa efter 5 varv.
## Flytta den in i en funktion och justera den enligt kommentaren.
"""
end = 5
y = 1
for x in range(1, 100):
    y *= 2
    # avsluta loopen med en if-sats här
print(y)

"""


def loop_x_times(end):
    y = 1
    counter = 0
    for i in range(1, 100):
        y *= 2
        counter += 1
        if counter == end:
            break
    print(y)
    return y

## Uppgift 2.4
## Skriv en funktion med namnet last.
## Den ska ta en lista som parameter och returnera det sista elementet i listan.

def last(lista):
    last_element = lista[-1]

    print(last_element)
    return last_element

## Uppgift 2.5
## Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter.
## När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.

def cut_edges(trim_list):
    temp_list = trim_list.copy()
    temp_list.pop(0)
    temp_list.pop(-1)
    print(temp_list)
    return temp_list

## Uppgift 2.6
## Lös felen i koden.
## def increase(x):
    return x
    x += 1

    print(increase(1))

## Lösning:

def increase(x):
    y = x + 1
    return y

## Uppgift 2.7
## Bygg en funktion med namnet average. Den ska ta parametrar: x och y. Båda ska vara tal.
## Funktionen ska returnera medelvärdet.
## Till exempel så räknar man ut medelvärdet av 4 och 8 genom med formeln: (4 + 8) / 2, vilket blir 6.

def average(x, y):
    validate_input = isinstance(x, (int, float)) and isinstance(y, (int, float))
    if validate_input:
        average_1 = (x + y) / 2
        return round(average_1)
    else:
        return "Felaktig input. Försök igen."


## Uppgift 2.8
## Gör en funktion som kan skriva ut innehållet i en lista lite snyggare.
## Först ska funktionen tala om ifall listan är tom, eller hur många element den har.
## Sedan ska funktionen skriva ut elementen i en punktlista. Exempel:
## pretty_print(["a", "b", 3.14])
"""  Listan har 3 element:
     1. a
     2. b
     3. 3.14
"""

def pretty_print(listan):

    if not listan:
        print(f"Listan har {len(listan)} element. Försök igen.")

    elif listan:
        antal = len(listan)
        print(f"Listan har {antal} element:\n")

        for element in listan:
            numrera = listan.index(element) + 1
            print(f"{numrera}. {element}")
