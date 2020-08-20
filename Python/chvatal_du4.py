# Ctvrta domaci uloha z IB111, 2016
#
# Piste co nejprehlednejsi kod, zejmena vhodne pojmenovavejte promenne
#           (za necitelny kod hrozi bodova srazka)
#
# Sve reseni pojmenujte jako "prijmeni_du4.py" a ulozte do prislusne odevzdavarny
#           (bez uvozovek a bez diakritiky)
# --------------------------------------------------------------
# zde muzete definovat pripadne importy
from random import randint
"""
[az 25 bodu]
Vytvorte program hrajici hru "Jednorozmerne piskvorky" proti uzivateli
Tato varianta se hraje na jednorozmernem planu dane velikosti. tzn. plan je predstavovan
posloupnosti o poctu policek rovnem velikosti planu. 
 - hraci se stridaji a delaji znacky do (dosud volnych) policek
 - oba hraci maji stejnou znacku, vyhrava zen hrac, ktery svym tahem zavrsi podposloupnost alespon 
      tri krizku vedle sebe
 - vasim ukolem je implementovat funkci "tictactoe(size, human_starts=True)"
    @parametr size              udava pocet policek na planu
    @parametr human_starts      znaci, ze zacina uzivatel     (v pripade false zacne pocitac)
    - ve funkci se tedy stridaji hrac a pocitac, muzete uvazovat rozumnou velikost planu (3-50 policek)
    - v kazdem kole vizualizujte stav hry (podle ukazky nize)
      - hlavne musi byt dobre patrne cislo u kazdeho pole -> na ukazce je pod kazdym polickem cislo
        urcujici "jednotky" v dane desitce a v radku jeste nize pak cislo urcujici desitku
        - tim je jednoduse zakodovano DVOJCIFERNE cislo tak, ze se bude dobre odsazovat
      - dale v kazdem tahu piste, kdo je na tahu a v pripade pocitace zduraznete, ktere pole voli
    - hracuv zah nacitejte ze vstupu, po hracove volb� tahu zkontrolujte, zda jde o korektni a dosud volnou pozici
      - pokud ne, tak varujte a zadost o vstup opakujte
    - pro volbu tahu pocitace napiste funkci "strategy(state)", ktera pro zadany plan "state"
    vybere vhodny tah pocitace
      - plan je reprezentovan jako pole/seznam znaku 'X' (umistena znacka) a '_' (prazdne policko)
      - v zakladni variante by mela funkce volit nejake volne policko, pokusy o inteligentnejsi vyber viz. bonus
      - funkci strategy(state) ve funkci tictactoe(size) skutecne volejte pro aktualni plan/stav hry
-------------------------------------------------------------------------------      
--------------------- ukazka funkce strategy:
state = ['_', '_', '_', 'X', 'X', '_', '_', 'X']
strategy(state)

vrati 2                 #to je 3. pozice (indexujeme od nuly). tim se zavrsi posloupnost 3 krizku
-------------------------------------------------------------------------------
---------------------- ukazka cele hry

tictactoe(26, human_starts=True)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
         0         |         1         |     2

Na tahu: hrac
Zadej tah: 1

X _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
         0         |         1         |     2

Na tahu: pocitac
Zahral na pozici: 4

_ X _ _ X _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
         0         |         1         |     2

Na tahu: hrac
Zadej tah: 6

_ X _ _ X _ X _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
         0         |         1         |     2

Na tahu: pocitac
Zahral na pozici: 5

_ X _ _ X X X _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
         0         |         1         |     2

Prohr�l jsi!
"""
state = []

#ocislovani pole
def field_base(size):
    iteration = 0
    bottom_num = 0
    while iteration != size:
        if iteration >= 9:
            print(iteration % 10, end=" ")
        else:
            print(iteration, end=" ")
        iteration += 1
    print()
    while iteration >= 9:
        print("         " + str(bottom_num) + "         |", end="")
        iteration -= 10
        bottom_num += 1
    for i in range(iteration - 1):
        print(" ", end="")
    print(bottom_num)
    for i in range(iteration - 1):
        print(" ", end="")

#kontrola, jesli neni konec
def is_end(state, size):
    position = 0
    for i in range(size-2):
        if state[position] == "X" and state[position + 1] == "X" and state[position + 2] == "X":
            return 42
        position += 1

#hraje hrac
def human_play(state, size):
    print("\nNa tahu: hrac")
    print("Zadej tah:", end=" ")
    position = (int(input()))
    if position >= size or position < 0 or state[position] == "X":
        print("\nposition not allowed")
        human_play(state, size)
    state[position] = "X"
    print("\n" + " ".join(state))
    field_base(size)
    if is_end(state, size) == 42:
        print ("\nVyhral jsi!")
        return
    strategy(state, size)

#hraje pocitac
def strategy(state, size):
    print("\nNa tahu: pocitac")
    position = 0
    position2 = 0
    number = randint(0, size-1)
    while state[number] == "X":
        number = randint(0, size-1)

    #zakonci pri dvou X vedle sebe
    for i in range(size - 2):
        if state[position] == "X" and state[position + 1] == "X":
            number = position + 2
            if state[position] == state[size - 2]:
                number = size - 3
                break
        position += 1

    #zakonci pri X_X
    for j in range(size - 3):
        if state[position2] == "X" and state[position2 + 2] == "X":
            number = position2 + 1
            break
        position2 += 1
        
    print("Zahral na pozici: " + str(number) + "\n")
    state[number] = "X"
    print(" ".join(state))
    field_base(size)
    if is_end(state, size) == 42:
        print("\nProhral jsi!")
        return
    human_play(state, size)

def tictactoe(size, human_starts=True):
    for i in range(size):
        state.append("_")
    print(" ".join(state))
    field_base(size)
    if human_starts == True:
        human_play(state, size)
    else:
        strategy(state, size)

tictactoe(26)

"""
BONUS
Jakekoliv inteligentnejsi reseni funkce   strategy(state)    muze byt oceneno bonusovymi body. Staci
1) implementovat lepsi algoritmus pro vyber pozice
2) v komentari v prislusne casti hodu napsat, jake optimalizace vyberu mate implementovany
        napr. #tady se divam, jestli nemohu na nejake pozici zavrsit 3posloupnost a pokud ano, ....

"""