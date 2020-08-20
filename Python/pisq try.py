#class Book:
#    def __init__(self, author, title, isbn):
#        self.author = author
#        self.title = title
#        self.isbn = isbn
#
#    dune = Book("Frank", "Dune", "646546846541")
#    temno = Book("Balzar", "Teorie", "9+55+5+5")

class Nadoba(object):
    def __init__(self, vyska, voda = 0):
        self.vyska = vyska
        self.voda = voda
        print(self.voda)
        print(self.vyska)
    def prazdna(self):
        return (self.voda == 0)

    def plna(self):
        return self.voda == self.vyska

    def prilij(self, mnozstvi):
        self.voda += mnozstvi
        if self.voda > self.vyska:
            self.voda = self.vyska

    def vykresli(self):
        for i in range(self.vyska-1, -1, -1):
            if i > self.voda:
                print("|  |")
            else:
                print("|**|")
        print("----")

    def __str__(self):
        pass


odmValec = Nadoba(12, 5)
odmValec.vykresli()
odmValec.prilij(13)
odmValec.vykresli()
