import string

def palindrom(szoveg):
    mondat = ""
    for i in szoveg:
        if i not in string.punctuation:
            mondat += i
    mondat = mondat.lower().replace(" ","")

    dupla = ["cs","dz","dzs","gy","ly","ny","sz","ty","zs"]
    mondat2 = ""
    sorsz = 0
    while sorsz < len(mondat):
        if sorsz < len(mondat) - 1 and (mondat[sorsz] + mondat[sorsz + 1]) in dupla:
            for betu in dupla:
                if mondat[sorsz] + mondat[sorsz + 1] == betu:
                    mondat2 = mondat2 + betu[::-1]
                    sorsz += 2
        else:
            mondat2 = mondat2 + mondat[sorsz]
            sorsz += 1

    for i in range(len(mondat)):
        if mondat[i] != mondat2[- i - 1]:
            print("Nem palindróm")
            break
    else:
        print("Palindróm")

if __name__ == "__main__":
    szoveg = input("Adja meg a szöveget! ")
    palindrom(szoveg)