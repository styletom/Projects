from random import randint

class World(object):
    def __init__(self, sirka, vyska, procentoZdi, pocetDuchu):
        #seznam duchu
        #hrac inicializace
            #self.hrac = Hrac(self)
        #seznam zdi
        #cil (candy) - X a Y souradnice
        self.sirka = sirka
        self.vyska = vyska
        self.procentoZdi = procentoZdi
        self.pocetDuchu = pocetDuchu


    def generateCandy(self, numOfPos):
        candy = randint(0, numOfPos)
        return candy

    def printState(self):
        numOfPos = self.sirka*self.vyska
        listWall = []
        for i in range(numOfPos//100*self.procentoZdi):
            random = randint(0, numOfPos)
            listWall.append(random)

        list1 = []
        for j in range(numOfPos+1):
            list1.append(j)
        for l in listWall:
            list1[l] = "⬛"

        candy = self.generateCandy(numOfPos)
        while list1[candy] == "⬛":
            candy = self.generateCandy(numOfPos)
        list1[candy] = "*"

        #hrac a duchove jen na pozici, vice jsem nestihl
        hrac = randint(0, numOfPos)
        while list1[hrac] == "⬛" or list1[hrac] == "*":
            hrac = randint(0, numOfPos)
        list1[hrac] = "o"

        duch1 = randint(0, numOfPos)
        while list1[duch1] == "⬛" or list1[duch1] == "*" or list1[duch1] == "o":
            duch1 = randint(0, numOfPos)
        list1[duch1] = "x"

        duch2 = randint(0, numOfPos)
        while list1[duch2] == "⬛" or list1[duch2] == "*" or list1[duch2] == "o":
            duch2 = randint(0, numOfPos)
        list1[duch2] = "x"

        for k in range(numOfPos):
            if k%self.sirka == 0:
                print()
            if list1[k] == "⬛":
                print("⬛", end="")
            elif list1[k] == "*":
                print("*", end="")
            elif list1[k] == "o":
                print("o", end="")
            elif list1[k] == "x":
                print("x", end="")
            else:
                list1[-1] = "⬚"
                print(list1[-1], sep='', end ="")

"""
#    def isValidPositionForPlayer(x, y):
        #nevalidni: mimo plochu, zed

#    def isValidPositionForGhost(x, y):
        #nevalidni: mimo plochu, zed. jiny duch

	
#class Hrac(object):
#	def __init__(self, world):
	#polohaX, polohaY
	#seznam navstivenych poloh
	
	def getSymbol():
		#vrati reprezentaci, jak je hrac vyobrazen
	def isDead():
		pass
	def moveByCommand():
		#input + vyhodnoceni
		#zavola move()

	def move(x, y):
		#meni polohu, pridava do seznamu navstivenych poloh
	# ...."""
		


"""class Duch(object):
	def __init__(self, world) 
		#polohaX, polohaY

	def move():
		#pohyb
	# ...."""
		
#definujte podle sebe
def game():
        world = World(30, 20, 10, 2)
        world.printState()

"""    while True:
        #...
        if World.hrac.isDead():
            break
		"""
game()