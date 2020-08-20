# Druha domaci uloha z IB111, 2016
#
# Piste co nejprehlednejsi kod, zejmena vhodne pojmenovavejte promenne
#           (za necitelny kod hrozi bodova srazka)
#
# Sve reseni pojmenujte jako "prijmeni_du2.py" a ulozte do prislusne odevzdavarny
#           (bez uvozovek a bez diakritiky)
# --------------------------------------------------------------
# zde muzete definovat pripadne importy

from random import randint

#1) [az 11 bodu] Napiste funkci simulujici velmi jednoduchy soubojovy system podobny systemu z RPG her
#pravidla jsou nasledujici:
# - boj probiha jako sekvence kol, v kazdem kole utoci hrac (player) na nestvuru (monster)
#        (nestvura na hrace nikdy neutoci)
# - sila hracova utoku je vypoctena jako hod 6stennou kostkou + zakladni utok (predavany 1. parametrem)
# - sila obrany nestvury se vypocita jako samotny hod 6stennou kostkou (zadnou zakladni obranu nepricitame)
#          !! padne-li (na utok nebo na obranu) sestka, hazi se znovu a hodnoty se pricitaji!! (ukazka: round 13)
# - nestvura ma zadany pocet zivotu (2. parametrem). Klesne-li na/pod nulu, simulace konci
#		!! u nestvury vypiste 0 hitpoints, ne zapornou hodnotu
# - pokud je sila utoku vyssi, nez sila obrany, nestvura ztraci tolik zivotu, kolik je rozdil techto hodnot
#
# - definujte jeste 3. parametr "output", ktery pokud je roven True, zajisti vypisovani stavu hry:
# - v kazdem kole vypisujte hozene hodnoty hracem (pred pricitanim) a nestvurou
# - pokud byla zranena nestvura, vypiste o kolik a kolik zivotu z kolika ji zbyva
# - na konci vypiste, po kolika kolech simulace skoncila
#------------------------------------------------------------------
#ukazka: simple_fight(4, 42)
#------------------------------------------------------------------
#1. round: player throws 3, monster throws 5.
#	Monster was hit for 2, remaining 40/42 hitpoints.
#
#2. round: player throws 5, monster throws 3.
#	Monster was hit for 6, remaining 34/42 hitpoints.
#
#3. round: player throws 3, monster throws 4.
#	Monster was hit for 3, remaining 31/42 hitpoints.
#
#4. round: player throws 3, monster throws 2.
#	Monster was hit for 5, remaining 26/42 hitpoints.
#
#5. round: player throws 4, monster throws 5.
#	Monster was hit for 3, remaining 23/42 hitpoints.
#
#6. round: player throws 1, monster throws 5.
#
#7. round: player throws 1, monster throws 5.
#
#8. round: player throws 4, monster throws 2.
#	Monster was hit for 6, remaining 17/42 hitpoints.
#
#9. round: player throws 3, monster throws 5.
#	Monster was hit for 2, remaining 15/42 hitpoints.
#
#10. round: player throws 2, monster throws 1.
#	Monster was hit for 5, remaining 10/42 hitpoints.
#
#11. round: player throws 1, monster throws 2.
#	Monster was hit for 3, remaining 7/42 hitpoints.
#
#12. round: player throws 2, monster throws 1.
#	Monster was hit for 5, remaining 2/42 hitpoints.
#
#13. round: player throws 4, monster throws 8.
#
#14. round: player throws 1, monster throws 2.
#	Monster was hit for 3, remaining 0/42 hitpoints.
#
#Game ended in 14. round

def roll_the_dice():
    num = randint(1,6)
    while num % 6 == 0:
        next = randint(1,6)
        num += next
    return num

def simple_fight(attack, max_hp, output):
    count = 1
    curr_hp = max_hp

    while curr_hp > 0:
        player_dice = roll_the_dice()
        monster_dice = roll_the_dice()

        #print 1st line
        if output == True:
            print(str(count) + ". round: player throws" ,end=" ")
            x = player_dice
            while x > 6:
                print(6, end=" ")
                x -= 6
            print(x, end="")
            print(", monster throws", end=" ")
            y = monster_dice
            while y > 6:
                print(6, end=" ")
                y -= 6
            print(str(y) + ".")
        player_dice += attack

        #print 2nd line
        if player_dice > monster_dice:
            monster_hit = player_dice - monster_dice
            curr_hp = curr_hp - monster_hit
            if curr_hp < 0:
                curr_hp = 0
            if output == True:
                print("  Monster was hit for " + str(monster_hit) + ", remaining " + str(curr_hp) + "/" + str(max_hp) + " hitpoints.")
        if output == True:
            print()
        count += 1
    global rounds
    rounds = count - 1

    if output == True:
        print("Game ended in " + str(rounds) + ". round\n")
    return rounds
simple_fight(4, 42, True)

#2) [az 4 body] Napiste funkci, ktera pro 1000 opakovani simulaci z bodu 1) s parametry attack, max_hp
#vypocte prumerny pocet kol.
#------------------------------------------------------------------
#ukazka: simple_fight_stats(4, 42)
#------------------------------------------------------------------
#For attack 4 and 42 hitpoints, average simulation length is 9.925 rounds.

def simple_fight_stats(attack, max_hp, output):
    sum_rounds = 0
    for i in range(1000):
        simple_fight(attack, max_hp, output)
        sum_rounds += rounds
        average = sum_rounds/1000
    print("For attack " + str(attack) + " and " + str(max_hp) + " hitpoints, average simulation length is " + str(average) + " rounds.")
simple_fight_stats(4, 42, False)

#Bonus: [az 3 body] upravte program z bodu 1 tak, aby se v pripade opakovani hodu po padnuti sestky
#vypisovaly hodnoty jednotlivych hodu oddelenych mezerou. Priklad:
#
#....
#13. round: player throws 4, monster throws 6 2.
#...
