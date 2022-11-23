def buborekrendezes(szamok):
    for k in range(0, len(szamok)):
        for i in range(1, len(szamok)-k):
            if szamok[i-1] > szamok[i]:
                szamok[i], szamok[i-1] = szamok[i-1], szamok[i]
    print(szamok)


if __name__ == "__main__":
    lista = [54, 76, 23, 45, 21, 5, 67, 22, 12, 64, 26, 59, 82, 99]
    buborekrendezes(lista)
