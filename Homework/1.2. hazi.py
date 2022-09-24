def valto(szam, egyseg):
    if egyseg == "cm":
        print("{:.2f}".format(int(szam)*0.393700787), "inches")
    elif egyseg == "inch":
        print(int(szam)*2.54, "cm")
    else:
        print("Not correct unit!")

if __name__ == "__main__":
    print("Adjon meg egy számot és egy mértékegységet (cm/inch):")
    mertek = float(input(""))
    mertekegyseg = input("")
    valto(mertek, mertekegyseg)