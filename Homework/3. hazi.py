def nulla_osztas(a,b):
    try:
        hanyados = a/b
        print(hanyados)
    except ZeroDivisionError:
        print("Division by zero not allowed")
    finally:
        print("Out of try except blocks")

if __name__ == "__main__":
    beker = True
    while beker:
        a = int(input("Enter 'a' value: "))
        b = int(input("Enter 'b' value: "))
        nulla_osztas(a,b)