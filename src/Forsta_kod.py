## Skriv ner vad du tror kommer skrivas ut.
## Skriv sedan in koden i din IDE, exakt som den står, och kör den.
## Fick du samma resultat som du trodde? Om inte, varför?

## Uppgift 1a
## Jag tror att 'test' kommer at skrivas ut.


## def foo(t):
##    print("test")

## Uppgift 1b
## 3 5. Vi anropar inte fun1. Vi anropar print och skriver ut det som står i argumentet.

def fun1(x, y):
    return x * y

## Uppgift 1c
## Anropar fun1 via print. resultatet av 3 * 5 skrivs ut. 15.


def fun1(x, y):
    return x * y


## Uppgift 1d
## Jag tror att a = (5 * 10) + (5 * 15), därmed visas "125" när koden körs.


def fun2(i):
    return 5 * i


## Uppgift 1e
## Funktionen fun3 anropas inte. a + 2 skrivs ut som 7.


def fun3(a):
    a += 1


## Uppgift 1f
## Funktionen foo finns redan och kommer skriva över den första funktionen.
## Det kommer generera ett felmeddelande vid första anropet i uppgift 1a. Kommenterar ut uppgift 1a ur körningen.
## Jag förstår inte hur 'i' ska få ett värde så jag gissar på error. Fel.. 18..
## Det verkar bli 2 * y * y. Alltså 2 * 3 * 3 = 18. Men jag hänger inte riktigt med.
## Tog bort semikolon i main.


def foo(i):
    return 2*i*i


def goo(x, y):
    return x(y)


## Uppgift 1g
## Funktionen "isinstance" kan kontrollera en variabels datatyp.
## Vad gör funktionen is_number? Går det att förbättra koden?

## Jag tror att funktionen alltid kommer att returnera 'False'.
## Man bör ändra koden så att 'return False' läggs efter else:
## --Fel, det gjorde ingen skillnad.
## --Då vet jag inte hur koden skall förbättras, men jag tycker att det skulle bli tydligare med en else:.

def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

## Uppgift 1h
## Funktionen skapar en lista och fyller listan med strängar som är mellan 5 - 7 tecken.
## Funktionen returnerar en lista med värden som är mellan 5-7 tecken.

def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

## Uppgift 1i
## 1; Funktionens syfte verkar vara att returnera det minsta värdet av de värden som matas in.
## 2; -11, '', 100
## 3; Ändrade "if item < counter:" till "if item == min(numbers):". Lade till lite felhantering.


def find_min(numbers):

    filter_values = all(isinstance(item, (int, float)) for item in numbers)

    if not numbers:
        print("The list was empty.\n")
    elif not filter_values:
        print("The list contains invalid items. Please enter numbers only.\n")
    else:
        counter = 0
        for item in numbers:
            if item == min(numbers):
                counter = item
        print(f"The smallest item is: {counter}\n")