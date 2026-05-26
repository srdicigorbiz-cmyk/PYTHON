mylist=['a', 'b','c']

try:
    index_number=int(input('Unesi broj:'))
    print(mylist[index_number])
    print(mylist[::-1])
    new_ist_item = (input('Unesi nov element lista:'))
    mylist.append(new_ist_item)
    print(f"osvezena lista: {mylist}")
except IndexError:
    print('los indeks')
except ValueError:
    print('unesi broj!')



L = [2,4,6,8,10]
L[1:4] = [7,9]
L.append(12)
L.insert(0,1)
del L[3]
print(L)