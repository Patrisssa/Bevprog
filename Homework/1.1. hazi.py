def mondat_elemzes(name):
    gyakorisag= {}
    for betu in set(name):
        gyakorisag[betu] = name.count(betu)
    print("Betűk gyakorisága: ", gyakorisag)

    print(f"Fordítva: {name[::-1]}")

    print("Listába rendezve szavanként: ", name.split(" "), "\n")

if __name__ == "__main__":
    mondat = input("Adjon meg egy mondatot: \n")
    mondat_elemzes(mondat)
