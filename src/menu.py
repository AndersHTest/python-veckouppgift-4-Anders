from Forsta_kod import *
from Ova_pa_funktioner_moduler import *
from Spelet_21 import *
from Pokerhand import *
from Turtle import *



def menu():
    active = True
    while active:

        print(f"\n1 - Läsa och förstå kod")
        print(f"2 - Öva på funktioner och moduler")
        print(f"3 - Spelet 21")
        print(f"4 - Pokerhand")
        print(f"5 - Turtle graphics")
        print(f"\n0 - Avsluta\n")

        control = input(f"Välj uppgift i menyn:\n")

        if control == "0":
            active = False

        if control == "1":
            print("\n1a:\n")
            print("Utkommenterad pga uppgift 1f")

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


        if control == "2":
            ## Uppgift 2.1
            print("\n2.1:\n")

            my_function("David")

            print("____\n")

            ## Uppgift 2.2a
            print("2.2a:\n")

            eko("hej")

            print("____\n")

            ## Uppgift 2.2b
            print("2.2b:\n")

            eko2("hej", 3)

            print("____\n")

            ## Uppgift 2.3
            print("2.3:\n")

            loop_x_times(5)

            print("____\n")

            ## Uppgift 2.4
            print("2.4:\n")

            last([1, 2, 3])

            print("____\n")

            ## Uppgift 2.5
            print("2.5:\n")

            cut_edges([1, 2, 3, 4])

            print("____\n")

            ## Uppgift 2.6
            print("2.6:\n")

            print(increase(1))

            print("____\n")

            ## Uppgift 2.7
            print("2.7:\n")

            print(average(4, 8))

            print("____\n")

            ## Uppgift 2.8
            print("2.8:\n")

            pretty_print(["a", "b", 3.14])

            print("____\n")


        if control == "3":

            ## Uppgift 3 version 1
            print("\n3, version 1:\n")

            print(spelet_21_v1())

            print("____\n")

            ## Uppgift 3 version 2
            print("3, version 2:\n")

            print(spelet_21_v2())

            print("____\n")

            ## Uppgift 3 version 3
            print("3, version 3:\n")

            spelet_21_v3()

            print("____\n")


        if control == "4":

            ## Uppgift 4, version 1
            print("\n4, version 1:\n")

            print(your_hand())

            print("____\n")


        if control == "5":

            ## Uppgift 5, version 1

            print("\n5, version 1:\n")

            turtle_kvadrat(100)

            print("____\n")

            ## Uppgift 5, version 2

            print("5, version 2:\n")

            t.clearscreen()
            turtle_poc(105, 100, "red", 2)

            print("____\n")

            ## Uppgift 5, version 3

            print("5, version 3:\n")

            t.clearscreen()
            turtle_circle(36, 30, -10, "blue")

            print("____\n")

            ## Uppgift 5, version 4

            print("5, version 4:\n")

            t.clearscreen()
            t.hideturtle()
            turtle_text("green")

            t.exitonclick()

            print("____\n")







