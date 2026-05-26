#Feladat: A "Pozitív Szűrő" (Only Positives)
#Gyakran előfordul, hogy egy adatsorból csak a releváns (például pozitív) számokra van szükségünk.
#Feladat: Írj egy függvényt filter_positives(lst) néven, amely egy számokat tartalmazó listából 
# kiválogatja a 0-nál nagyobb számokat, és egy új listában adja vissza őket.

#Példa: [10, -5, 0, 3, -1] -> [10, 3]
def filter_positives(lst):
    pos_list=[]
    for l in lst:
        if l > 0:
            pos_list.append(l)
    return pos_list

raw_input=input("Irj be szamokat vesszovel elvalasztva:")
spl_input=raw_input.split(",")
num_list=[]
for s in spl_input:
    num_list.append(int(s.strip()))
result = filter_positives(num_list)
print(result)