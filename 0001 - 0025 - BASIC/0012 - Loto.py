def loto():
    winning_numbers=[]
    loto_set = set(range(1, 40))
    for i in range(6):
        num=loto_set.pop()
        winning_numbers.append(num)
    print(f"Winning numbers are: {winning_numbers}")

def menu():
    while True:
        print("L O T O by Srdic Igor")
        print("---------------------")
        print("1. Play loto.")
        print("2. Exit")
        print("---------------------")
        choice=int(input("Enter your choice:"))
        if choice == 1 or choice == '1':
            loto()
        else:
            print("Good bye!")
            break

menu()

