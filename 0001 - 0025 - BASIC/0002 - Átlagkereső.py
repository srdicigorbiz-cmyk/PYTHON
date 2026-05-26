#5. Feladat: Átlagkereső (Average Calculator)
#Az adatbázis-kezelés (SQL) egyik leggyakoribb művelete az átlagszámítás (AVG). Csináljuk meg ezt Pythonban!
#Feladat: Írj egy függvényt get_average(lst) néven. A függvény adja össze a lista elemeit, és ossza el az elemek számával.
#Segítség: Használd a sum(lst) és a len(lst) beépített függvényeket!
# Bónusz: Ha a lista üres, a program ne omoljon össze, hanem adjon vissza 0-t.
def get_average(lst):
    if len(lst) > 0:
        szuma=sum(lst)
        eredmeny=szuma/len(lst)
        return eredmeny
    else:
        return 0
raw_input=input("Ird be a szamokat vesszovel elvalasztva:")
num_lst=[]
if raw_input != "":
    spl_input=raw_input.split(",")
    for i in spl_input:
        num_lst.append(int(i.strip()))
result=get_average(num_lst)
print(f"Az átlag: {result}")