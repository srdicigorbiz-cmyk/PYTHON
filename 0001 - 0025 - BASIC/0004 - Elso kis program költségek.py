print("Üdvözöllek a kiadások programban!")
print("\nMenü:\n1. Irj be új kiadást\n2. Nézd meg az eddigi kiadásokat.\n3. Összesített és átlag kiadás\n4. Törölj minden kiadást a programból\n5. Kilépés")
expenses=[]

while True:
    
    choice=input("Válassz:")
    
    if choice == "5":
        print("Kilépés. Viszlát!")
        break
    if choice == "1":
        ex=float(input("Írd be a kiadás összegét:"))
        expenses.append(ex)
        print("Kiadás sikeresen hozzáadva!")
    if choice == "2":
        counter = 0
        if len(expenses) == 0:
            print("Még nincs evidentált kiadás.")
        else:
            for i in expenses:
                counter = counter + 1
                print(f"{counter}. {i}")
    if choice == "3":
        sum_exp=0
        if len(expenses) == 0:
            print("Még nincs evidentált kiadás.")
        else:
            for i in expenses:
                sum_exp += i
            lst_lenght=len(expenses)
            avg_exp=sum_exp/lst_lenght
            print(f"Kiadások összesen: {sum_exp}")
            print(f"Kiadások átlaga: {avg_exp}")
    if choice == "4":
        expenses.clear()
        print("Minden kiadás törölve.")
    if choice not in('1','2','3','4','5'):
        print('Téves választás. Próbáld meg újra.')