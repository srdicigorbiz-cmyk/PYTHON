buvos_szam = 42
while True:
    szam = int(input("Tippelj:"))
    if szam == buvos_szam:
        print("Gratulálok, kitaláltad!")
        break
    elif szam < buvos_szam:
        print("Nagyobb számra gondoltam.")
    elif szam > buvos_szam:
        print("Kisebb számra gondoltam.")
