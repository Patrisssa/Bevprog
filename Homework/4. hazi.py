class Team:
    def __init__(self, nev, projekt, szerepkor):
        self.nev = nev
        self.projekt = projekt
        self.szerepkor = szerepkor

    def __str__(self):
        return ("-- Developer létrehozva. --\n" + self.nev + " a " + self.projekt + "-en dolgozik " + self.szerepkor + " szerepkörben.\n")

    def __eq__(self, other_dev):
        if self.projekt == other_dev.projekt:
            return (self.nev + " és " + other_dev.nev + " dolgoznak egy projekten.")

def developers():
    p1 = Team("Ricsi", "SolArch", "Frontend")
    p2 = Team("Angéla", "ZerTeng", "Tesztelő")
    p3 = Team("Peti", "KefERP", "Backend")
    p4 = Team("Éva", "KefERP", "Frontend")
    print(p1, p2, p3, p4)

    devs = [p1, p2, p3, p4]
    for i in range(len(devs)):
        for x in range(i+1, len(devs)):
                if (devs[i] == devs[x]) != None:
                    print(devs[i] == devs[x])

if __name__ == "__main__":
    developers()


