import string

def szoveg():
    with open("hazi.txt", "r", encoding="UTF-8") as fajl:
        tartalom = fajl.read().splitlines()
        with open("ki.txt", "w", encoding='utf-8') as fajl2:
            maganhangzo = "aáeéiíoóöőuúüű"
            n = 1
            mondat = ""
            for sor in tartalom:
                if sor != '':
                    if n % 3 == 0:
                        for betu in sor:
                            if betu not in string.punctuation and betu not in maganhangzo:
                                    mondat += betu
                        mondat += "\n"
                    n += 1
            fajl2.write(mondat)

if __name__ == "__main__":
    szoveg()