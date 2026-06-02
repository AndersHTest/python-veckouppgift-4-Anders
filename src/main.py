from Forsta_kod import *


## Uppgift 1a
## Jag tror att 'test' kommer at skrivas ut.

print("1a:\n")
print("Utkommenterad pga uppgift 1f")

## foo("hej")

print("____\n")

## Uppgift 1b
## 3 5. Vi anropar aldrig fun1. Vi anropar print och skriver ut det som står i argumentet.

print("1b:\n")
print(3, 5)

print("____\n")

## Uppgift 1c
## Anropar fun1 via print. resultatet av 3 * 5 skrivs ut. 15.

print("1c:\n")

print(fun1(3, 5))

print("____\n")

## Uppgift 1d
## Jag tror att a = (5 * 10) + (5 * 15), därmed visas "125" när koden körs.

print("1d:\n")

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)

print("____\n")

## Uppgift 1e
## Funktionen fun3 anropas aldrig. a + 2 skrivs ut som 7.

print("1e:\n")

a = 5
a += 2

print(a)

print("____\n")

## Uppgift 1f
## Funktionen foo finns redan och kommer skriva över den första funktionen.
## Det kommer generera ett felmeddelande vid första anropet i uppgift 1a. Kommenterar ut uppgift 1a ur körningen.
## Jag förstår inte hur 'i' ska få ett värde så jag gissar på error. Fel.. 18..
## Det verkar bli 2 * y * y. Alltså 2 * 3 * 3 = 18. Men jag hänger inte riktigt med.
## Tog bort semikolon.

print("1f:\n")

a = goo(foo, 3)
print(a)

print("____\n")

## Uppgift 1g
## Funktionen "isinstance" kan kontrollera en variabels datatyp.
## Vad gör funktionen is_number? Går det att förbättra koden?

## Jag tror att funktionen alltid kommer att returnera 'False'.
## Man bör ändra koden så att 'return False' läggs efter else:
## --Fel, det gjorde ingen skillnad.
## --Då vet jag inte hur koden skall förbättras, men jag tycker det blir tydligare med en else:.

print("1g:\n")

print(is_number(5.5))
print(is_number(42))

print("____\n")

## Uppgift 1h
## Funktionen skapar en lista och fyller listan med strängar som är mellan 5 - 7 tecken.
## Funktionen returnerar en lista med värden som är mellan 5-7 tecken.

print("1h:\n")

average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])

print("____\n")


## Uppgift 1i
## 1; Funktionens syfte verkar vara att returnera det minsta värdet av de värden som matas in.
## 2; -11, '', 100
## 3; Ändrade "if item < counter:" till "if item == min(numbers):". Lade till lite felhantering.

print("1i:\n")

find_min([10, 3, -4, -11])
find_min([])
find_min([100])

print("____\n")