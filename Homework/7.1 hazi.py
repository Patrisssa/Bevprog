def binaris_kereses(lista):
    keresett = 70
    n = len(lista)
    also, felso = 0, n-1
    db = 0

    while also <= felso:
        db += 1
        k = (felso+also) // 2
        if keresett < lista[k]:
            felso = k - 1
        elif keresett > lista[k]:
            also = k + 1
        else:
            break
            
    print("Alsó érték: ", also, "\nFelső érték: ", felso, "\nk érték: ", k, "\nLépések száma: ", db)


if __name__ == "__main__":
    lista = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
    binaris_kereses(lista)
