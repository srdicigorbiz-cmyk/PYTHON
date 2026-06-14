def find_words(lista, betu):
    if len(lista)==0:
        return ""
    
    if isinstance(lista[0], list):
        return find_words(lista[0], betu) + find_words(lista[1:], betu)
    else:
        if betu in lista[0]:
            return [lista[0]] + find_words(lista[1:], betu)
        else:
            return find_words(lista[1:], betu)




lista=["szavak", "orak", "zene", ["szamito", "zimbabwe"], "yukon"]
betu = 'y'
print(find_words(lista, betu))