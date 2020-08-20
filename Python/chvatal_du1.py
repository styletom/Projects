# Prvni domaci uloha z IB111, 2016
#
# Mate za ukol naprogramovat 5 funkci, za kazdou muzete ziskat az 3 body
# Piste co nejprehlednejsi kod, zejmena vhodne pojmenovavejte promenne
#           (za necitelny kod hrozi bodova srazka)
#
# Sve reseni pojmenujte jako "prijmeni_du1.py" a ulozte do prislusne odevzdavarny
#           (bez uvozovek a bez diakritiky)
# --------------------------------------------------------------
# zde muzete definovat pripadne importy
from turtle import Turtle
from math import pi

#---------------------------------------------------------------
# 1) Napiste funkci, ktera pro zadane N vypise vsechna cela cisla od jedne do N vcetne
# tak, ze licha jsou vypsana normalne a misto sudych se vypise cislo opacne
#
# napr: pro N = 8 funkce vypise: 1, -2, 3, -4, 5, -6, 7, -8
#       pozn. muzete predpokladat, ze jako N bude zadavano kladne cele cislo
#---------------------------------------------------------------

def numbers_interlaced(n):
    l = 1
    s = -1
    for i in range(n):
        if s%2 == 0:
        	print(s, end=" ")
        else:
        	print(l, end=" ")
        l += 1
        s -= 1
numbers_interlaced(8)

#---------------------------------------------------------------
# 2) Napiste funkci, ktera pro zadane parametry N, M vypise matici (tabulku) cisel
# o velikosti N krat M, (N radku, M sloupcu) kde kazde cislo je dano jako soucet cisla radku a sloupce.
# Radky i sloupce cislujte od 1, zarovnani nereste (sloupce oddelujte mezerou)
#
# napr: pro N = 4, M = 6 bude vystup:
#
#   2 3 4 5 6 7
#   3 4 5 6 7 8
#   4 5 6 7 8 9
#   5 6 7 8 9 10
print() #oddeleni funkce na dalsi radek
#---------------------------------------------------------------

def sum_table(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(i + j, end=" ")
        print()

sum_table(4, 6)
#---------------------------------------------------------------
# 3) Napiste funkci, ktera v textove grafice vykresli pro zadane N prazdnou
# pyramidu o N patrech zvorenou krizky "#" a vyplnenou teckami ".".
#
# napr: pro N = 4 funkce vykresli

            #
          # . # 
        # . . . #
      # # # # # # #

# pozn. zde je spravne odsazovani mezi patry stezejni (na velikosti odsazeni cele pyramidy nezalezi)
#---------------------------------------------------------------

def blank_pyramid(n):
    indent = 0
    for i in range(1, n + 1):
        for j in range(1 - n, n):
            if j == indent or j == -indent or i == n :
                print("#", end = " ")
            elif j < indent and j > - indent:
                print(".", end = " ")
            else:
                print(" ", end = " ")
        indent += 1
        print()
blank_pyramid(5)

#---------------------------------------------------------------
# 4) Napiste funkci, ktera v textove hrafice vykresli presypaci hodiny (slozene
# ze dvou pyramid otocenych spicemi k sobe). Napr pro height = 9 funkce vykresli:
    # # # # # # # # #
      # # # # # # #
        # # # # #
          # # #
            #
          # # #
        # # # # #
      # # # # # # #
    # # # # # # # # #
#---------------------------------------------------------------

def hourhlass(height):
    indent = height / 2 - 0.5
    for i in range(1, height + 1):
        for j in range(1 - height, height):
            if j == indent or j == -indent or j < indent and j > - indent or indent < 0 and j > indent and j < - indent:
                print("#", end = " ")
            else:
                print(" ", end = " ")
        indent -= 1
        print()
hourhlass(9)

#---------------------------------------------------------------
# 5) Napiste funkci, ktera v zelvi grafice vykresli kruhovou vysec o uhlu angle a polomeru r.
# Kruh aproximujte 360uhelnikem, cara povede od stredu kruhu po polomeru k obvodu, po obvodu
# pak opise oblouk o danem uhlu a nakonec se vrati do stredu
#
# napr: pro uhel 40 stupnu vykresli neco jako dilek pizzy, pro 270 stupnu pacmana bez oka
#---------------------------------------------------------------

line = Turtle()
line.speed = 60

def circle_part(angle, r):

    line.forward(r)
    line.right(90)
    side = 2 * pi * r / 360
    n = 360

    for i in range (angle):
        line.forward(side)
        line.right(360/n)

    line.right(90)
    line.forward(r)

circle_part(270, 100)
