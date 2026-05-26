def rejtelyes_szamlalo(szam):
    if szam == 0:
        print("Kilőttünk!")
        return
    print(szam)
    rejtelyes_szamlalo(szam - 1)  # Előbb hívom meg újra
    print(szam)  # És csak utána írom ki

rejtelyes_szamlalo(3)